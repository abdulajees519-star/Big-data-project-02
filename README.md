# MapReduce Engine using Python - Programming Languages Analysis

## Project Overview

This project demonstrates the implementation of a simple **MapReduce Engine** using Python. The input dataset contains different programming language names, and the MapReduce process calculates the frequency of each programming language.

The project simulates the core stages of the Hadoop MapReduce framework, including Mapping, Partitioning, and Reducing.

## Objective

The objective of this project is to understand the MapReduce programming model by processing programming language data and generating the frequency of each language.

## Technologies Used

- Python 3.x
- File Handling
- Dictionaries
- Hash Function
- Functions

## Project Structure

MapReduce/
│── input.txt
│── main.py
│── mapper.py
│── partitioner.py
│── reducer.py

## File Description

### main.py

Controls the complete execution of the MapReduce process.

Responsibilities:

- Reads the input file
- Splits the input into two parts
- Calls the Mapper
- Calls the Partitioner
- Calls the Reducer
- Displays the final frequency count

### mapper.py

Reads each programming language from the input file and converts it into an intermediate key-value pair.

Example

Input

Python

Output

(Python, 1)

### partitioner.py

Distributes the intermediate key-value pairs into partitions using the following hash function:

hash(key) % number_of_reducers

This ensures that all occurrences of the same programming language are processed by the same reducer.

### reducer.py

Groups identical programming language names and calculates their total count.

Example

Input

Python 1
Python 1
Python 1

Output

Python 3

### input.txt

Contains programming language names used as the input dataset.

Example

Python Java Python
C C++ Java
Python JavaScript

## Execution Steps

1. Open the project folder in Visual Studio Code.

2. Open the Terminal.

3. Run the following command:

python main.py

4. The program displays:

- Partition Output
- Final Frequency Count

## Sample Output

----- Final Output -----

C 5
C++ 3
Java 8
JavaScript 3
Python 9

## Workflow

input.txt
      │
      ▼
Read Input
      │
      ▼
Mapper
      │
      ▼
(Key, Value) Pairs
      │
      ▼
Partitioner
      │
      ▼
Reducer
      │
      ▼
Final Output-

## Concepts Used

- MapReduce
- Mapper
- Partitioner
- Reducer
- Hash Partitioning
- Key-Value Pairs
- Data Aggregation
- File Handling
- Python Programming

## Learning Outcomes

After completing this project, we learned:

- The working principle of the MapReduce framework.
- How Mapper converts records into key-value pairs.
- How Hash Partitioning distributes data among reducers.
- How Reducer aggregates identical keys.
- How Python simulates a simple MapReduce Engine.
