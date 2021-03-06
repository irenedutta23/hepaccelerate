#adapted from https://github.com/mattpitkin/psrqpy/blob/master/paper/Makefile
default: pdf

MDFILE=paper.md
BIBFILE=paper.bib
LATEXFILE=paper.tex

# some variables for the paper
REPOSITORY=https://github.com/hepaccelerate/hepaccelerate
ARCHIVE=http://dx.doi.org/10.5281/zenodo.1175303
REVIEW=https://github.com/openjournals/joss-reviews/issues/XYZ
ARCHIVEDOI=http://dx.doi.org/10.5281/zenodo.1175303
FORMATTEDDOI=10.21105/joss.00538
YEAR=2018
TITLE="hepaccelerate: Processing Columnar Collider Data with GPU-Accelerated Kernels"
AUTHOR="Joosep Pata"
ISSUE=22
VOLUME=3
PAGE=538
JOURNALNAME="Journal of Open Source Software"
PUBLISHED="???"
SUBMITTED="???"
PAPERURL=https://www.theoj.org/joss-papers/joss.00538/10.21105.joss.00538.pdf

latex: $(MDFILE) $(BIBFILE)
	# get JOSS template
	curl https://raw.githubusercontent.com/openjournals/whedon/master/resources/latex.template > latex.template
	# get JOSS logo
	curl https://raw.githubusercontent.com/openjournals/whedon/master/resources/joss/logo.png > joss-logo.png
	# use pandoc and pandoc-citeproc to create LaTeX source
	pandoc \
	    --filter pandoc-citeproc \
	    --bibliography=$(BIBFILE) \
	    -V repository="$(REPOSITORY)" \
	    -V journal_name=$(JOURNALNAME) \
	    -V paper_url="$(PAPERURL)" \
	    -V archive_doi="$(ARCHIVEDOI)" \
	    -V review_issue_url="$(REVIEW)" \
	    -V formatted_doi="$(FORMATTEDDOI)" \
	    -V logo_path="joss-logo.png" \
	    -V year="$(YEAR)" \
	    -V paper_title=$(TITLE) \
	    -V citation_author=$(AUTHOR) \
	    -V issue="$(ISSUE)" \
	    -V volume="$(VOLUME)" \
	    -V page="$(PAGE)" \
	    -V submitted=$(SUBMITTED) \
	    -V published=$(PUBLISHED) \
	    -V graphics="true" \
	    -V papersize=a4paper \
	    -V geometry:margin=1in \
	    -t latex \
	    -s $(MDFILE) \
	    -o $(LATEXFILE) \
	    --from markdown+autolink_bare_uris
#	    --template latex.template


simplepdf:
	pandoc --filter pandoc-citeproc --bibliography=$(BIBFILE) $(MDFILE) -o paper.pdf

pdf: latex
	pdflatex paper.tex
	pdflatex paper.tex

clean:
	rm paper.bcf paper.aux paper.log paper.out paper.run.xml

clean_downloads:
	rm latex.template joss-logo.png
