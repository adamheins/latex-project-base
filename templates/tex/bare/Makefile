PDF_FILE=out.pdf
TEX_FILE=content.tex
FLAGS=--bibtex-cmd=biber --latex-cmd pdflatex


$(PDF_FILE): $(TEX_FILE) clean
# Leading dash causes processing to proceed even if errors occur.
	@latexrun $(FLAGS) $(TEX_FILE) -o $(PDF_FILE)
# latex.out is where latexrun puts output files.
	@-rm -rf latex.out

.PHONY: clean
clean:
# Remove the old PDF.
	@-rm -f $(PDF_FILE)
	@latexrun --clean-all
