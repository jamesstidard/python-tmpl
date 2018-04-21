git:
	pipenv lock
	git init
	git add .
	git commit -m "init"
	hub create {{if GitHubPrivate}} -p {{end}}"{{GitHubRepository}}"
	git push -u origin master
