split($9, fname, ".") == 2 && fname[2] == "md"{
	entry = fname[1]
	for(n = 8; (getline line < (entry ".md")) > 0 && n > 0; n--){
		if(sub(/title:/, "", line))
			title = line
		}
	printf "\n\n---\n\n[%s](%s.html)\n", title, entry
	printf "<p align=\"right\"> ... %s %s %s </p>\n\n", entry, $6, $7
	}
