from pathlib import Path
import numpy as np, matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams.update(
    {
        "font.size": 11,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "savefig.dpi": 200,
        "savefig.facecolor": "white",
    }
)
BLUE = "#1f4e79"
ORG = "#d9822b"
RED = "#b2262e"
GRY = "#666666"
OUT = Path(__file__).parent.parent / "outputs"
fig, ax = plt.subplots(1, 2, figsize=(11.2, 4.6))
a = ax[0]
for xs, ls in [(3.0, "-"), (1.5, "--")]:
    rs = 1.0
    Rs = xs
    L = np.sqrt(Rs**3 / rs)
    sst = np.sqrt(1 - Rs**2 / L**2)
    Ri = np.linspace(0, Rs, 300)
    s = np.sqrt(1 - (Ri / L) ** 2)
    N = (3 * sst - s) / 2
    Ro = np.linspace(Rs, 6, 300)
    No = np.sqrt(1 - rs / Ro)
    a.plot(
        Ri,
        N,
        color=RED,
        ls=ls,
        lw=2.4,
        label=(r"lapse $N$ inside" if xs == 3.0 else None),
    )
    a.plot(
        Ri,
        s,
        color=BLUE,
        ls=ls,
        lw=1.8,
        label=(r"slice foreshortening $\cos\theta=1/\gamma$" if xs == 3.0 else None),
    )
    a.plot(
        Ro,
        No,
        color=GRY,
        ls=ls,
        lw=2,
        label=("outside: $N=\\cos\\theta$" if xs == 3.0 else None),
    )
    a.text(
        Rs + 0.1,
        0.70 if xs == 3.0 else 0.43,
        rf"$R_*={xs}\,r_s$",
        fontsize=10,
        color=GRY,
    )
a.set_xlabel(r"$R/r_s$")
a.set_ylim(0, 1.05)
a.legend(frameon=False, fontsize=9, loc="lower right")
a.set_title("Inside matter, redshift outruns foreshortening", fontsize=11)
b = ax[1]
x = np.linspace(1.1252, 6, 500)
sst = np.sqrt(1 - 1 / x)
pc = (1 - sst) / (3 * sst - 1)
N0 = (3 * sst - 1) / 2
b.semilogy(x, pc, color=RED, lw=2.4, label=r"central pressure $p_c/\rho c^2$")
b.plot(x, N0, color=BLUE, lw=2.2, label=r"central lapse $N(0)$")
b.axvline(9 / 8, color=ORG, ls=":", lw=2)
b.text(
    9 / 8 + 0.08,
    1e2,
    r"$R_*=\frac{9}{8}r_s$" + "\n" + r"$\gamma_*=3,\ \theta_*=70.5^\circ$",
    color=ORG,
    fontsize=10,
)
b.set_xlabel(r"$R_*/r_s$")
b.set_ylim(1e-3, 1e3)
b.legend(frameon=False, fontsize=9, loc="lower right")
b.set_title("The Buchdahl bound: lapse at the centre hits zero", fontsize=11)
plt.tight_layout()
plt.savefig(OUT / "interior_lapse.png")
