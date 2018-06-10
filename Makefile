PDF_FILE=output.pdf

TEX_BASENAME=template
TEX_DIR=tex
TEX_FILE=$(TEX_DIR)/$(TEX_BASENAME).tex

COMMON_FLAGS=-bibtex -cd

$(PDF_FILE): $(TEX_FILE) clean
	latexmk $(COMMON_FLAGS) -pdf -pdflatex="pdflatex -interaction=nonstopmode" -use-make $(TEX_FILE)
	@mv $(TEX_BASENAME).pdf $(PDF_FILE)
	@latexmk $(COMMON_FLAGS) -c -silent $(TEX_FILE)

.PHONY: clean
clean:
	@rm -f $(PDF_FILE)
	@latexmk $(COMMON_FLAGS) -C -silent $(TEX_FILE)
