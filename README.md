# Library Management System

## Project Overview

The Library Management System is designed to organize library resources effectively, catering to both patrons' needs and administrators' requirements for reporting and managing library operations. It uses an innovative tree data structure for categorization and a priority queue for efficient order processing.

---

## Features

1. **Category and Subcategory Management**:
   - Add and organize categories and subcategories.
2. **Book Management**:
   - Add, remove, search, and list books.
3. **Order Processing**:
   - Place orders with a priority queue based on price and submission time.
4. **Command-Line Interface**:
   - User-friendly command-line interface for all operations.

---

## How to Use

    - `Add Category <category name>`: Add a new category to the tree.
    - `Add Subcategory <subcategory name> to <category name>`: Add a subcategory to an existing category.
    - `Add Book <book data> to <category name>`: Add a book to a specified category.
    - `Remove Book <book name> from <category name>`: Remove a book from a specified category.
    - `Search <book name>`: Display information about a specific book.
    - `List Books`: Display all books.
    - `List Books from <category name>`: Display all books in a category.
    - `Order <book name>`: Place an order for a book.
    - `List Orders`: View the prioritized order queue.

---

## Key Components

1. **Tree Data Structure**:
   - Organizes categories and subcategories efficiently.
   - Stores books under relevant categories or subcategories.

2. **Priority Queue (Max Heap)**:
   - Manages orders based on price and submission time.
   - Ensures efficient and fair order processing.
  
---

## Feedback

We welcome your feedback and suggestions! Feel free to reach out or open an issue in this repository.
