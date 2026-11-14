"""
Visualization utilities for the Cannabis Consumption Trends project.

Provides reusable chart styling, branding, and export functions.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd


COLORS = {
    "background": "#0B1120",
    "panel": "#111827",
    "text": "#F8FAFC",
    "muted": "#94A3B8",
    "grid": "#334155",
    "accent": "#34D399",
}

GRADE_COLORS = {
    "8th Grade": "#34D399",
    "10th Grade": "#38BDF8",
    "12th Grade": "#A78BFA",
}


def configure_theme() -> None:
    """Configure the Greencloudz visualization theme."""

    available_fonts = {
        font.name for font in fm.fontManager.ttflist
    }

    font_family = next(
        (
            font
            for font in ["Montserrat", "Aptos", "DejaVu Sans"]
            if font in available_fonts
        ),
        "DejaVu Sans",
    )

    plt.rcParams.update({
        "font.family": font_family,
        "font.size": 11,
        "figure.facecolor": COLORS["background"],
        "axes.facecolor": COLORS["panel"],
        "axes.edgecolor": COLORS["grid"],
        "axes.labelcolor": COLORS["muted"],
        "text.color": COLORS["text"],
        "xtick.color": COLORS["muted"],
        "ytick.color": COLORS["muted"],
        "grid.color": COLORS["grid"],
        "savefig.facecolor": COLORS["background"],
    })


def plot_prevalence_trends(
    dataframe: pd.DataFrame,
    drug: str,
    reporting_interval: str = "12 Month",
    start_year: int | None = None,
    end_year: int | None = None,
    logo_path: str | Path | None = None,
):
    """Plot prevalence trends across educational grades."""

    configure_theme()

    required = {"drug", "time", "grade", "year", "estimate"}

    if not required.issubset(dataframe.columns):
        raise ValueError("Missing required visualization columns.")

    filtered = dataframe[
        (dataframe["drug"] == drug)
        & (dataframe["time"] == reporting_interval)
    ].copy()

    if start_year is not None:
        filtered = filtered[filtered["year"] >= start_year]

    if end_year is not None:
        filtered = filtered[filtered["year"] <= end_year]

    if filtered.empty:
        raise ValueError("No observations match the selected filters.")

    fig, ax = plt.subplots(figsize=(14, 7))

    for grade, color in GRADE_COLORS.items():
        grade_data = filtered[
            filtered["grade"] == grade
        ].sort_values("year")

        if grade_data.empty:
            continue

        ax.plot(
            grade_data["year"],
            grade_data["estimate"],
            label=grade,
            color=color,
            linewidth=2.5,
            marker="o",
            markersize=3,
        )

    ax.set_title(
        f"{drug} | {reporting_interval} Prevalence",
        fontsize=17,
        fontweight="bold",
        color=COLORS["text"],
        pad=25,
    )

    ax.set_xlabel("Year")
    ax.set_ylabel("Prevalence (%)")
    ax.set_ylim(bottom=0)

    ax.grid(
        True,
        axis="y",
        alpha=0.35,
    )

    ax.legend(
        frameon=False,
        labelcolor=COLORS["text"],
    )

    for spine in ax.spines.values():
        spine.set_visible(False)

    fig.text(
        0.08,
        0.025,
        "Source: Monitoring the Future | University of Michigan",
        fontsize=9,
        color=COLORS["muted"],
    )

    if logo_path is not None:
        logo_path = Path(logo_path)

        if logo_path.exists():
            logo_ax = fig.add_axes([0.80, 0.88, 0.15, 0.08])
            logo_ax.imshow(plt.imread(logo_path))
            logo_ax.axis("off")

    fig.subplots_adjust(
        left=0.08,
        right=0.95,
        top=0.82,
        bottom=0.15,
    )

    return fig, ax


def export_figure(
    figure,
    output_path: str | Path,
    dpi: int = 300,
) -> None:
    """Export a figure to the specified location."""

    output_path = Path(output_path)

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    figure.savefig(
        output_path,
        dpi=dpi,
        bbox_inches="tight",
        facecolor=figure.get_facecolor(),
    )