
build_dilating_planes:
	cd {{justfile_directory()}}/diagrams/inputs; sudo pdflatex -output-directory=../outputs ./dilating_planes.tex
	pdftops -eps ./diagrams/outputs/dilating_planes.pdf ./diagrams/outputs/dilating_planes.eps


build_trig_derivation:
	cd {{justfile_directory()}}/diagrams/inputs; sudo pdflatex -output-directory=../outputs ./trig_orbital_velocity_derivation.tex
	pdftops -eps ./diagrams/outputs/trig_orbital_velocity_derivation.pdf ./diagrams/outputs/trig_orbital_velocity_derivation.eps

clean_diagram_output:
	/opt/anaconda3/envs/jupyter/bin/python {{justfile_directory()}}/clean.py

build_diagrams: build_dilating_planes build_trig_derivation
	/opt/anaconda3/envs/jupyter/bin/python {{justfile_directory()}}/diagrams/inputs/generate_omega_mass_density_plot.py
	magick diagrams/outputs/omega_mass_density.png diagrams/outputs/omega_mass_density.eps
	/opt/anaconda3/envs/jupyter/bin/python {{justfile_directory()}}/diagrams/inputs/generate_eilers_plot.py
	magick diagrams/outputs/eilers_observation.png diagrams/outputs/eilers_observation.eps

build_main:
	sudo pdflatex ./main.tex
	bibtex ./main
	sudo pdflatex ./main.tex
	sudo pdflatex ./main.tex

build: build_diagrams build_main clean_diagram_output
