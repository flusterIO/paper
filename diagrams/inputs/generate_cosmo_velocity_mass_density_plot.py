from physics.plot_generators.cosmological_velocity_mass_density import (
    plotCosmologicalVelocityMassDensity,
)
from pathlib import Path


if __name__ == "__main__":
    fig, ax = plotCosmologicalVelocityMassDensity()
    p = (
        Path(__file__).parent.parent
        / "outputs"
        / "cosmo_velocity_mass_density_plot.png"
    )
    fig.savefig(p)
