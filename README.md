# Algorithms & Data Structures Platform

## Summary

An educational platform illustrating the implementation of fundamental computer science structures using **Python 3**. This repository serves as a practical guide for understanding the core logic behind data organization, bridging the gap between theoretical algorithmic concepts and clean code implementation.

It emphasizes manual memory management simulation, algorithmic complexity analysis (Big O), and modular software architecture separating theory from execution.

## Features
- **Pure Python Implementation**: Focuses on raw logic without external dependencies.
- **Modular Architecture**: Decouples data structure definitions from laboratory exercises.
- **Type Hinting**: Utilizes modern Python syntax for clarity and robust IDE support.
- **Embedded Documentation**: Theoretical concepts are detailed within docstrings for immediate context.
- **Broad Coverage**: Includes both linear and non-linear structures, from basic Arrays to complex AVL Trees.
- **Efficiency Analysis**: Emphasis on Big O time and space complexity.

## Educational Units

The platform is organized into four core units, mirroring a standard computer science curriculum. Each unit focuses on a specific category of data management and storage.

### Unit 1: Linear Static Data Structures
Foundation of memory management and index-based access. Although Python lists are dynamic, this module enforces static constraints for educational purposes.
- **Introduction**: Memory, Heap vs Stack, and Big O Notation.
- **One-Dimensional Arrays**: Manual implementation of fixed-size array operations.
- **Two-Dimensional Arrays**: Matrix manipulation and triangular logic.

### Unit 2: Dynamic Data Structures
Introduction to Nodes and References, moving away from contiguous memory allocation.
- **Abstract Data Types (ADT)**: Formal specification and interface implementation.
- **Singly Linked Lists**: Unidirectional nodes and dynamic insertion logic.
- **Doubly Linked Lists**: Bidirectional navigation and link management.
- **Circular Linked Lists**: Ring topology and applications like the Josephus problem.

### Unit 3: Stacks and Queues
Implementation of restricted access policies, essential for OS process scheduling.
- **Stacks (LIFO)**: Last-In, First-Out logic using both Arrays and Linked Lists.
- **Queues (FIFO)**: First-In, First-Out logic for task scheduling.
- **Priority Queues**: Dequeuing based on priority rather than arrival time.

### Unit 4: Non-Linear Data Structures
Advanced hierarchical data representation using heavy recursion.
- **General Trees**: N-ary tree implementation for hierarchical systems.
- **Binary Trees**: Strict structures with preorder, inorder, and postorder traversals.
- **Binary Search Trees (BST)**: Optimized O(log n) search operations.
- **AVL Trees**: Self-balancing BSTs implementing single and double rotations.

## Project Structure

The repository follows a strict modular pattern to separate theory from practice:

```text
unit-XX-name/
├── YY-topic-name/
│   ├── structure_name.py  # Data structure logic and theory (Docstrings)
│   └── exercises.py       # Laboratory practice and implementation tests
```

## Guides

To get the most out of this repository, follow these steps:

1.  **Theory First**: Check the `structure_name.py` file in the relevant unit. Read the docstrings to understand the underlying logic and complexity.
2.  **Practice Second**: Run the corresponding `exercises.py` to see the implementation in action.
3.  **Visualization**: Use the VSCode Debugger to step through pointers (especially in Linked Lists and Trees) to visualize how nodes connect in memory.

## Reference Documentation

- [Official Python 3 Documentation](https://docs.python.org/3/)
- [PEP 484 – Type Hints](https://peps.python.org/pep-0484/)
- [TimeComplexity - Python Wiki](https://wiki.python.org/moin/TimeComplexity)
- [Visualgo - Data Structure Visualization](https://visualgo.net/en)

## Prerequisites & Setup

This project requires no complex build tools.

1.  **Python Version**: Ensure you have Python 3.10 or higher.
2.  **Installation**:
    ```bash
    git clone <repository-url>
    cd PY-DATA-STRUCTURES
    ```
3.  **Running Exercises**:
    ```bash
    # Example: Run Singly Linked List exercises
    python3 unit-02-dynamic-data-structures/02-singly-linked-lists/exercises.py
    ```