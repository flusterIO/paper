from pathlib import Path

import numpy as np, matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate, optimize
from physics.data.constants import eilers as E

G = 6.67430e-11
Msun = 1.98847e30
kpc = 3.0856776e19
Gk = (
    G * Msun / kpc / 1e6
)  # G in kpc (km/s)^2 / Msun  (x1e... see below)  -> km^2/s^2 kpc / Msun
Gk = G * Msun / (kpc * 1e6)  # (km/s)^2 * kpc / Msun


# ---------- baryonic model: M_bar(<R) in Msun, R in kpc ----------
def disc_exp(R, S0, Rd):  # S0 in Msun/pc^2, thin-disc enclosed mass
    S0k = S0 * 1e6
    Mtot = 2 * np.pi * S0k * Rd**2
    x = R / Rd
    return Mtot * (1 - (1 + x) * np.exp(-x))


def disc_hole(R, S0, Rd, Rm):  # Sigma=S0 exp(-Rm/R-R/Rd)
    S0k = S0 * 1e6
    f = lambda r: 2 * np.pi * r * S0k * np.exp(-Rm / r - r / Rd)
    return integrate.quad(f, 1e-6, R)[0]


def bulge(R, rho0=98.4e9, r0=0.075, rcut=2.1, a=1.8):  # rho0 in Msun/kpc^3
    f = (
        lambda r: 4
        * np.pi
        * r**2
        * rho0
        / (1 + r / r0) ** a
        * np.exp(-((r / rcut) ** 2))
    )
    return integrate.quad(f, 1e-6, R)[0]


def M_raw(R):
    return (
        disc_exp(R, 896, 2.50)
        + disc_exp(R, 183, 3.02)
        + disc_hole(R, 53.1, 7.0, 4.0)
        + disc_hole(R, 2180, 1.5, 12.0)
        + bulge(R)
    )


R0 = 8.12
scale = 4.44e10 / M_raw(R0)
M_bar = lambda R: scale * M_raw(R)
M_tot_raw = M_raw(200.0)

R = E.radius_kpc
v = E.velocity_km_s
sig_stat = 0.5 * (E.velocity_error_lower_km_s + E.velocity_error_upper_km_s)
sig_sys = E.systematic_fraction * v
sig = np.hypot(sig_stat, sig_sys)
sig5 = np.hypot(sig, 0.05 * v)  # extra 5% floor on top

Menc = np.array([M_bar(r) for r in R])


def v_paper(M, Rk):  # exact paper expression, SI, tau=1 s
    Mk = M * Msun
    Rm = Rk * kpc
    return np.sqrt(G * Mk * (G * Mk + 2 * Rm**3)) / Rm**2 / 1e3


v_esc = np.sqrt(2 * Gk * Menc / R)  # sqrt(2GM/R)
v_pap = v_paper(Menc, R)
v_newt = np.sqrt(Gk * Menc / R)


def chi2(vm, s):
    return np.sum(((v - vm) / s) ** 2)


dof = len(R)
print(
    f"Model baryon total (raw, un-rescaled) M_bar(<200 kpc) = {M_tot_raw:.3e} Msun; rescale factor to 4.44e10 at 8.12 kpc = {scale:.3f}"
)
print(
    f"max |v_paper - sqrt(2GM/R)| = {np.max(np.abs(v_pap-v_esc)):.2e} km/s  (relativistic term is negligible)"
)
print()
print(
    f"{'R':>6} {'v_obs':>7} {'sig':>6} {'Menc':>9} {'v_paper':>8} {'v_Newt':>7} {'M_req':>9}"
)
Mreq = v**2 * R / (2 * Gk)
for i in range(dof):
    print(
        f"{R[i]:6.2f} {v[i]:7.2f} {sig[i]:6.2f} {Menc[i]:9.2e} {v_pap[i]:8.1f} {v_newt[i]:7.1f} {Mreq[i]:9.2e}"
    )
print()
for name, vm in [
    ("paper v_orbit (sqrt(2GM/R))", v_pap),
    ("Newtonian circular, baryons only", v_newt),
]:
    print(
        f"{name:36s} chi2 = {chi2(vm,sig):10.1f}  ({chi2(vm,sig)/dof:8.1f}/dof)   with extra 5% floor: {chi2(vm,sig5):8.1f} ({chi2(vm,sig5)/dof:6.1f}/dof)"
    )

# one-parameter fit: free overall mass scale s on the paper's formula
shape = np.sqrt(2 * Gk * Menc / R)
s_fit = np.sum(v * shape / sig**2) / np.sum(shape**2 / sig**2)
print(
    f"\nBest single scale on sqrt(2GM_enc/R): v -> {s_fit:.3f} x v  => mass x {s_fit**2:.3f}"
)
for lab, s in [("stat+sys", sig), ("with 5% floor", sig5)]:
    sf = np.sum(v * shape / s**2) / np.sum(shape**2 / s**2)
    print(
        f"  {lab:14s}: chi2_min = {chi2(sf*shape,s):8.1f} ({chi2(sf*shape,s)/(dof-1):6.1f}/dof), mass scale {sf**2:.2f}, implied M(<8.12) = {sf**2*4.44e10:.2e}"
    )
# shape only: ratio v(24.8)/v(5.3)
i5 = np.argmin(abs(R - 5.27))
i25 = np.argmin(abs(R - 24.82))
print(
    f"\nShape: observed v(24.82)/v(5.27) = {v[i25]/v[i5]:.3f};  model = {shape[i25]/shape[i5]:.3f}"
)
print(f"M_bar model(<24.82)/M_bar(<5.27) = {Menc[i25]/Menc[i5]:.2f}")
print(
    f"Required M_enc to match data: at 8.19 kpc {Mreq[6]:.2e}, at 24.82 kpc {Mreq[-1]:.2e} Msun"
)
print(
    f"Model total baryonic mass (raw) {M_tot_raw:.2e} Msun; required at 24.82 kpc exceeds it by x{Mreq[-1]/M_tot_raw:.2f} (x{Mreq[-1]/M_bar(24.82):.2f} vs rescaled model)"
)
np.savez(
    "rc_results.npz",
    R=R,
    v=v,
    sig=sig,
    Menc=Menc,
    v_pap=v_pap,
    v_newt=v_newt,
    Mreq=Mreq,
)

d = np.load("rc_results.npz")
R = d["R"]
v = d["v"]
sig = d["sig"]
vp = d["v_pap"]
vn = d["v_newt"]
Mreq = d["Mreq"]
Menc = d["Menc"]
fig, ax = plt.subplots(1, 2, figsize=(11, 4.2))
a = ax[0]
a.errorbar(R, v, yerr=sig, fmt="o", ms=3.5, color="k", label="Eilers et al. (2019)")
a.plot(
    R, vp, "-", color="tab:red", label=r"paper $v_{\rm orbit}=\sqrt{2GM_{\rm enc}/R}$"
)
a.plot(
    R,
    vn,
    "--",
    color="tab:blue",
    label=r"Newtonian $\sqrt{GM_{\rm enc}/R}$, baryons only",
)
a.set_xlabel("Galactocentric radius R [kpc]")
a.set_ylabel("velocity [km/s]")
a.set_ylim(80, 260)
a.legend(fontsize=8, loc="lower left")
a.set_title("Predicted vs observed velocity")
b = ax[1]
b.plot(
    R, Mreq / 1e10, "ko-", ms=3, label=r"enclosed mass required: $v_{\rm obs}^2R/2G$"
)
b.plot(
    R,
    Menc / 1e10,
    "-",
    color="tab:red",
    label=r"baryonic $M_{\rm enc}(<R)$ (rescaled to $4.44\times10^{10}$ at 8.12 kpc)",
)
b.axhline(
    7.5,
    color="gray",
    ls=":",
    label=r"un-rescaled model total baryons ($7.5\times10^{10}$)",
)
b.set_xlabel("Galactocentric radius R [kpc]")
b.set_ylabel(r"mass [$10^{10}\,M_\odot$]")
b.legend(fontsize=7.5, loc="upper left")
b.set_title("Mass needed vs baryons available")
plt.tight_layout()
plt.savefig(
    Path(__file__).parent.parent / "outputs" / "rotation_curve_plot.png", dpi=160
)
