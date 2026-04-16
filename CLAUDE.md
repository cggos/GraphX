# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## About GraphX

GraphX is a research and experimentation repository for graph theory, data visualization, and graphical algorithms. It explores multiple graph engines and visualization tools across several languages. It is not a single application — it is a collection of standalone scripts and documentation organized by tool/language.

## Commands

### Documentation (MkDocs)
```bash
pip install mkdocs-material pymdown-extensions
mkdocs serve        # local dev server
mkdocs build        # static site output
```

### Python igraph scripts
```bash
pip install python-igraph cairocffi
python igraph/python/ig00.py   # run any script directly
```

### Python custom graph implementations
```bash
python python/g00.py
```

### R igraph scripts
```R
install.packages("igraph")
Rscript igraph/R/ig00.R
```

### GraphViz DOT rendering
```bash
dot -Tpng GraphViz/dot/test.dot -o test.png
dot -Tsvg GraphViz/dot/test.dot -o test.svg
```

### C++ DSA (cmake)
```bash
cd dsa && mkdir -p build && cd build
cmake ..
make
ctest          # requires GTest (auto-detected by cmake)
```

## Architecture

The repo is organized by tool/language — each subdirectory is independent:

- **`python/`** — Pure Python graph data structure implementations (`Vertex`, `Graph` classes with adjacency-list representation). Scripts are standalone experiments; no shared library.
- **`igraph/python/`** — Scripts using the `python-igraph` library (`ig` module). Covers graph construction, adjacency matrices, layouts, and plotting with `cairocffi`.
- **`igraph/R/`** — R scripts using the `igraph` package.
- **`GraphViz/dot/`** — DOT language graph definition files rendered with the `dot` CLI.
- **`Inkscape/`** — SVG templates for visual graph designs; `template.svg` sets the visual standard.
- **`tree/`** — C++ binary tree implementations (tree is a graph subtype). Compiled via `dsa/CMakeLists.txt` as the `binary_tree` target.
- **`dsa/`** — C++ data structures and algorithms (linked lists, sparse matrix, general algorithms, unit tests). Built with CMake from `dsa/`; see `dsa/README.md`. Note: `unit_test` links against an external `cgads` library not included in this repo.
- **`docs/`** — MkDocs source (Markdown). Site config is `mkdocs.yml` with the Material theme and `pymdownx` extensions. Navigation is defined explicitly in `mkdocs.yml` under `nav:`.

## Conventions

- New scripts go into the directory matching their tool/language (e.g., a new igraph Python script → `igraph/python/`).
- Scripts are numbered sequentially (`ig00.py`, `ig01.py`, …).
- Documentation for new experiments belongs in `docs/` or a `README.md` within the relevant subdirectory.
- MkDocs navigation must be updated manually in `mkdocs.yml` when adding new doc pages.
