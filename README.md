# About my website

My [website](https://rajarshi99.github.io/)
is hosted by GitHub.
To do so I had to create a repository
with the name `rajarshi99.github.io`
and the rest was pretty easy.
If your github username is xyz
then you would need to create
the repository `xyz.github.io`.

For easy editing I write the content in markdown
and then I run a custom `Makefile`
using the `make` command.
I use the `pandoc` program
to generate the `.html` pages
from the `.md files`.

## What is `footer.txt`?

The `Makefile` concatenates `footer.txt`
to each of the files with the extension `.md`
and then uses the `pandoc` program
to generate the required web pages.

## How do I generate the table of contents?

I generate a table of contents
for all the markdown files
using my script `gen_toc.awk`
on the output of the `ls` command,
which lists directory contents.
```Makefile
more.html : more_header.md gen_toc.awk $(DEP) $(MD_DEEP)
	ls -lt */* \
		| awk -f gen_toc.awk \
		| cat more_header.md - footer.txt \
		| pandoc -s -o $@
```
This is can be seen on the site called
[more...](https://rajarshi99.github.io/more.html)

## What joy is this for?

I come here for command line jugglery.
Showcasing articles is a by-product. ✌️

## What am I going to do next?

I will make a script
to automatically create an interactive page
to display the webpages as nodes
and the hyperlinks as edges of a graph.

Last updated: 8 Aug 2025
