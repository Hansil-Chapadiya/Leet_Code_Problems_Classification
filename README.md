# LeetCode Problems Classifier

A Python-based tool to classify LeetCode problems by their difficulty level (`Easy`, `Medium`, or `Hard`) using the LeetCode API. The tool processes problem numbers from a dataset (e.g., filenames) and maps them to their difficulty level.

---

## Features

- **Extract Problem Numbers:** Parses filenames or other structured data to extract problem numbers.
- **Fetch Difficulty Levels:** Uses LeetCode's public API to fetch difficulty levels for the problems.
- **Classification:** Maps problem numbers to their respective difficulties and handles missing data gracefully.
- **Custom Dataset Support:** Works with any input containing problem numbers, such as filenames or structured files.
- **File Cleanup:** Optionally deletes unnecessary files (e.g., `.exe`) from a given folder.

---

## Prerequisites

### 1. Python 3.x
Ensure you have Python installed. If not, download it from [Python.org](https://www.python.org/).

### 2. Dependencies
Install the required Python libraries:


## Example Output
- Input
- Problem Numbers: [6, 26, 128, 179, 214]
  Problem 6: Easy
  Problem 26: Medium
  Problem 128: Hard
  Problem 179: Medium
  Problem 214: Hard
