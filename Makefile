# _*_ Makefile _*_

MD = $(wildcard *.md) $(wildcard */*.md)
MD_DEEP = $(wildcard */*.md)
THEME = themes/gruvbox/gruvbox-light.css
DEP = $(wildcard *footer.txt) $(wildcard */footer.txt) $(THEME)
OUT = $(MD:.md=.html) more.html

all: $(OUT)

%.html : %.md $(DEP)
	echo $< $@
	awk -f add_footer.awk $< \
		| pandoc -s -o $@ --css=$$(realpath --relative-to=$$(dirname $@) $(THEME))

more.html : more_header.md gen_toc.awk $(DEP) $(MD_DEEP)
	{ ls -ltd */*.md ; ls -ltd README.md ; } \
		| awk -f gen_toc.awk \
		| cat more_header.md - footer.txt \
		| pandoc -s -o $@ --css=$$(realpath --relative-to=$$(dirname $@) $(THEME))

clean:
	rm -rf $(OUT)

