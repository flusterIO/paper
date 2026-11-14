from pathlib import Path

from physics.plot_generators.observational.orbital_velocity import plotOrbitalVelocity


if __name__ == "__main__":
    fig, ax = plotOrbitalVelocity()
    p = Path(__file__).parent.parent / "outputs" / "eilers_observation.png"
    fig.savefig(p)
