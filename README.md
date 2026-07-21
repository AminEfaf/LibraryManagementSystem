# Library Management System

A command-line application for managing library categories, books, and book orders using fundamental data structures.

## Overview

This project was developed as a **Data Structures course project**. It demonstrates the use of a tree data structure for organizing categories and subcategories, and a priority queue (max heap) for processing book orders efficiently.

The system allows users to manage books, search the catalog, and handle prioritized book orders through a simple command-line interface.

## Features

* Add and organize categories and subcategories
* Add, remove, search, and list books
* Store books under relevant categories or subcategories
* Process book orders using a priority queue based on price and submission time
* Interact with the system through a command-line interface

## Commands

* `Add Category <category name>` — Add a new category.
* `Add Subcategory <subcategory name> to <category name>` — Add a subcategory to an existing category.
* `Add Book <book data> to <category name>` — Add a book to a category.
* `Remove Book <book name> from <category name>` — Remove a book from a category.
* `Search <book name>` — Search for a book and display its information.
* `List Books` — Display all books.
* `List Books from <category name>` — Display books in a specific category.
* `Order <book name>` — Place an order for a book.
* `List Orders` — View the prioritized order queue.

## Data Structures Used

* **Tree Data Structure** — Organizes categories and subcategories hierarchically.
* **Priority Queue (Max Heap)** — Manages book orders based on priority criteria.

## Feedback

If you have suggestions or find a bug, please open an issue in this repository.
