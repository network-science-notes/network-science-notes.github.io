.ONESHELL: 

SHELL = /bin/zsh


	

VENV_ACTIVATE = . env/bin/activate
activate: 
	$(VENV_ACTIVATE)


publish: 
	$(VENV_ACTIVATE)
	python scripts/prep-qmd.py
	quarto render --profile publish
	python scripts/create-ipynb.py
	python scripts/remove-hidden.py

prep: 
	python scripts/prep-qmd.py
	python scripts/create-ipynb.py

preview: 
	$(VENV_ACTIVATE) 
	quarto preview --profile preview

clean: 
	find . -type f -name "* [0-9]*" -delete
	find . -name "* [0-9]*" -type d -exec rm -r "{}" \;
	rm -rf docs
	rm -rf chapters

