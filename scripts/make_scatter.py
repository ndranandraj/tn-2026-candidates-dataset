#!/usr/bin/env python3
"""
make_scatter.py — TN 2026 namesake-count × 2021-margin scatter plot.

Reads the candidates CSV (schema documented in ../DATA_DICTIONARY.md),
aggregates to one point per constituency, and produces a 1080x1080
PNG suitable for r/dataisbeautiful.

Usage
-----
    python make_scatter.py INPUT_CSV OUTPUT_PNG [--sample]

    --sample   Render a "SAMPLE / ILLUSTRATIVE" watermark in the corner.
               Use this before real data is loaded, so preview images
               can't be confused with the final release.

The chart design choices:
  • X-axis: 2021 winning margin, in percentage points (log-ish feel
    via a square-root scale — compresses the boring high-margin seats
    and expands the tight-margin band where the story lives).
  • Y-axis: Count of namesake candidates filed for 2026 in that
    constituency. Integer, jittered a hair for visibility.
  • Point colour: red for flagged (margin < 5 AND namesakes ≥ 2),
    grey otherwise.
  • Labels: only the flagged outliers (top N by namesake count).
  • Footer: source + dataset URL + license.

Design is deliberately neutral — no party colours — so the chart reads
as a data artifact rather than a political statement.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")  # headless
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np
import pandas as pd

# ---------- Design tokens (matches blog palette) -----------------------

NAVY = "#1E2761"
CORAL = "#F96167"
INK = "#0F172A"
MUTED = "#94A3B8"
BG = "#FFFFFF"
GRID = "#E2E8F0"

TITLE_FONT = {"fontsize": 18, "fontweight": "bold", "color": INK}
SUBTITLE_FONT = {"fontsize": 11, "color": "#475569"}
AXIS_FONT = {"fontsize": 12, "color": INK}
TICK_FONT = {"labelsize": 11, "colors": "#334155"}
FOOTER_FONT = {"fontsize": 8, "color": "#64748B"}

DPI = 135                 # 1080 / 8 in = 135
FIGSIZE = (8, 8)          # 1080 x 1080 px

FLAG_MARGIN = 5.0         # percentage points
FLAG_MIN_NAMESAKES = 2

# ---------- Data loading -----------------------------------------------

def load_aggregate(csv_path: Path) -> pd.DataFrame:
    """
    Load candidates CSV; aggregate to one row per constituency with
    margin_pct_2021 and namesake_count_2026.
    """
    df = pd.read_csv(csv_path)

    # Only 2026 filings contribute to namesake_count_2026
    cur = df[df["year"] == 2026].copy()

    namesake = (
        cur.dropna(subset=["namesake_group_id"])
           .groupby("constituency_code")
           .size()
           .rename("namesake_count_2026")
    )

    # margin_pct_2021 is constant within a constituency — take the first
    margin = (
        df.dropna(subset=["margin_pct_2021"])
          .drop_duplicates("constituency_code")
          .set_index("constituency_code")[["constituency_name", "margin_pct_2021"]]
    )

    agg = margin.join(namesake, how="left").fillna({"namesake_count_2026": 0})
    agg["namesake_count_2026"] = agg["namesake_count_2026"].astype(int)
    agg["flag"] = (
        (agg["margin_pct_2021"] < FLAG_MARGIN) &
        (agg["namesake_count_2026"] >= FLAG_MIN_NAMESAKES)
    )
    return agg.reset_index()


# ---------- Plot -------------------------------------------------------

def render(agg: pd.DataFrame, output: Path, sample: bool = False) -> None:
    fig, ax = plt.subplots(figsize=FIGSIZE, dpi=DPI, facecolor=BG)
    ax.set_facecolor(BG)

    # Jitter the y-axis a little so overlapping integer points are visible
    rng = np.random.default_rng(42)
    y_jitter = agg["namesake_count_2026"] + rng.uniform(-0.15, 0.15, size=len(agg))

    # Non-flagged points
    base = agg[~agg["flag"]]
    ax.scatter(
        base["margin_pct_2021"],
        y_jitter[~agg["flag"].values],
        s=28, color=MUTED, alpha=0.55, edgecolor="none", label="Other constituencies",
    )

    # Flagged points
    flagged = agg[agg["flag"]]
    ax.scatter(
        flagged["margin_pct_2021"],
        y_jitter[agg["flag"].values],
        s=72, color=CORAL, alpha=0.9, edgecolor=NAVY, linewidth=0.8,
        label=f"Margin < {FLAG_MARGIN}pp · ≥{FLAG_MIN_NAMESAKES} namesakes",
    )

    # Shade the "danger zone"
    ax.axvspan(0, FLAG_MARGIN, ymin=0, ymax=1, color=CORAL, alpha=0.06, zorder=0)

    # Label top outliers — pick the 5 with the highest namesake count,
    # break ties by tightest 2021 margin, then stagger offsets vertically
    # so labels don't pile up.
    top = (flagged
           .sort_values(["namesake_count_2026", "margin_pct_2021"],
                        ascending=[False, True])
           .head(5))
    offsets = [(8, 10), (8, -14), (8, 22), (8, -26), (8, 34)]
    for (_, row), (dx, dy) in zip(top.iterrows(), offsets):
        ax.annotate(
            str(row["constituency_name"]),
            xy=(row["margin_pct_2021"], row["namesake_count_2026"]),
            xytext=(dx, dy), textcoords="offset points",
            fontsize=10, color=NAVY, fontweight="bold",
            path_effects=[pe.withStroke(linewidth=3, foreground="white")],
            arrowprops=dict(arrowstyle="-", color=NAVY, lw=0.6, alpha=0.6),
        )

    # Scale & ticks
    ax.set_xscale("function", functions=(np.sqrt, np.square))
    ax.set_xlim(0, max(20, agg["margin_pct_2021"].max() * 1.05))
    ax.set_ylim(-0.5, max(6, agg["namesake_count_2026"].max() + 1))
    ax.yaxis.get_major_locator().set_params(integer=True)
    ax.tick_params(axis="both", **TICK_FONT)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color("#CBD5E1")
    ax.grid(True, color=GRID, linewidth=0.8, zorder=0)
    ax.set_axisbelow(True)

    # Labels
    ax.set_xlabel("2021 winning margin (percentage points)", **AXIS_FONT)
    ax.set_ylabel("Namesake candidates filed for 2026", **AXIS_FONT)

    # Title block
    fig.text(0.07, 0.955, "Tamil Nadu 2026: where the namesakes cluster",
             **TITLE_FONT)
    fig.text(0.07, 0.925,
             "Tighter 2021 margins draw more namesake filings in 2026.",
             **SUBTITLE_FONT)
    fig.text(0.07, 0.905,
             "Each dot = one constituency.",
             **SUBTITLE_FONT)

    # Legend
    leg = ax.legend(loc="upper right", frameon=False, fontsize=10)
    for t in leg.get_texts():
        t.set_color(INK)

    # Footer — two lines so long URLs don't collide with the byline
    fig.text(0.07, 0.045,
             "Source: ECI Form 26 affidavits + Form 20 results",
             **FOOTER_FONT)
    fig.text(0.07, 0.025,
             "Dataset: github.com/ndranandraj/tn-2026-candidates-dataset · CC-BY-4.0",
             **FOOTER_FONT)
    fig.text(0.93, 0.025, "ndranandraj.com", ha="right", **FOOTER_FONT)

    # Sample watermark
    if sample:
        fig.text(0.5, 0.5, "SAMPLE · NOT FINAL",
                 ha="center", va="center",
                 fontsize=56, color=CORAL, alpha=0.12,
                 rotation=18, fontweight="bold")

    plt.subplots_adjust(left=0.11, right=0.95, top=0.86, bottom=0.14)
    fig.savefig(output, dpi=DPI, facecolor=BG)
    plt.close(fig)
    print(f"Wrote {output} ({output.stat().st_size // 1024} KB)")


# ---------- CLI --------------------------------------------------------

def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("input_csv", type=Path)
    ap.add_argument("output_png", type=Path)
    ap.add_argument("--sample", action="store_true",
                    help="Render a SAMPLE watermark (use before real data is wired up).")
    args = ap.parse_args(argv)

    if not args.input_csv.exists():
        print(f"Input not found: {args.input_csv}", file=sys.stderr)
        return 2

    agg = load_aggregate(args.input_csv)
    args.output_png.parent.mkdir(parents=True, exist_ok=True)
    render(agg, args.output_png, sample=args.sample)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
