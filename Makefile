# _*_ Makefile _*_

MD = $(wildcard *.md) $(wildcard */*.md)
MD_DEEP = $(wildcard */*.md)
DEP = $(wildcard *footer.txt) $(wildcard */footer.txt)
OUT = $(MD:.md=.html) more.html

all: $(OUT)

%.html : %.md $(DEP)
	awk -f add_footer.awk $< \
		| pandoc -s -o $@

more.html : more_header.md gen_toc.awk $(DEP) $(MD_DEEP)
	ls -lt */* \
		| awk -f gen_toc.awk \
		| cat more_header.md - footer.txt \
		| pandoc -s -o $@

clean:
	rm -rf $(OUT)

