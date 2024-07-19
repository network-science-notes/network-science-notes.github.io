.ONESHELL: 

SHELL = /bin/zsh


	

VENV_ACTIVATE = . env/bin/activate
activate: 
	$(VENV_ACTIVATE)


publish: prep
	$(VENV_ACTIVATE)
	quarto render --profile publish

prep: 
	$(VENV_ACTIVATE) 
	python scripts/create-ipynb.py
	python scripts/prep-qmd.py

preview: 
	$(VENV_ACTIVATE) 
	quarto preview --profile preview

clean: 
	find . -type f -name "* [0-9]*" -delete
	find . -name "* [0-9]*" -type d -exec rm -r "{}" \;
