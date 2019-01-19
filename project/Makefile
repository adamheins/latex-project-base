PDF_FILE=out.pdf

TEX_BASENAME=template
TEX_DIR=tex
TEX_FILE=$(TEX_DIR)/$(TEX_BASENAME).tex


$(PDF_FILE): $(TEX_FILE) clean
# Leading dash causes processing to proceed even if errors occur.
	@latexrun $(TEX_FILE) -o $(PDF_FILE)
	@-rm -rf latex.out

.PHONY: clean
clean:
# Remove the old PDF.
	@-rm -f $(PDF_FILE)
	@latexrun --clean-all
