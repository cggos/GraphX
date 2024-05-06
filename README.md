# GraphX

- DSA: https://github.com/cggos/DSA

---

## GraphViz with Dot

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

## Image Matching Graph

- https://pypi.org/project/libccv/

<p align="center">
  <img src="https://mirror.ghproxy.com/https://github.com/cggos/ccv/blob/master/python/imgs/imgmatch_graphviz.png" style="width: 80%"/>
</p>
