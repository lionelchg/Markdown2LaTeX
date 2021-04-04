# Markdown2LaTeX

Converter from markdown file using KaTeX to `.tex` files

## Installation

Install the package when in the root directory (where the `setup.py` file is), then run:

```shell
pip install -e .
```

A variable environnement needs to be created to indicate where the folder `md2latex/` is. In your `.bashrc` of `.zshrc`:

```shell
export MDTOLATEX_HOME=path/to/md2latex
```

## Convert

To convert markdown files along with the macros:

```shell
md2latex -f markdown_filename -m macros_filename
```
