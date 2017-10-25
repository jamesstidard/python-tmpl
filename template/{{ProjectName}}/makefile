git:
	git init
	git add .
	git commit -m "init"
	hub create {{if GitHubPrivate}} -p {{end}}"{{GitHubRepository}}"
	git push -u origin master
venv:
	pyenv install -s {{PythonVersion}}; \
	pyenv local {{PythonVersion}}; \
	python -m venv ~/.virtualenvs/"{{ProjectName}}"; \
	source ~/.virtualenvs/"{{ProjectName}}"/bin/activate; \
	pip install -r requirements/development.txt;
