# About my website

My [website](https://rajarshi99.github.io/)
is hosted by GitHub.
To do so I had to create a repository
with the name `rajarshi99.github.io`
and the rest was pretty easy.
If your github username is xyz
then you would need to create
the repository `xyz.github.io`, in my opinion.

For easy editing I write the content in markdown
and then I run a custom `Makefile`
using the `make` command.
The `Makefile` concatenates `footer.md`
to each of the files with the extension `.md`
and then uses the `pandoc` program
to generate the required web pages.

Last updated: 3 Aug 2024
