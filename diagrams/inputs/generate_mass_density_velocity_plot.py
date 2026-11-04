from pathlib import Path

from physics.plot_generators.mass_density_derived_velocity import (
    plotMassDensityDerivedVelocity,
)


if __name__ == "__main__":
    fig, ax = plotMassDensityDerivedVelocity()
    p = Path(__file__).parent.parent / "outputs" / "mass_density_velocity_plot.png"
    fig.savefig(p)
