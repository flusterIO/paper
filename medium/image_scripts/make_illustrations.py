"""Illustrations for the Medium article (not data plots; those live in physics.plot_generators.flow_of_space).

Run:  python make_illustrations.py   -> writes ../images/*.png
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mp
import numpy as np

OUT = Path(__file__).resolve().parent.parent / "images"
OUT.mkdir(parents=True, exist_ok=True)
NAVY, GOLD, TEAL, ORANGE, INK = "#0b1530", "#f2c14e", "#2ec4b6", "#ff7f51", "#e8ecf4"
rng = np.random.default_rng(7)


def hero():
    fig = plt.figure(figsize=(16, 7), facecolor=NAVY)
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 16); ax.set_ylim(0, 7); ax.axis("off"); ax.set_facecolor(NAVY)
    # perspective grid (flat absolute space)
    for x0 in np.linspace(-20, 36, 40):
        ax.plot([8, x0], [3.2, -1], color="#25365f", lw=0.8)
    for k in range(1, 14):
        yy = 3.2 - 4.2 * (k / 13) ** 1.7
        ax.plot([-1, 17], [yy, yy], color="#25365f", lw=0.8)
    # stars
    ax.scatter(rng.uniform(0, 16, 220), rng.uniform(3.3, 7, 220), s=rng.uniform(0.2, 3, 220), color="white", alpha=0.6)
    # clock
    cx, cy, r = 3.6, 4.0, 1.5
    ax.add_patch(mp.Circle((cx, cy), r, fill=False, lw=4, color=GOLD))
    for k in range(12):
        a = np.pi / 2 - k * np.pi / 6
        ax.plot([cx + 0.82 * r * np.cos(a), cx + 0.95 * r * np.cos(a)], [cy + 0.82 * r * np.sin(a), cy + 0.95 * r * np.sin(a)], color=GOLD, lw=2.5)
    ax.plot([cx, cx + 0.55 * r * np.cos(np.pi / 3)], [cy, cy + 0.55 * r * np.sin(np.pi / 3)], color=GOLD, lw=4, solid_capstyle="round")
    ax.plot([cx, cx + 0.85 * r * np.cos(-0.35)], [cy, cy + 0.85 * r * np.sin(-0.35)], color=GOLD, lw=2.5, solid_capstyle="round")
    # the clock dissolving into motion: streaks leaving its right side and rising into y
    for i in range(160):
        t0 = rng.uniform(-np.pi / 2, np.pi / 2)
        x0, y0 = cx + r * np.cos(t0), cy + r * np.sin(t0)
        L = rng.uniform(3, 11)
        slope = rng.uniform(0.02, 0.22)
        xs = np.linspace(x0, x0 + L, 60)
        ys = y0 + slope * (xs - x0) ** 1.3 / 3
        col = [GOLD, TEAL, INK][i % 3]
        for j in range(0, 59, 3):
            ax.plot(xs[j:j + 4], ys[j:j + 4], color=col, lw=rng.uniform(0.5, 1.8), alpha=0.9 * (1 - j / 60) ** 1.5)
    fig.savefig(OUT / "hero-time-as-motion.png", dpi=150, facecolor=NAVY)
    plt.close(fig)


def triangle():
    fig, ax = plt.subplots(figsize=(10, 6.2), facecolor="white")
    ax.set_xlim(-0.5, 10.5); ax.set_ylim(-1.1, 6.4); ax.axis("off"); ax.set_aspect("equal")
    A, B, C = np.array([0, 0]), np.array([8, 0]), np.array([8, 4.8])
    ax.add_patch(mp.Polygon([A, B, C], closed=True, facecolor="#eef5ff", edgecolor="none"))
    ax.plot(*zip(A, C), color="#0072B2", lw=4)
    ax.plot(*zip(A, B), color="#D55E00", lw=4)
    ax.plot(*zip(B, C), color="#009E73", lw=4)
    ax.add_patch(mp.Rectangle((7.6, 0), 0.4, 0.4, fill=False, lw=1.5, color="0.3"))
    ax.add_patch(mp.Arc(A, 2.4, 2.4, theta1=0, theta2=np.degrees(np.arctan2(4.8, 8)), lw=2, color="0.25"))
    ax.text(1.45, 0.38, r"$\psi$", fontsize=20, color="0.2")
    ax.text(3.4, 3.0, "absolute time  ×  c\n(the same for everyone)", fontsize=15, color="#0072B2", rotation=31, ha="center", va="center", weight="bold")
    ax.text(4.0, -0.6, "distance travelled through space", fontsize=15, color="#D55E00", ha="center", weight="bold")
    ax.text(8.25, 2.4, "your clock's\ntime  ×  c", fontsize=15, color="#009E73", va="center", weight="bold")
    ax.text(5.0, 6.0, r"(absolute time)$^2$ = (your clock's time)$^2$ + (distance)$^2$", fontsize=17, ha="center", color="0.15")
    ax.text(5.0, 5.4, r"sin $\psi$ = your speed ÷ the speed of light      cos $\psi$ = how fast your clock runs", fontsize=12.5, ha="center", color="0.35")
    fig.savefig(OUT / "diagram-pythagoras-of-time.png", dpi=170, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def apple(ax, x, y, s=0.35):
    ax.add_patch(mp.Circle((x, y), s, color="#c0392b", zorder=5))
    ax.plot([x, x + 0.05], [y + s * 0.9, y + s * 1.5], color="#5d4037", lw=3, zorder=6)
    ax.add_patch(mp.Ellipse((x + 0.22, y + s * 1.35), 0.32, 0.14, angle=25, color="#2e7d32", zorder=6))


def falling():
    fig, axs = plt.subplots(1, 2, figsize=(13, 6.2), facecolor="white")
    for ax in axs:
        ax.set_xlim(0, 6); ax.set_ylim(0, 6.2); ax.axis("off"); ax.set_aspect("equal")
    # left: the usual story
    ax = axs[0]
    ax.add_patch(mp.Rectangle((0, 0), 6, 1.2, color="#8d6e63")); ax.add_patch(mp.Rectangle((0, 1.2), 6, 0.18, color="#66bb6a"))
    apple(ax, 3, 4.4)
    ax.annotate("", xy=(3, 2.0), xytext=(3, 3.8), arrowprops=dict(arrowstyle="-|>", lw=4, color="#D55E00", mutation_scale=30))
    ax.text(3.35, 2.9, "pulled\ndown", fontsize=15, color="#D55E00", va="center")
    ax.text(3, 5.75, "The usual story", fontsize=18, ha="center", weight="bold", color="0.15")
    # right: co-expansion
    ax = axs[1]
    ax.add_patch(mp.Rectangle((0, 0), 6, 1.2, color="#8d6e63")); ax.add_patch(mp.Rectangle((0, 1.2), 6, 0.18, color="#66bb6a"))
    for k, yy in enumerate(np.linspace(1.75, 3.1, 4)):
        xs = np.linspace(0.2, 5.8, 100)
        ax.plot(xs, yy + 0.08 * np.sin(xs * 2 + k), color=TEAL, lw=1.6, alpha=0.35 + 0.15 * k)
    for xa in (0.9, 2.0, 4.0, 5.1):
        ax.annotate("", xy=(xa, 2.6), xytext=(xa, 1.5), arrowprops=dict(arrowstyle="-|>", lw=3, color="#009E73", mutation_scale=22))
    apple(ax, 3, 4.4)
    ax.text(3, 3.65, "holds still", fontsize=14, ha="center", color="0.3", style="italic")
    ax.text(3, 0.6, "the co-expanding ground\nrises to meet it", fontsize=13, ha="center", va="center", color="white", weight="bold")
    ax.text(3, 5.75, "Co-expansion", fontsize=18, ha="center", weight="bold", color="0.15")
    fig.savefig(OUT / "illustration-falling-vs-rising.png", dpi=160, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def tile_icon(ax, kind, cx, cy):
    if kind == "mercury":
        for a in np.linspace(0, 1.2, 5):
            t = np.linspace(0, 2 * np.pi, 200)
            x, y = 0.55 * np.cos(t), 0.32 * np.sin(t)
            ax.plot(cx + x * np.cos(a) - y * np.sin(a) + 0.15 * np.cos(a), cy + x * np.sin(a) + y * np.cos(a) + 0.15 * np.sin(a), color="#0072B2", lw=1, alpha=0.5)
        ax.add_patch(mp.Circle((cx, cy), 0.12, color=GOLD))
    elif kind == "light":
        ax.add_patch(mp.Circle((cx, cy - 0.15), 0.28, color=GOLD))
        x = np.linspace(-0.85, 0.85, 120)
        ax.plot(cx + x, cy + 0.35 - 0.25 * (1 + np.tanh(4 * x)) / 2 - 0.25 * x * (x > 0), color=ORANGE, lw=2.5)
        ax.plot([cx - 0.85, cx + 0.85], [cy + 0.35, cy + 0.35], color=ORANGE, lw=1, ls=":", alpha=0.6)
    elif kind == "radar":
        ax.add_patch(mp.Circle((cx, cy), 0.25, color=GOLD))
        ax.plot([cx - 0.85, cx + 0.85], [cy + 0.45, cy + 0.38], color=TEAL, lw=2, ls="--")
        ax.add_patch(mp.Rectangle((cx + 0.7, cy + 0.3), 0.2, 0.15, color="0.4"))
    elif kind == "clock":
        ax.add_patch(mp.Circle((cx, cy), 0.42, fill=False, lw=2.5, color="#0072B2"))
        ax.plot([cx, cx], [cy, cy + 0.3], color="#0072B2", lw=2.5); ax.plot([cx, cx + 0.22], [cy, cy - 0.05], color="#0072B2", lw=2.5)
    elif kind == "gyro":
        ax.add_patch(mp.Circle((cx, cy), 0.25, color="#9fa8da"))
        ax.add_patch(mp.Ellipse((cx, cy), 1.0, 0.35, fill=False, lw=2, color="#3949ab"))
        ax.add_patch(mp.Ellipse((cx, cy), 0.35, 1.0, fill=False, lw=2, color="#3949ab", angle=20))
    elif kind == "pulsar":
        for rr, a in ((0.25, 0.3), (0.6, 2.0)):
            ax.add_patch(mp.Circle((cx, cy), rr, fill=False, lw=1, color="0.5", ls=":"))
            ax.add_patch(mp.Circle((cx + rr * np.cos(a), cy + rr * np.sin(a)), 0.07, color="#bdbdbd"))
        ax.add_patch(mp.Circle((cx, cy), 0.08, color=TEAL)); ax.plot([cx - 0.35, cx + 0.35], [cy + 0.35, cy - 0.35], color=TEAL, lw=1.5)
    elif kind == "waves":
        x = np.linspace(-0.8, 0.8, 200); ax.plot(cx + x, cy + 0.3 * np.sin(14 * x) * np.exp(-((x + 0.1) ** 2) / 0.25), color="#7b1fa2", lw=2.5)
    elif kind == "shadow":
        ax.add_patch(mp.Circle((cx, cy), 0.5, color=ORANGE, alpha=0.9)); ax.add_patch(mp.Circle((cx, cy), 0.33, color="#111111"))


def tests():
    items = [("mercury", "Mercury's orbit", "43″ per century"), ("light", "Starlight bending", "1.75″ at the Sun"),
             ("radar", "Radar echo delay", "Cassini, 1 in 100,000"), ("clock", "Clocks & gravity", "GPS, Galileo satellites"),
             ("gyro", "Frame dragging", "Gravity Probe B"), ("pulsar", "Neutron stars fall", "triple pulsar, 1 in a million"),
             ("waves", "Gravitational waves", "travel at light speed"), ("shadow", "Black-hole shadows", "same size as Einstein's")]
    fig, ax = plt.subplots(figsize=(14, 7.2), facecolor="white"); ax.set_xlim(0, 4); ax.set_ylim(0, 2.25); ax.axis("off")
    for k, (kind, title, sub) in enumerate(items):
        i, j = k % 4, 1 - k // 4
        x0, y0 = i + 0.05, j + 0.05
        ax.add_patch(mp.FancyBboxPatch((x0, y0), 0.9, 0.9, boxstyle="round,pad=0.02,rounding_size=0.06", facecolor="#f5f7fb", edgecolor="#d5dbe8"))
        tile_icon(ax, kind, x0 + 0.45, y0 + 0.6) if False else None
        sub_ax = ax.inset_axes([x0 + 0.2, y0 + 0.36, 0.5, 0.5], transform=ax.transData); sub_ax.set_xlim(-1, 1); sub_ax.set_ylim(-1, 1); sub_ax.axis("off"); sub_ax.set_aspect("equal")
        tile_icon(sub_ax, kind, 0, 0)
        ax.text(x0 + 0.45, y0 + 0.24, title, ha="center", fontsize=13, weight="bold", color="0.15")
        ax.text(x0 + 0.45, y0 + 0.12, sub, ha="center", fontsize=10.5, color="0.4")
        ax.add_patch(mp.Circle((x0 + 0.8, y0 + 0.8), 0.07, color="#2e7d32")); ax.text(x0 + 0.8, y0 + 0.795, "✓", ha="center", va="center", fontsize=14, color="white", weight="bold")
    ax.text(2, 2.17, "Every test of Einstein's gravity, passed", ha="center", fontsize=19, weight="bold", color="0.15")
    fig.savefig(OUT / "infographic-classic-tests.png", dpi=160, bbox_inches="tight", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    hero(); triangle(); falling(); tests()
    print("wrote", sorted(p.name for p in OUT.glob("*.png")))
