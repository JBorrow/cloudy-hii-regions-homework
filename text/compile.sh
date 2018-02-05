rm -rf compiled

mkdir compiled

xelatex -output-directory="compiled" text.tex

bibtex compiled/text

xelatex -output-directory="compiled" text.tex
xelatex -output-directory="compiled" text.tex

