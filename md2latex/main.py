import re
import argparse
import os
import numpy as np

def md_main2latex(md_fn:str) -> None:
    """ Convert the markdown file *md_fn* into latex format

    :param md_fn: filename of the markdown file
    :type md_fn: str
    """
    # Markdown file
    md_fp = open(md_fn, 'r')

    # Template file
    template_fp = open(os.getenv('MDTOLATEX_HOME') + '/template.tex', 'r')
    template_lines = template_fp.readlines()

    # Output file
    latex_fn = re.search('(\w*)\.md', md_fn).group(1) + '.tex'
    latex_fp = open(latex_fn, 'w')

    # For sections
    md_heading_patterns = {'\A# (.+)':r'\n\\title{\1}\n\\maketitle',
                           '\n## (.+)':r'\n\\section{\1}',
                           '\n### (.+)':r'\n\\subsection{\1}',
                           '\n#### (.+)':r'\n\\subsubsection{\1}',
                           '\n##### (.+)':r'\n\\paragraph{\1}'}

    # For equations (order matters here)
    md_equation_pattern = {r'\$\$\n\\begin{aligned}([^$]*)\\end{aligned}\n\$\$':r'\\begin{align}\1\\end{align}',
                            r'\$\$\n(\\begin{align}[^$]*\\end{align})\n\$\$':r'\1',
                            r'\$\$\n(\\begin{equation}[^$]*\\end{equation})\n\$\$':r'\1',
                            r'\$\$([^$]*)\$\$':r'\\begin{equation}\1\\end{equation}'}

    # Texts highlighting patterns (order matters here)
    md_text = {'\*\*\*(.*)\*\*\*':r'\\textbf{\\textit{\1}}',
                '\*\*(.*)\*\*':r'\\textbf{\1}',
                '\*(.*)\*':r'\\textit{\1}'}

    # Itemize lists
    md_itemize = {'\n\n-(.*)':r'\n\n\\begin{itemize}\n\\item\1',
                '\n-(.*)\n\n':r'\n\\item\1\n\\end{itemize}\n\n',
                '\n-(.*)':r'\n\\item\1'
                }

    # Enumerate lists
    md_enumerate = {'\n\n\d\.(.*)':r'\n\n\\begin{enumerate}\n\\item\1',
                '\n\d\.(.*)\n\n':r'\n\\item\1\n\\end{enumerate}\n\n',
                '\n\d\.(.*)':r'\n\\item\1'
                }

    # Concatenate the dictionnaries
    replace_dict = {**md_heading_patterns,
                    **md_equation_pattern,
                    **md_text,
                    **md_itemize,
                    **md_enumerate}

    # Concatenate the whole file into one string
    whole_file_str = ''.join(md_fp.readlines())

    # Replace headings then equations
    for pattern, repl in replace_dict.items():
        whole_file_str = re.sub(pattern, repl, whole_file_str)

    # Table treatment - this is a lookahead regex command
    # the DOTALL is very important for this regex to work
    table_pattern = re.compile('\n\n\|(?:(?!\n\n).)*', re.DOTALL)
    while table_pattern.search(whole_file_str):
        begin, end = table_pattern.search(whole_file_str).span()
        table_str = table_pattern.search(whole_file_str).group()[2:]
        elements = [element for element in table_str.split('|') if not element in ['', '\n']]
        ncols = len([i for i, el in enumerate(elements) if '---' in el])
        elements = [element for element in elements if not '---' in element]
        nrows = int(len(elements) / ncols)
        elements = np.array(elements).reshape(nrows, ncols)
        table_latex_str = '\n\n\\begin{center}\n\\begin{tabular}{|' + ' c |' * ncols + '}\\hline\n'
        for irow in range(nrows):
            if irow == 0:
                table_latex_str += ' & '.join(elements[irow, :]) + '\\\\\n\\hline'
            elif irow == nrows - 1:
                table_latex_str += ' & '.join(elements[irow, :]) + '\\\\'
            else:
                table_latex_str += ' & '.join(elements[irow, :]) + '\\\\\n'
        table_latex_str += '\n\\hline\n\\end{tabular}\n\\end{center}\n\n'

        whole_file_str = whole_file_str[:begin] + table_latex_str + whole_file_str[end:]

    # Insert at the right place in the template
    template_lines.insert(31, whole_file_str)

    # Write the latex string
    latex_fp.write(''.join(template_lines))

def md_macros2latex(md_fn):
    """ Convert the markdown file *md_fn* containing macros into latex format

    :param md_fn: filename of the markdown file
    :type md_fn: str
    """
    md_fp = open(md_fn, 'r')

    latex_fn = 'macros.tex'
    latex_fp = open(latex_fn, 'w')

    md_macros_pattern = re.compile(r'\\gdef(\\\w+)(.*)(\{\\.+\})')

    for line in md_fp:
        # Second block useless
        if 'Redefinition of standard macros' in line:
            break
        if md_macros_pattern.search(line):
            macro = md_macros_pattern.search(line).group(1)
            nargs = md_macros_pattern.search(line).group(2)
            if nargs != '':
                nargs = f"[{nargs.count('#')}]"
            macro_repl = md_macros_pattern.search(line).group(3)
            new_line = rf'\newcommand{{{macro}}}{nargs}{macro_repl}'
            latex_fp.write(new_line + '\n')

def convert():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--main_fn', help='Main markdown filename', required=True)
    parser.add_argument('-m', '--macros_fn', help='Macros markdown filename', default=None)
    args = parser.parse_args()

    # Convert main markdown file
    md_main2latex(args.main_fn)

    # Convert macros file if specified
    if args.macros_fn is not None:
        md_macros2latex(args.macros_fn)
    else:
        open('macros.tex', 'w').close()

if __name__ == '__main__':
    convert()