split($9, fname, ".") == 2 && fname[2] == "md"{
	entry = fname[1]
	getline headline < (entry ".md")
	sub(/#/, "", headline)
	printf "\n\n---\n\n> [%s](%s.html) <b>%s</b>\n\n", entry, entry, headline
	for(n = 5; (getline line1 < (entry ".md")) > 0 && n > 0; n--)
		print "> " line1
	printf "... <p align=\"right\"> %s %s </p>\n\n", $6, $7
	}
