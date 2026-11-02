from physics.plot_generators.omega_mass_density import plot, outliers
from pathlib import Path


def main():
    df, fig, ax = plot(drop_rows=outliers)
    outputPath = Path(__file__).parent.parent / "outputs" / "omega_mass_density.png"
    fig.savefig(outputPath)
    print("Figure saved...")


if __name__ == "__main__":
    main()
