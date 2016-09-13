SHELL=/bin/bash

DOCUMENT=thesis

document:
	xelatex ${DOCUMENT}.tex
	makeindex ${DOCUMENT}.nlo -s nomencl.ist -o ${DOCUMENT}.nls
	makeglossaries ${DOCUMENT}
	biber ${DOCUMENT}
	xelatex ${DOCUMENT}.tex

cover:
	pdftk gfx/PhDengelskMonster.pdf ${DOCUMENT}.pdf cat output RobertoDiRemigioPhDThesis.pdf

clean:
	rm -f *~ *.aux *.idx *.log *.bbl *.lol *.lof *.lot *.blg *-blx.bib *.out
	rm -f *.backup *.brf *.toc *.bcf *.run.xml texput.log
	rm -f *.tdo *.nlo *.nls *.ilg *.acn *.glo *.glsdefs *.ist
	rm -f *.acr *.alg *.glg *.gls
	rm -f FrontBackmatter/*.aux
	rm -f Chapters/*.aux
