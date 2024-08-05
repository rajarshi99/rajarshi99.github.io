{ print }

END {
	n = split(FILENAME, part, "/")
	for(i = 1; i < n; i++)
		footer_path = footer_path part[i] "/"
	while((getline foot_line < (footer_path "footer.txt")) > 0) 
		print foot_line
	}
