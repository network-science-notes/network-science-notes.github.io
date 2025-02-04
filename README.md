# Setup

## Quarto 

Please install Quarto version 1.5 or later. You can run `quarto --version` in the terminal to see what version of Quarto is currently installed. 

## Virtual Environment

To run scripts and build this website, we will use a custom virtual environment. 

To create the environment, run the following command:

```bash
python3 -m venv env
```

### Package Installation

To install packages in this environment:

```bash
source env/bin/activate

python3 -m pip install numpy pandas matplotlib seaborn mesa jupyter networkx scikit-learn scipy jupyter-cache ipykernel
```

Most other packages can be installed in the same way. 

# Writing Content

## Add a Chapter

To add a chapter to the site: 

1. Create a new file in the `source` directory with format `<number>-<chapter-name>.qmd`. The `<number>` is just for organizing the sequencing of the notes. 
2. Copy over the metadata from a previous document. This metadata controls some aspects of the behavior of each document, and most of it can be modified. The most important field is `jupyter: python3`, which should not be changed. 
3. Add the filename above to the files `_quarto-preview.yml` and `_quarto-publish.yml`. You can also add a new top-level section for the chapter if desired. 

You are now ready to write the chapter! Quarto implements standard Markdown and mathematics, as well as computation with Python and some useful tools for cross-references. 

## Hidden Solutions 

To add hidden solutions to the lecture notes, use the following syntax: 

```markdown
This is content that will appear in the public lecture notes. 

::: {.hide .solution}

This is a hidden solution which will not appear in the public lecture notes. 

:::
```

It is possible to add classes other than `.solution`, but the `.hide` class must be present. For example, we have added a `.proof` class.

Hidden solutions will not appear in the published online notes, but (after running `make publish`) will be present in the local folder `docs/full-notes`. The notes in this directory can be opened locally and printed to PDF or directly to a printer.  

# Previewing and Publishing

Before either previewing or publishing the website, it is necessary to run 

```bash
source env/bin/activate
```

in the terminal. 

## Preview Site 

To preview the site, run the command `make preview` in your terminal. This will build a preview version of the site and open it in your default browser. 

## Publish Site 

To publish the site:

1. Run the command `make publish` in your terminal. This will build a copy of the site, including processing of notebooks for live-coding, and then place the results in the `docs` folder. 
2. Then, commit changes to any source `.qmd` chapters, as well as the complete contents of the `docs` folder, and push to GitHub. 



 
