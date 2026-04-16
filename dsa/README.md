# Data Structures and Algorithms (DSA) :sunny:

A collection of data structures and algorithms implemented in C++11, featuring various implementations for linked lists, trees, and general algorithms.

---

## Features

- **Linked Lists**: Single and double linked list implementations.
- **Trees**: Binary tree traversals and operations.
- **Algorithms**: Memory alignment, permutations, combinations, and more.
- **Unit Testing**: Comprehensive tests using Google Test.
- **Documentation**: Detailed MD docs for various DSA topics.

## Getting Started

### Prerequisites

- C++11 compatible compiler (e.g., GCC, Clang)
- CMake 3.0 or higher
- Google Test (optional, for running tests)

### Build Instructions

```bash
mkdir build && cd build
cmake ..
make
```

### Running Examples

After building, you can run various executables generated in the build directory:

```bash
./linked_list
./binary_tree
./algorithm
```

### Running Tests

```bash
cd build
ctest
# Or run the unit test binary directly
./unit_test/unit_test.run
```

## Documentation

Documentation is located in the `docs/` directory. You can also use [MkDocs](https://www.mkdocs.org/) to serve the documentation:

```bash
mkdocs serve
```

## Related Projects

- [GraphX](https://github.com/cggos/GraphX): A graph processing library.

## License

This project is licensed under the BSD-style license - see the [LICENSE](LICENSE) file for details.
