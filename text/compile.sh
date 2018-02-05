rm -rf compiled

mkdir compiled

pdflatex -output-directory="compiled" text.tex

cd compiled
bibtex text

cd ..

pdflatex -output-directory="compiled" text.tex
pdflatex -output-directory="compiled" text.tex

