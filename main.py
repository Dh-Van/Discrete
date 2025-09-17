import os

GHW = 2
PROBLEMS = 4

os.makedirs(f'GHW{GHW}/problems')

TEMPLATE = rf"""\documentclass[11pt]{{article}}

\usepackage{{../discrete}}

\begin{{document}}

\title{{Group HW \#{GHW}}}
\author{{Michael Ku, Dhvan Shah, Pranav Bonthu}}
\maketitle

"""

with open(f'GHW{GHW}/main.tex', 'w') as f:
    f.write(TEMPLATE)
    
    for i in range(1, PROBLEMS + 1):
        f.write(r'\subfile{problems/Problem' + str(i) + '.tex}\n')
        
    f.write('\n' + r'\end{document}')