"""Unit tests for reusable statistical analysis functions."""

import pandas as pd
import pytest

from src.analysis import (
    calculate_yoy_changes,
    calculate_linear_trend,
    calculate_pearson_correlation,
)

from src.data_processing import (
    clean_prevalence_data,
    validate_prevalence_data,
)


@pytest.fixture
def sample_data():
    """Create a small synthetic dataset with known values."""

    return pd.DataFrame({
        "drug": ["Cannabis"] * 4,
        "time": ["12 Month"] * 4,
        "grade": ["12th Grade"] * 4,
        "year": [2021, 2022, 2023, 2024],
        "estimate": [10.0, 12.0, 14.0, 16.0],
    })


def test_data_validation(sample_data):
    """Verify valid observations pass integrity checks."""

    cleaned = clean_prevalence_data(sample_data)
    result = validate_prevalence_data(cleaned)

    assert result["total_observations"] == 4
    assert result["all_passed"]


def test_yoy_changes(sample_data):
    """Verify annual prevalence differences."""

    result = calculate_yoy_changes(sample_data)

    assert result["yoy_change_pp"].dropna().tolist() == [
        2.0, 2.0, 2.0
    ]


def test_linear_trend(sample_data):
    """Verify a perfectly linear prevalence trend."""

    result = calculate_linear_trend(sample_data)

    assert result["slope_pp_per_year"] == pytest.approx(2.0)
    assert result["r_squared"] == pytest.approx(1.0)


def test_invalid_prevalence(sample_data):
    """Verify that invalid prevalence estimates are detected."""

    invalid = sample_data.copy()
    invalid.loc[0, "estimate"] = 120.0

    result = validate_prevalence_data(invalid)

    assert not result["all_passed"]