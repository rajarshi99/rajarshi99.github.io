ls *.md | while read md_file
do
		pandoc $md_file -o ${md_file%.*}.html
		echo $md_file to ${md_file%.*}.html
done
