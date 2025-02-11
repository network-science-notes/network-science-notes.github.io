.ONESHELL: 

PYTHON = env/bin/python3

publish: 
	$(PYTHON) scripts/prep-qmd.py
	quarto render --profile publish
	$(PYTHON) scripts/create-ipynb.py
	$(PYTHON) scripts/remove-hidden.py
	git add .
	git commit -m "Update"
	git push

prep: 
	$(PYTHON) scripts/prep-qmd.py
	$(PYTHON) scripts/create-ipynb.py

preview: 
	quarto preview --profile preview

clean: 
	find . -type f -name "* [0-9]*" -delete
	find . -name "* [0-9]*" -type d -exec rm -r "{}" \;
	rm -rf docs
	rm -rf chapters

scrub: 
	find . -type f -name "* [0-9]*" -delete

