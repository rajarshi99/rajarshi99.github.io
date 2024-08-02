# _*_ Makefile _*_

MD = $(wildcard *.md)
OUT = $(MD:.md=.html)

all: $(OUT)

%.html : %.md
	pandoc $< -o $@

clean:
	echo $(OUT)

