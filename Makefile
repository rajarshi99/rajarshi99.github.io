# _*_ Makefile _*_

MD = $(wildcard *.md)
OUT = $(MD:.md=.html)

all: $(OUT)

%.html : %.md footer.md
	cat $< footer.md | pandoc -o $@

clean:
	rm -rf $(OUT)

