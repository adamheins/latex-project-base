PDF_FILE=output.pdf

TEX_BASENAME=template
TEX_DIR=tex
TEX_FILE=$(TEX_DIR)/$(TEX_BASENAME).tex

# -cd goes into the tex directory
# -bibtex builds the bbl files from .bib
# -f forces continuation even if errors occur
COMMON_FLAGS=-cd -bibtex -f

$(PDF_FILE): $(TEX_FILE) clean
# Leading dash causes processing to proceed even if errors occur.
	-latexmk $(COMMON_FLAGS) -pdf -pdflatex="pdflatex -interaction=nonstopmode" $(TEX_FILE)
# Latex automatically named the PDF file the same as the tex file, so we
# rename it here.
	@-mv $(TEX_BASENAME).pdf $(PDF_FILE)
# Running latexmk with the -c flag cleans up all of the extra files like
# .log, .aux, etc, but not .pdf, .dvi, or .eps.
	@latexmk $(COMMON_FLAGS) -c -silent

.PHONY: clean
clean:
# Remove the old PDF.
	@-rm -f $(PDF_FILE)
# Using -C is the same as -c but also removes PDF, DVI, and postscript files.
# Since we've renamed the output PDF, we must remove it manually.
	@latexmk $(COMMON_FLAGS) -C -silent
