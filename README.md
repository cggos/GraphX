# GraphX

**Graph Anything**

GraphX is a research and experimentation repository dedicated to graph theory, data visualization, and graphical algorithms. It serves as a centralized hub for exploring various graph engines and visualization tools.

---

## 🚀 Key Technologies

- **Graph Engines**: [igraph](https://igraph.org/) (Python & R), [GraphViz](https://graphviz.org/) (DOT)
- **Visualization**: [cairocffi](https://pypi.org/project/cairocffi/), [Inkscape](https://inkscape.org/) (SVG)
- **Documentation**: [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)
- **Languages**: Python, R, DOT, Markdown

---

## 📁 Project Structure

- `docs/`: Project documentation and guides.
- `igraph/`: Implementations using the igraph library in Python and R.
- `GraphViz/`: Examples and templates for the DOT language.
- `Inkscape/`: SVG design templates.
- `python/`: Custom graph data structure implementations and experiments.

---

## 🛠️ Quick Start

### Documentation
View the local documentation site:
```bash
pip install mkdocs-material
mkdocs serve
```

### Python Experiments
Install dependencies and run a sample script:
```bash
pip install python-igraph cairocffi
python igraph/python/ig00.py
```

---

## 📊 Examples

### GraphViz with Dot

```graphviz
graph {
    orientation=landscape

    // node[shape=circle];
    a -- b[color=red,penwidth=3.0];
    b -- c;
    c -- d[color=red,penwidth=3.0];
    d -- e;
    e -- f;
    a -- d;
    b -- d[color=red,penwidth=3.0];
    c -- f[color=red,penwidth=3.0];
}
```

### Image Matching Graph

- Based on [libccv](https://pypi.org/project/libccv/)

<p align="center">
  <img src="https://github.com/cggos/ccv/blob/master/python/imgs/imgmatch_graphviz.png" style="width: 80%"/>
</p>

---

## 🔗 Related Projects

- [DSA (Data Structures and Algorithms)](https://github.com/cggos/DSA)
