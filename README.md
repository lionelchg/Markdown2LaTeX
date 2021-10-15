# Markdown2LaTeX

Converter from markdown file using KaTeX to `.tex` files. The conversion is very close to the original markdown file compared to `pandoc`. A related blog post can be found [here](https://lionelchg.github.io/blog/2021/notes/).

## Installation

Install the package when in the root directory (where the `setup.py` file is), then run:

```shell
pip install -e .
```

A variable environnement needs to be created to indicate where the folder `md2latex/` is. In your `.bashrc` or `.zshrc`:

```shell
export MDTOLATEX_HOME=path/to/md2latex
```

## Convert

To convert markdown files along with macros defined in KaTeX:

```shell
md2latex -f markdown_filename -m macros_filename
```

A demo is provided in the `example/` folder. Go into the folder and execute

```shell
md2latex -f example.md -m macros.md
```

## How does it work?

`md2latex` uses regex to parse the markdown file and convert the entries to LaTeX. An initial template is given to the python script (`template.tex` in `md2latex/`). As of now the following conversions are made:

- `$$..$$` and related to `equation`, `align` environments
- Lists in `1. 2. 3.` are converted to `enumerate` environment, `- - -` in `itemize` environment
- Markdown tables are converted to LaTeX tables

For all these conversions to work the original markdown file must follow the standard markdown format where tables, lists and equations are surrounded by blank lines.

