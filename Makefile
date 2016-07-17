SHELL=/bin/bash

DOCUMENT=RobertoDiRemigioPhDThesis

document:
	xelatex ${DOCUMENT}.tex
	biber ${DOCUMENT}
	xelatex ${DOCUMENT}.tex

clean:
	rm -f *~ ${DOCUMENT}.aux ${DOCUMENT}.idx ${DOCUMENT}.log ${DOCUMENT}.bbl ${DOCUMENT}.lol ${DOCUMENT}.lof ${DOCUMENT}.lot ${DOCUMENT}.blg *-blx.bib ${DOCUMENT}.out *.backup ${DOCUMENT}.brf ${DOCUMENT}.toc  ${DOCUMENT}.bcf ${DOCUMENT}.run.xml texput.log
