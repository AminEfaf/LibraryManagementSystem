Introduction and Manual for Library Management System

Welcome to our Library Management System, a comprehensive tool designed to organize and streamline library operations efficiently! 📚🖥️

System Objective:

The primary goal of this project is to develop a system tailored for organizing library resources, catering to both patrons' needs and administrators' requirements for reporting and managing library operations. 📊🔍

In this system, library administrators can define and remove books from the library. Each book's information includes its title, author, and price. The proposed data structure for storing these books is a tree, with the library manager overseeing this structure. Each tree node can contain a list of books or subcategories. 📝🌳

Project Features and Commands:

Your project should encompass the following functionalities and commands:

Add Category <category name>: Add a new category to the tree.
Add Subcategory <subcategory name> to <category name>: Add a subcategory to an existing category.
Add Book <book data> to <category name>: Add a book to a specified category.
Remove Book <book name> from <category name>: Remove a book from a specified category.
Search <book name>: Display information about a specific book.
List Books: Display information about all books.
List Books from <category name>: Display information about all books within a particular category.
Order <book name>: Place an order for a book.
List Orders: View the order queue and process each order.
Order Queue Management:

The library utilizes a priority queue to manage orders, prioritizing based on the price of the order and the time of submission. Orders with identical prices are prioritized based on submission time, giving precedence to earlier submissions. The library manager observes the queue in ascending order of priority, ensuring efficient order processing. To implement the order queue, use a Max Heap, where the root always represents the order with the highest priority.

How the Program Works:

Upon starting the program, the user is presented with a command-line interface where they can input commands to interact with the library management system.
The user can issue various commands to add categories, subcategories, books, remove books, search for books, list all books, list books within specific categories, place orders, and view order queues.
The system uses a tree data structure to organize categories and subcategories, ensuring efficient categorization of books.
Books are added to the appropriate categories or subcategories within the tree structure.
Orders placed by users are managed using a priority queue, where orders are prioritized based on price and submission time.
The library manager can view the order queue, process orders, and ensure timely delivery of requested books.
Get ready to revolutionize library management with our comprehensive system! Are you prepared to embark on this journey towards efficient library operations? 📚💼
