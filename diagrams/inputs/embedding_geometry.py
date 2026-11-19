import numpy as np, matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

plt.rcParams.update(
    {
        "font.size": 10,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "pdf.fonttype": 42,
        "savefig.facecolor": "white",
    }
)
OUT = Path(__file__).parent.parent / "outputs"
BLUE = "#1f4e79"
ORG = "#d9822b"
RED = "#b2262e"
GRY = "#666666"

# ---- Fig 2: embedding geometries (star: cap + paraboloid ; critical density) ----
fig, ax = plt.subplots(1, 2, figsize=(10.5, 4.2))
a = ax[0]
rs = 1.0
Rs = 3.0
L = np.sqrt(Rs**3 / rs)
Rin = np.linspace(0, Rs, 300)
yin = L - L * np.sqrt(1 - (Rin / L) ** 2)
Rout = np.linspace(Rs, 8, 400)
yout = yin[-1] + 2 * np.sqrt(rs * (Rout - rs)) - 2 * np.sqrt(rs * (Rs - rs))
a.plot(Rin, yin, color=RED, lw=2.4, label=r"interior: spherical cap, $\beta^2=R^2/L^2$")
a.plot(Rout, yout, color=BLUE, lw=2.4, label=r"exterior: paraboloid, $\beta^2=r_s/R$")
a.plot([Rs], [yin[-1]], "ko", ms=4)
a.text(Rs + 0.15, yin[-1] - 0.5, r"surface $R_*=3r_s$", fontsize=9)
a.set_xlabel(r"$R/r_s$")
a.set_ylabel(r"$y/r_s$")
a.legend(frameon=False, loc="upper left", fontsize=8.5)
a.set_title("(a) Uniform-density body", fontsize=10)
b = ax[1]
Rc = np.linspace(0, 1, 400)
yc = 1 - np.sqrt(1 - Rc**2)
b.plot(Rc, yc, color=ORG, lw=2.4)
b.plot([1], [1], "ko", ms=4)
b.annotate(
    r"$R=c/H$: vertical tangent, $\beta=1$",
    (1, 1),
    (0.12, 0.80),
    arrowprops=dict(arrowstyle="->", color=GRY),
    fontsize=9,
)
b.text(0.03, 0.42, r"critical density, $\beta=HR/c$", fontsize=9)
b.set_xlabel(r"$R\,/\,(c/H)$")
b.set_ylabel(r"$y\,/\,(c/H)$")
b.set_aspect("equal")
b.set_title("(b) Critical-density universe", fontsize=10)
plt.tight_layout()
plt.savefig(OUT / "embedding_geometries.eps")
plt.close()

# ---- Fig 3: Flamm profile, tilt, lapse ----
fig, ax = plt.subplots(1, 2, figsize=(10.5, 4.2))
a = ax[0]
Rr = np.linspace(1, 7, 400)
y = 2 * np.sqrt(Rr - 1)
a.plot(Rr, y, color=BLUE, lw=2.4)
a.plot(Rr, -y, color=BLUE, lw=2.4, ls="--", alpha=0.45)
R0 = 2.5
y0 = 2 * np.sqrt(R0 - 1)
sl = 1 / np.sqrt(R0 - 1)
xs = np.array([R0 - 0.9, R0 + 0.9])
a.plot(xs, y0 + sl * (xs - R0), color=ORG, lw=1.6)
a.plot([R0], [y0], "o", color=RED, ms=4)
a.annotate(
    r"$\sin\theta=\beta,\ \cos\theta=N=1/\gamma$",
    (R0, y0),
    (3.6, 0.4),
    arrowprops=dict(arrowstyle="->", color=GRY),
    fontsize=9,
)
a.set_xlabel(r"$R/r_s$")
a.set_ylabel(r"$y/r_s$")
a.set_xlim(0.8, 7)
a.set_aspect("equal")
a.set_title(r"(a) Exterior profile $y=2\sqrt{r_s(R-r_s)}$", fontsize=10)
b = ax[1]
R2 = np.linspace(1.001, 10, 500)
b.plot(R2, np.sqrt(1 / R2), color=ORG, lw=2.2, label=r"$\beta=\sin\theta=\sqrt{r_s/R}$")
b.plot(R2, np.sqrt(1 - 1 / R2), color=RED, lw=2.2, label=r"$N=\cos\theta=1/\gamma$")
b.set_xlabel(r"$R/r_s$")
b.legend(frameon=False)
b.set_ylim(0, 1.05)
b.set_title("(b) Flow speed and lapse", fontsize=10)
plt.tight_layout()
plt.savefig(OUT / "lapse_tilt.eps")
plt.close()

# ---- Fig 4: interior lapse and Buchdahl ----
fig, ax = plt.subplots(1, 2, figsize=(10.5, 4.4))
a = ax[0]
for xs_, ls in [(3.0, "-"), (1.5, "--")]:
    rs = 1.0
    Rs = xs_
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
        lw=2.2,
        label=(r"lapse $N$ (interior)" if xs_ == 3.0 else None),
    )
    a.plot(
        Ri,
        s,
        color=BLUE,
        ls=ls,
        lw=1.7,
        label=(r"$\cos\theta=1/\gamma$ (interior)" if xs_ == 3.0 else None),
    )
    a.plot(
        Ro,
        No,
        color=GRY,
        ls=ls,
        lw=1.8,
        label=(r"exterior $N=\cos\theta$" if xs_ == 3.0 else None),
    )
a.text(3.1, 0.70, r"$R_*=3\,r_s$ (solid)", fontsize=8.5, color=GRY)
a.text(1.55, 0.43, r"$R_*=1.5\,r_s$ (dashed)", fontsize=8.5, color=GRY)
a.set_xlabel(r"$R/r_s$")
a.set_ylim(0, 1.05)
a.legend(frameon=False, fontsize=8.5, loc="lower right")
a.set_title("(a) Inside matter the lapse departs from $\\cos\\theta$", fontsize=10)
b = ax[1]
x = np.linspace(1.1252, 6, 500)
sst = np.sqrt(1 - 1 / x)
pc = (1 - sst) / (3 * sst - 1)
N0 = (3 * sst - 1) / 2
b.semilogy(x, pc, color=RED, lw=2.2, label=r"central pressure $p_c/\rho c^2$")
b.plot(x, N0, color=BLUE, lw=2.0, label=r"central lapse $N(0)$")
b.axvline(9 / 8, color=ORG, ls=":", lw=2)
b.text(
    9 / 8 + 0.08,
    1e2,
    r"$R_*=\frac{9}{8}r_s$" + "\n" + r"$\gamma_*=3,\ \theta_*=70.5^\circ$",
    color=ORG,
    fontsize=9,
)
b.set_xlabel(r"$R_*/r_s$")
b.set_ylim(1e-3, 1e3)
b.legend(frameon=False, fontsize=8.5, loc="lower right")
b.set_title("(b) Buchdahl bound", fontsize=10)
plt.tight_layout()
plt.savefig(OUT / "interior_lapse.eps")
plt.close()

# ---- Fig 5: the two flows ----
G = 6.67430e-11
c = 299792458.0
Msun = 1.98847e30
kpc = 3.0856776e19
Mpc = 3.0856776e22
H = 70e3 / Mpc
M = 6e10 * Msun
Rm = np.logspace(np.log10(0.5 * kpc), np.log10(c / H * 2), 600)
bN = np.sqrt(2 * G * M / (c**2 * Rm))
bH = H * Rm / c
fig, a = plt.subplots(figsize=(6.6, 4.2))
a.loglog(
    Rm / kpc,
    bN,
    color=RED,
    lw=2,
    label=r"infall $\beta_N=\sqrt{2GM/c^2R}$, $M=6\times10^{10}M_\odot$",
)
a.loglog(Rm / kpc, bH, color=BLUE, lw=2, label=r"Hubble flow $\beta_H=HR/c$, $H_0=70$")
a.axhline(1, color=GRY, ls=":")
a.axvline(c / H / kpc, color=GRY, ls=":")
a.text(c / H / kpc * 0.9, 1.4, r"$R_H=c/H$", ha="right", color=GRY, fontsize=9)
Rzg = (2 * G * M / c**2 * c**2 / H**2) ** (1 / 3)
a.plot([Rzg / kpc], [np.sqrt(2 * G * M / (c**2 * Rzg))], "ko", ms=4)
a.text(Rzg / kpc * 1.15, np.sqrt(2 * G * M / (c**2 * Rzg)) * 1.3, "equal", fontsize=9)
a.set_xlabel("R [kpc]")
a.set_ylabel(r"flow speed $\beta=v/c$")
a.set_ylim(1e-9, 3)
a.legend(frameon=False, loc="lower right", fontsize=8)
plt.tight_layout()
plt.savefig(OUT / "flows.eps")
plt.close()

# ---- Fig 6: frame dragging: flow v_s in equatorial plane, vorticity (dipole) in meridional plane ----
fig, ax = plt.subplots(1, 2, figsize=(10.5, 4.6))
a = ax[0]
g = np.linspace(-4, 4, 17)
X, Y = np.meshgrid(g, g)
Rr = np.hypot(X, Y)
m = Rr > 1.0
VX = -Y / Rr**3
VY = X / Rr**3
sp = np.hypot(VX, VY)
a.quiver(
    X[m],
    Y[m],
    (VX / sp)[m],
    (VY / sp)[m],
    np.log10(sp[m]),
    cmap="viridis",
    pivot="mid",
    scale=22,
    width=0.006,
)
a.add_patch(plt.Circle((0, 0), 1.0, color="#cccccc"))
a.set_aspect("equal")
a.set_xlim(-4.3, 4.3)
a.set_ylim(-4.3, 4.3)
a.set_xlabel(r"$x/R_*$")
a.set_ylabel(r"$y/R_*$")
a.set_title(
    r"(a) Equatorial plane: flow $\mathbf{v}_s=\omega\,\hat{z}\times\mathbf{x}$, $\omega\propto R^{-3}$",
    fontsize=10,
)
b = ax[1]
xg = np.linspace(-4, 4, 300)
zg = np.linspace(-4, 4, 300)
XX, ZZ = np.meshgrid(xg, zg)
RR = np.hypot(XX, ZZ)
Fx = 3 * XX * ZZ / RR**5
Fz = (3 * ZZ**2 - RR**2) / RR**5
mask = RR < 1.0
Fx = np.ma.array(Fx, mask=mask)
Fz = np.ma.array(Fz, mask=mask)
b.streamplot(
    XX,
    ZZ,
    Fx,
    Fz,
    color=np.log10(np.hypot(Fx, Fz) + 1e-12),
    cmap="viridis",
    density=1.4,
    linewidth=1.0,
    arrowsize=0.9,
)
b.add_patch(plt.Circle((0, 0), 1.0, color="#cccccc"))
b.annotate(
    "",
    xy=(0, 0.8),
    xytext=(0, -0.8),
    arrowprops=dict(arrowstyle="->", color="k", lw=1.5),
)
b.text(0.08, 0.15, r"$\mathbf{J}$", fontsize=11)
b.set_aspect("equal")
b.set_xlim(-4, 4)
b.set_ylim(-4, 4)
b.set_xlabel(r"$x/R_*$")
b.set_ylabel(r"$z/R_*$")
b.set_title(
    r"(b) Meridional plane: vorticity $\nabla\times\mathbf{v}_s$ (dipole)", fontsize=10
)
plt.tight_layout()
plt.savefig(OUT / "frame_dragging.eps")
plt.close()
print("figures done")
