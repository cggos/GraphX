# Design: Merge DSA into GraphX

**Date:** 2026-04-16  
**Approach:** Plan A — direct file copy, no git history preservation

## Goal

Merge the contents of the sibling repository `/opt/user_data/code/DSA` into GraphX. DSA contains C++ implementations of linked lists, trees, and general algorithms, plus MkDocs documentation.

## Target Directory Structure

```
GraphX/
├── tree/                        # From DSA/tree/ — tree is a graph subtype, lives at root
│   ├── binary_tree.cc / .h
│   ├── binary_tree_01.cc / .h
│   └── main.cc
│
├── dsa/                         # New subdirectory for remaining DSA content
│   ├── alg/                     # DSA/alg/ unchanged
│   ├── linked_list/             # DSA/linked_list/ unchanged
│   ├── mix/                     # DSA/mix/ unchanged
│   ├── unit_test/               # DSA/unit_test/ unchanged
│   ├── .clang-format
│   ├── README.md                # DSA's original README
│   └── CMakeLists.txt           # Adjusted for new tree/ path
│
├── docs/
│   ├── tree/README.md           # From DSA docs/tree/
│   ├── alg/
│   │   ├── README.md
│   │   ├── dp.md
│   │   ├── search.md
│   │   ├── sort.md
│   │   └── traversal.md
│   ├── cpp/
│   │   ├── README.md
│   │   └── lib.md
│   └── ... (existing GraphX docs unchanged)
│
└── mkdocs.yml                   # Extended with Tree / Algorithms / C++ nav sections
```

## File Decisions

| DSA file | Action |
|---|---|
| `tree/` | Copy to `GraphX/tree/` |
| `alg/`, `linked_list/`, `mix/`, `unit_test/` | Copy to `GraphX/dsa/<dir>/` |
| `.clang-format` | Copy to `GraphX/dsa/` |
| `CMakeLists.txt` | Copy to `GraphX/dsa/`, adjust tree path |
| `README.md` | Copy to `GraphX/dsa/README.md` |
| `docs/tree/`, `docs/alg/`, `docs/cpp/` | Copy to `GraphX/docs/<dir>/` |
| `GEMINI.md` | Skip — GraphX has CLAUDE.md |
| `LICENSE` | Skip — GraphX has its own LICENSE |
| `docs/CNAME` | Skip — GraphX already has one |
| `mkdocs.yml` | Skip — GraphX's mkdocs.yml extended instead |

## CMakeLists.txt Changes

`dsa/CMakeLists.txt` needs two path adjustments because `tree/` moves from `dsa/tree/` to `../tree/`:

```cmake
# Before
include_directories(${PROJECT_SOURCE_DIR})
aux_source_directory(${PROJECT_SOURCE_DIR}/tree SRC_TREE)

# After
include_directories(${PROJECT_SOURCE_DIR} ${PROJECT_SOURCE_DIR}/..)
aux_source_directory(${PROJECT_SOURCE_DIR}/../tree SRC_TREE)
```

## mkdocs.yml Changes

Append three new nav sections to GraphX's `mkdocs.yml`:

```yaml
  - Tree:
    - Overview: tree/README.md

  - Algorithms:
    - Overview: alg/README.md
    - Traversal: alg/traversal.md
    - Search: alg/search.md
    - Sort: alg/sort.md
    - Dynamic Programming: alg/dp.md

  - C++:
    - Overview: cpp/README.md
    - Libs: cpp/lib.md
```

## Build & Test

After merge, DSA's C++ code is built from `GraphX/dsa/`:

```bash
cd GraphX/dsa
mkdir build && cd build
cmake ..
make
ctest
```
