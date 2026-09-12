split($9, fname, ".") == 2 {
	entry = fname[1]
	for(n = 8; (getline line < (entry ".md")) > 0 && n > 0; n--){
		if(sub(/title:/, "", line))
			printf "\n\n---\n\n[%s](%s.html)\n", line, entry
		else if((line !~ /author:.*/) && (line !~ /^---/))
			print line
		}
	print "..."
	printf "<p align=\"right\"> %s </p>\n\n", $6 $7
	}
