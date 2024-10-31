.PHONY: clean cpr.pdf
cpr.pdf:
	pdflatex cpr.tex
	biber cpr
	pdflatex cpr.tex
	pdflatex cpr.tex
clean:
	@-rm *aux *log *pdf *xml *bcf *blg *lot *bbl
