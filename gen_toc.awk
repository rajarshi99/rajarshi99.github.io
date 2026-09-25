split($9, fname, ".") == 2 {
	entry = fname[1]
	printf "\n<span style=\"float: right;\"> %s </span>\n</p>\n\n", $6 $7
	for(n = 8; (getline line < (entry ".md")) > 0 && n > 0; n--){
		if(sub(/title:/, "", line))
			printf "\n\n\n- **[%s](%s.html)**\n", line, entry
		else if((line !~ /author:.*/) && (line !~ /^---/))
			printf "\n%s", line
		}
	print "..."
	}
