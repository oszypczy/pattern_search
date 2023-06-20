# Pattern Search Program Readme

This Python program performs pattern search using three different algorithms: Naive, KMP, and KR. It generates a graph to compare the execution time of these algorithms when searching for patterns in a given text.

## Usage

To use the program, follow these steps:

1. Make sure you have Python installed on your system.
2. Download or clone the repository containing the program files.
3. Place the `pan-tadeusz-unix.txt` file in the same directory as the program files. This file contains the text in which patterns will be searched.
4. Open a terminal or command prompt and navigate to the directory containing the program files.
5. Run the `main.py` file using the command: `python main.py`.
6. The program will execute the pattern search algorithms and generate a graph showing the execution time for each algorithm.
7. The resulting graph will be saved as `joined_search_time_graph.png` in the same directory.

## Algorithm Descriptions

The program uses the following pattern search algorithms:

### Naive Algorithm

The naive search algorithm iterates over every character in the text, looking for an exact match of the pattern. It returns the indices where the pattern is found in the text. If the pattern is empty or larger than the text, an empty list is returned.

### KMP Algorithm

The Knuth-Morris-Pratt (KMP) algorithm is a more efficient pattern search algorithm. It constructs a partial match table for the pattern, which determines the amount to jump in the text if a character doesn't match. The algorithm uses this table to avoid unnecessary comparisons. It returns the indices where the pattern is found in the text. If the pattern is empty or larger than the text, an empty list is returned.

### KR Algorithm

The Karp-Rabin (KR) algorithm is a probabilistic pattern search algorithm. It uses hash functions to quickly compare the pattern with substrings of the text. It returns the indices where the pattern is found in the text. If the pattern is empty or larger than the text, an empty list is returned.

## Graph Generation

The program generates a graph to compare the execution time of the naive, KMP, and KR algorithms. It measures the time taken by each algorithm to search for patterns of different lengths in the provided text. The x-axis represents the number of words to search, ranging from 100 to 1000. The y-axis represents the time taken by each algorithm in seconds. The resulting graph is saved as `joined_search_time_graph.png`.

## Additional Information

The program uses the "Pan Tadeusz" book as the text for pattern search. Some tests have been conducted using pytest.

Note: It's assumed that the `matplotlib` library is installed to generate the graph.

For any questions or issues, please contact the program author.
