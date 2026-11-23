from pathlib import Path
import glob

outputDir = Path(__file__).parent / "diagrams" / "outputs"

mainDir = Path(__file__).parent


def cleanInputFolder(d: Path):
    main_files = [
        f
        for f in d.glob("main.*")
        if not f.__str__().endswith(".pdf")
        and not f.__str__().endswith(".tex")
        and not f.__str__().endswith(".png")
    ]
    for f in d.glob("main-*"):
        main_files.append(f)
    for m in main_files:
        print(f"Cleaning {m.__str__()}")
        m.unlink()


cleanInputFolder(Path(__file__).parent / "iop")

files = [
    f
    for f in outputDir.glob("*")
    if not f.__str__().endswith(".pdf")
    and not f.__str__().endswith(".eps")
    and not f.__str__().endswith("simple_triangle.png")
]

for f in files:
    Path(f).unlink()


main_files = [
    f
    for f in mainDir.glob("main.*")
    if not f.__str__().endswith(".pdf")
    and not f.__str__().endswith(".tex")
    and not f.__str__().endswith(".bbl")
    and not f.__str__().endswith(".png")
]


for f in main_files:
    Path(f).unlink()


final_files = [
    f
    for f in mainDir.glob("final.*")
    if not f.__str__().endswith(".pdf")
    and not f.__str__().endswith(".tex")
    and not f.__str__().endswith(".bbl")
    and not f.__str__().endswith(".bib")
    and not f.__str__().endswith(".png")
]


for f in final_files:
    Path(f).unlink()


pdflatex_files = [f for f in mainDir.glob("pdflatex*")]


for f in pdflatex_files:
    Path(f).unlink()
