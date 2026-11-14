"""
Data processing utilities for the Cannabis Consumption Trends project.

Provides reusable functions for loading, cleaning, and validating
Monitoring the Future prevalence datasets.
"""

from pathlib import Path

import pandas as pd


REQUIRED_COLUMNS = [
    "drug",
    "time",
    "grade",
    "estimate",
    "year",
]

OBSERVATION_KEYS = [
    "drug",
    "time",
    "grade",
    "year",
]


def load_raw_data(raw_directory: str | Path) -> pd.DataFrame:
    """Load and combine Monitoring the Future CSV files."""

    raw_directory = Path(raw_directory)

    csv_files = sorted(raw_directory.glob("*.csv"))

    if not csv_files:
        raise FileNotFoundError(
            f"No CSV files found in {raw_directory}"
        )

    dataframes = [
        pd.read_csv(file)
        for file in csv_files
    ]

    return pd.concat(
        dataframes,
        ignore_index=True
    )


def clean_prevalence_data(
    dataframe: pd.DataFrame,
) -> pd.DataFrame:
    """Select and standardize prevalence columns."""

    missing_columns = set(REQUIRED_COLUMNS) - set(
        dataframe.columns
    )

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {sorted(missing_columns)}"
        )

    cleaned = dataframe[REQUIRED_COLUMNS].copy()

    cleaned["estimate"] = pd.to_numeric(
        cleaned["estimate"],
        errors="raise"
    )

    cleaned["year"] = pd.to_numeric(
        cleaned["year"],
        errors="raise"
    ).astype(int)

    cleaned = cleaned.sort_values(
        OBSERVATION_KEYS
    ).reset_index(drop=True)

    return cleaned


def validate_prevalence_data(
    dataframe: pd.DataFrame,
) -> dict:
    """Validate dataset completeness, uniqueness, and prevalence limits."""

    missing_columns = set(REQUIRED_COLUMNS) - set(
        dataframe.columns
    )

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {sorted(missing_columns)}"
        )

    checks = {
        "no_missing_values": not dataframe[
            REQUIRED_COLUMNS
        ].isna().any().any(),

        "unique_observations": not dataframe.duplicated(
            subset=OBSERVATION_KEYS
        ).any(),

        "valid_prevalence_range": dataframe[
            "estimate"
        ].between(0, 100).all(),
    }

    return {
        "total_observations": len(dataframe),
        "checks": checks,
        "all_passed": all(checks.values()),
    }


def save_processed_data(
    dataframe: pd.DataFrame,
    output_path: str | Path,
) -> None:
    """Save a processed dataset to CSV."""

    output_path = Path(output_path)

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    dataframe.to_csv(
        output_path,
        index=False
    )