# Data Structures and Algorithms (DSA)

C++11 implementations of fundamental data structures and algorithms, living as a subdirectory of [GraphX](https://github.com/cggos/GraphX).

> **Note:** Binary tree code lives at `../tree/` (GraphX root), compiled here as the `binary_tree` target.

---

## Contents

- **`linked_list/`** — Single and double linked list implementations
- **`alg/`** — Memory alignment, permutations, combinations, and more
- **`mix/`** — Queue, sparse matrix
- **`unit_test/`** — Google Test suite (requires external `cgads` library)

## Build

```bash
mkdir build && cd build
cmake ..
make
```

Targets: `linked_list`, `binary_tree`, `sparse_matrix`, `algorithm`, `mem_align`, `array_string`, `permutation_combination`, and more.

### Tests

```bash
ctest
# or directly:
./unit_test/unit_test.run
```

GTest is auto-detected by CMake. `unit_test` additionally requires the `cgads` library.

## Documentation

Docs are in `../docs/tree/`, `../docs/alg/`, `../docs/cpp/` and served via the GraphX MkDocs site:

```bash
cd .. && mkdocs serve
```
