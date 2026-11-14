import pandas as pd
from pathlib import Path

# Define project paths
PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_PATH = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "cannabis_prevalence_clean.csv"
)

# Load dataset
df = pd.read_csv(DATA_PATH)

# Selected published reference estimates
official_estimates = [
    {
        "drug": "Cannabis",
        "time": "12 Month",
        "grade": "8th Grade",
        "year": 2025,
        "expected": 7.6,
    },
    {
        "drug": "Cannabis",
        "time": "12 Month",
        "grade": "10th Grade",
        "year": 2025,
        "expected": 15.6,
    },
    {
        "drug": "Cannabis",
        "time": "12 Month",
        "grade": "12th Grade",
        "year": 2025,
        "expected": 25.7,
    },
]

# Validate selected observations
for reference in official_estimates:

    matching = df[
        (df["drug"] == reference["drug"])
        & (df["time"] == reference["time"])
        & (df["grade"] == reference["grade"])
        & (df["year"] == reference["year"])
    ]

    assert len(matching) == 1, (
        f"Invalid observation count: {reference}"
    )

    actual = matching["estimate"].iloc[0]
    expected = reference["expected"]

    assert abs(actual - expected) < 0.001, (
        f"Value mismatch: expected {expected}, got {actual}"
    )

    print(
        f"PASSED | {reference['grade']} | "
        f"{reference['year']} | {actual}%"
    )

print("\nALL SELECTED OFFICIAL ESTIMATES VERIFIED")