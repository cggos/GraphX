# Gemini CLI Instructional Context: GraphX

This repository, **GraphX**, is a comprehensive knowledge base and experimentation hub for graph theory, visualization, and graphical data structures. It integrates multiple tools and languages to explore "Graphical Anything."

## Project Overview
- **Purpose**: Research, education, and experimentation with graphs and diagrams.
- **Key Technologies**: 
    - **Graph Engines**: [igraph](https://igraph.org/) (Python and R), [GraphViz](https://graphviz.org/) (DOT).
    - **Visualization**: [cairocffi](https://pypi.org/project/cairocffi/), [Inkscape](https://inkscape.org/) (SVG).
    - **Documentation**: [MkDocs](https://www.mkdocs.org/) with the [Material theme](https://squidfunk.github.io/mkdocs-material/).
    - **Languages**: Python, R, DOT, Markdown.

## Directory Structure
- `docs/`: Source files for the MkDocs documentation site.
- `igraph/`: 
    - `python/`: Python scripts demonstrating `python-igraph` usage.
    - `R/`: R scripts demonstrating `igraph` usage in R.
- `GraphViz/`: Examples and README for DOT language graphs.
- `Inkscape/`: SVG templates and graphical assets.
- `python/`: General Python implementations of graph data structures and experiments.

## Getting Started

### Documentation
The documentation is managed by MkDocs.
- **Build/Serve**: 
  ```bash
  pip install mkdocs-material pymdown-extensions
  mkdocs serve
  ```
- **Configuration**: See `mkdocs.yml` for navigation and plugin settings.

### Python Environment
To run the Python graph scripts:
- **Core Dependencies**:
  ```bash
  pip install python-igraph cairocffi
  ```
- **Usage**: Most scripts are standalone experiments (e.g., `python python/g00.py`).

### R Environment
To run the R scripts:
- **Dependency**: Install the `igraph` package in R:
  ```R
  install.packages("igraph")
  ```
- **Usage**: Run scripts like `igraph/R/ig00.R` in an R environment.

### GraphViz (DOT)
- **Rendering**: Use the `dot` command-line utility.
  ```bash
  dot -Tpng GraphViz/dot/test.dot -o test.png
  ```

## Development Conventions
- **Experimentation**: New graph algorithms or visualization techniques should be added to their respective tool/language directory.
- **Documentation First**: Ensure new scripts or findings are documented in the `docs/` folder or relevant READMEs.
- **Aesthetics**: Follow the visual standards established in `Inkscape/template.svg` and `mkdocs.yml` for consistent graphical output.
