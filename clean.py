from pathlib import Path
import glob

outputDir = Path(__file__).parent / "diagrams" / "outputs"

mainDir = Path(__file__).parent

files = [
    f
    for f in outputDir.glob("*")
    if not f.__str__().endswith(".pdf") and not f.__str__().endswith(".eps")
]

for f in files:
    Path(f).unlink()


main_files = [
    f
    for f in mainDir.glob("main.*")
    if not f.__str__().endswith(".pdf")
    and not f.__str__().endswith(".tex")
    and not f.__str__().endswith(".bbl")
]


for f in main_files:
    Path(f).unlink()


pdflatex_files = [f for f in mainDir.glob("pdflatex*")]


for f in pdflatex_files:
    Path(f).unlink()
