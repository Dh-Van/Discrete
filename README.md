# Discrete Math GHW Collaboration

This project uses LaTeX's `\subfile` package to manage our group homework. Each problem is a separate `.tex` file, which allows us to work in parallel and compile everything into one final document.

---

## Quick Start

Follow these two rules to ensure everything compiles correctly.

### 1. File Naming Convention

**This is the most important rule.** You **must** name your file according to the problem number you are working on.

* **Format:** `Problem<Number>.tex`
* **Examples:** `Problem1.tex`, `Problem5.tex`, `Problem12.tex`

### 2. LaTeX Setup

To simplify the preamble and ensure consistent formatting, we use a custom style file.

1.  **Download:** Get the `discrete.sty` file from this repository.
2.  **Upload:** Add the `discrete.sty` file to the root directory of your LaTeX project (e.g., in Overleaf, click the "Upload" button).
3.  **Use Package:** Add the following command to the top of your `Problem<Number>.tex` file:
    ```latex
    \usepackage{discrete}
    ```

---

## How It Works

Each `Problem<Number>.tex` file is a standalone document that can be compiled on its own. This is great for focusing on your specific problem without needing the whole project.

A central `main.tex` file uses the `\subfile` command to import all the individual problem files, assembling them into the complete homework submission. You generally won't need to edit this file, but you can compile it to see the full, up-to-date assignment at any time.