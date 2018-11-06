PDF_FILE=output.pdf

TEX_BASENAME=template
TEX_DIR=tex
TEX_FILE=$(TEX_DIR)/$(TEX_BASENAME).tex

# Here we may want to use -f as well to force processing in the presence of
# nomimal errors like duplicate bibtex entries.
COMMON_FLAGS=-cd -bibtex

$(PDF_FILE): $(TEX_FILE) clean
	latexmk $(COMMON_FLAGS) -pdf -pdflatex="pdflatex -interaction=nonstopmode" $(TEX_FILE)
	# Latex automatically named the PDF file the same as the tex file, so we
	# rename it here.
	@mv $(TEX_BASENAME).pdf $(PDF_FILE)
	# Running latexmk with the -c flag cleans up all of the extra files like
	# .log, .aux, etc, but not .pdf, .dvi, or .eps.
	@latexmk $(COMMON_FLAGS) -c -silent $(TEX_FILE)

.PHONY: clean
clean:
	# Make a backup of current PDF (overwrites any existing backup).
	@mv $(PDF_FILE) $(PDF_FILE).back
	# Using -C is the same as -c but also removes PDF, DVI, and postscript files.
	# Since we've renamed the output PDF, we must remove it manually.
	@latexmk $(COMMON_FLAGS) -C -silent $(TEX_FILE)
