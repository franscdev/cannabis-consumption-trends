"""
Statistical analysis utilities for the Cannabis Consumption Trends project.

Provides reusable functions for descriptive trend analysis,
year-over-year changes, and Pearson correlations.
"""

import numpy as np
import pandas as pd


GROUP_COLUMNS = ["drug", "time", "grade"]


def calculate_yoy_changes(
    dataframe: pd.DataFrame,
) -> pd.DataFrame:
    """Calculate prevalence changes between consecutive years."""

    required = GROUP_COLUMNS + ["year", "estimate"]

    if not set(required).issubset(dataframe.columns):
        raise ValueError("Missing required analysis columns.")

    result = dataframe.copy()

    result = result.sort_values(
        GROUP_COLUMNS + ["year"]
    )

    grouped = result.groupby(GROUP_COLUMNS)

    previous_year = grouped["year"].shift(1)
    previous_estimate = grouped["estimate"].shift(1)

    consecutive_years = (
        result["year"] - previous_year == 1
    )

    result["yoy_change_pp"] = (
        result["estimate"] - previous_estimate
    ).where(consecutive_years)

    return result.reset_index(drop=True)


def calculate_linear_trend(
    dataframe: pd.DataFrame,
) -> dict:
    """Calculate a descriptive ordinary least squares trend."""

    required = ["year", "estimate"]

    if not set(required).issubset(dataframe.columns):
        raise ValueError("Missing year or estimate columns.")

    data = dataframe[required].dropna().copy()

    data = data.sort_values("year")

    if len(data) < 2:
        raise ValueError("At least two observations are required.")

    if data["year"].nunique() < 2:
        raise ValueError("At least two distinct years are required.")

    x = data["year"].to_numpy(dtype=float)
    y = data["estimate"].to_numpy(dtype=float)

    baseline_year = x.min()
    centered_x = x - baseline_year

    slope, intercept = np.polyfit(
        centered_x,
        y,
        1
    )

    predicted = slope * centered_x + intercept

    ss_res = np.sum((y - predicted) ** 2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)

    r_squared = (
        1 - ss_res / ss_tot
        if ss_tot > 0
        else np.nan
    )

    return {
        "start_year": int(x.min()),
        "end_year": int(x.max()),
        "observations": len(data),
        "slope_pp_per_year": float(slope),
        "intercept": float(intercept),
        "r_squared": float(r_squared),
    }


def calculate_pearson_correlation(
    dataframe: pd.DataFrame,
    categories: list[str],
    grade: str,
    start_year: int,
    end_year: int,
    use_yoy_changes: bool = False,
) -> pd.DataFrame:
    """Calculate correlations between annual prevalence series."""

    required = [
        "drug",
        "grade",
        "year",
        "estimate"
    ]

    if not set(required).issubset(dataframe.columns):
        raise ValueError("Missing required correlation columns.")

    filtered = dataframe[
        (dataframe["drug"].isin(categories))
        & (dataframe["grade"] == grade)
        & (dataframe["year"].between(start_year, end_year))
    ].copy()

    if "time" in filtered.columns:
        filtered = filtered[
            filtered["time"] == "12 Month"
        ]

    prevalence = filtered.pivot(
        index="year",
        columns="drug",
        values="estimate"
    ).reindex(
        index=range(start_year, end_year + 1),
        columns=categories
    )

    if prevalence.isna().any().any():
        raise ValueError(
            "Incomplete observations for the selected period."
        )

    if use_yoy_changes:
        prevalence = prevalence.diff().dropna()

    if len(prevalence) < 3:
        raise ValueError(
            "At least three observations are required."
        )

    return prevalence.corr(method="pearson")