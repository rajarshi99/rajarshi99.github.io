split($9, fname, ".") == 2 && fname[2] == "md"{
	entry = fname[1]
	getline headline < (entry ".md")
	sub(/#/, "", headline)
	printf "\n\n---\n\n> [%s](%s.html)\n", headline, entry
	for(n = 5; (getline line1 < (entry ".md")) > 0 && n > 0; n--){
		sub(/#*/, "", line1)
		printf "\n> " line1
		}
	printf "...<p align=\"right\"> %s %s %s </p>\n\n", entry, $6, $7
	}
