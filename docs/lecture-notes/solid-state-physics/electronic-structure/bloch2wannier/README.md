# Bloch-to-Wannier lecture-note source

`main.tex` is a standalone lecture-note rendering derived from the accepted exploratory notebook and its Markdown companion.

Build locally with:

```sh
make
```

The Makefile invokes `latexmk` and does not install or modify repository dependencies. A local TeX distribution providing the packages imported by `main.tex` is required.

Remove generated files with:

```sh
make clean
```

Do not commit generated PDFs or LaTeX auxiliary/build artifacts. The scientific and pedagogical claim boundary is stated in `main.tex`; in particular, the source preserves all four limitations of the exploratory notebook.
