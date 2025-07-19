
# Line-watch: A Custom Regular Expression Engine (CLI Utility)

[![PyPI version](https://img.shields.io/pypi/v/line-watch)](https://pypi.org/project/line-watch/)
[![Python](https://img.shields.io/pypi/pyversions/line-watch)](https://pypi.org/project/line-watch/)
[![License](https://img.shields.io/github/license/yourusername/line-watch)](LICENSE)

## 🚀 Project Overview

Line-watch is a versatile command-line interface (CLI) utility, developed in Python to emulate and expand upon the core functionalities of tools like `grep`. What makes Line-watch unique is its **entirely custom-built regular expression engine**. This project was an engaging exploration into fundamental computer science concepts, including **compiler design principles, lexical analysis, parsing techniques, and finite automata theory**, aiming to build a self-contained and efficient solution for text pattern matching.

It provides a practical tool for searching text while also serving as a clear demonstration of how a regex engine can be constructed from the ground up. The engine's core relies on a **recursive backtracking algorithm**, which effectively simulates the behavior of Non-deterministic Finite Automata (NFAs) to provide flexible and accurate pattern matching.

-----

## ✨ Core Capabilities

Line-watch offers a solid set of features, covering many common regular expression syntaxes:
  * **Extensive Regex Syntax Coverage**:
      * **Literal Character Matching**: Exact identification of character sequences.
      * **Wildcard (`.`)**: Matches any single character (excluding newline).
      * **Anchors (`^`, `$`):**
          * `^`: Asserts position at the beginning of a line.
          * `$`: Asserts position at the end of a line.
      * **Character Classes**:
          * `\d`: Matches any decimal digit (0-9).
          * `\w`: Matches any "word" character (alphanumeric `[a-z, A-Z, 0-9]` and underscore `_`).
      * **Character Sets (`[]`)**:
          * `[abc]`: Matches any single character from a specified explicit set.
          * `[^abc]`: Matches any single character *not* in the specified set (negated character class).
          * `[a-z]`: Supports character ranges for concise definition (e.g., `[a-z]`, `[0-9]`).
      * **Quantifiers**: Control over the repetition of the preceding element:
          * `*`: Matches zero or more occurrences.
          * `+`: Matches one or more occurrences.
          * `?`: Matches zero or one occurrence (optional).
          * `{n}`: Matches exactly `n` occurrences.
          * `{n,}`: Matches `n` or more occurrences.
          * `{n,m}`: Matches between `n` and `m` (inclusive) occurrences.
  * **Escaped Special Characters**: Handles matching of special regex characters as literals (e.g., `\.` to match a literal dot, `\*` to match a literal asterisk).
  * **Robust Command-Line Interface (CLI)**: Provides a user-friendly interface for performing pattern searches against direct input strings or by processing content from specified files.
  * **Comprehensive Unit Testing**: Supported by a rigorous test suite using `pytest` and `unittest`, ensuring reliability and validating the engine's behavior across diverse scenarios, including complex patterns and edge cases.

-----

## 📁 Project Structure

The project maintains a well-defined and modular directory structure, promoting code readability and maintainability:

```
line-watch/
├── .github/
│   └── workflows/
│       └── security.yml       # GitHub Actions workflow for automated security analysis and CI/CD
├── line_watch/
│   ├── __init__.py            # Python package initialization file
│   ├── cli.py                 # Command-Line Interface (CLI) implementation
│   ├── engine.py              # Core Regular Expression Engine: contains parsing and matching logic
│   └── utils.py               # Utility functions, including character check helpers and regex component parsing
├── tests/
│   ├── __init__.py
│   └── test_engine.py         # Comprehensive unit tests for the regex engine and utility functions
├── .gitignore                 # Specifies files and directories to be excluded from version control
├── LICENSE                    # Project licensing information (MIT License)
├── pyproject.toml             # Project metadata, build configuration, and command-line entry point (PEP 517/621 standard)
└── README.md                  # This project documentation file
```

-----

## ⚙️ Setup and Installation

To set up and run Line-watch on your local machine, follow these instructions:

1.  **Clone the Repository**:
    Begin by cloning the project repository:

    ```bash
    git clone https://github.com/SREEHARI-M-S/line-watch.git
    cd line-watch
    ```

2.  **Create and Activate a Virtual Environment (Recommended)**:
    It's good practice to use a virtual environment for dependency management, ensuring project isolation.

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: `venv\Scripts\activate`
    ```

3.  **Install Project Package**:
    Install Line-watch as an editable package. This allows you to run the `lw` command directly from your terminal and ensures any changes you make to the source code are immediately reflected.

    ```bash
    pip install -e .
    ```

    This command will also install `pytest`, which is used for testing.

-----

## 🚀 Usage Guide

The `lw` CLI utility provides a streamlined interface for pattern matching.

### Command Syntax

The general command structure is:

```bash
lw <regex_pattern> [-f <filename> | -s <string_to_match>]
```

  * `<regex_pattern>`: The regular expression pattern you wish to match.
  * `-f <filename>` / `--file <filename>`: Specify a file path. Line-watch will search for the pattern within each line of this file.
  * `-s <string_to_match>` / `--string <string_to_match>`: Provide a direct string to match against. This is suitable for single-line pattern checks.
  * **No arguments provided for `-f` or `-s`**: If neither `-f` nor `-s` is specified, `lw` will read input line by line from standard input (stdin).

### Practical Examples

1.  **Matching a Pattern Against a Direct String Input (`-s`)**:

    ```bash
    lw "hello" -s "This is a hello world string."
    # Output: ✅ Matched: 'This is a hello world string.' with pattern 'hello'

    lw "^start" -s "The line starts here."
    # Output: ❌ Not Matched: 'The line starts here.' with pattern '^start'
    ```

2.  **Utilizing Character Classes**:

    ```bash
    lw "id\\d+" -s "User ID12345"
    # Output: ✅ Matched: 'User ID12345' with pattern 'id\d+'

    lw "func_\\w+" -s "Calling func_initialize."
    # Output: ✅ Matched: 'Calling func_initialize.' with pattern 'func_\w+'
    ```

3.  **Employing Character Sets and Ranges**:

    ```bash
    lw "[aeiou]pple" -s "apple"
    # Output: ✅ Matched: 'apple' with pattern '[aeiou]pple'

    lw "[A-Z0-9]{3}" -s "ABCDEF"
    # Output: ✅ Matched: 'ABCDEF' with pattern '[A-Z0-9]{3}'
    ```

4.  **Demonstrating Quantifiers (`*`, `+`, `?`, `{n,m}`)**:

    ```bash
    lw "colou?r" -s "colour"
    # Output: ✅ Matched: 'colour' with pattern 'colou?r'

    lw "a{2,4}b" -s "aaab"
    # Output: ✅ Matched: 'aaab' with pattern 'a{2,4}b'

    lw "X.*Y" -s "This is XcontentY within text."
    # Output: ✅ Matched: 'This is XcontentY within text.' with pattern 'X.*Y'
    ```

5.  **Processing Patterns Against a File (`-f`)**:
    First, create a sample `data.log` file:

    ```bash
    echo "INFO: Application started." > data.log
    echo "DEBUG: Variable x = 10." >> data.log
    echo "ERROR: File not found in /path/to/data." >> data.log
    echo "WARNING: Disk space low (20GB left)." >> data.log
    ```

    Then, execute Line-watch:

    ```bash
    lw "^ERROR:" -f data.log
    # Output:
    # ✅ Line 3: ERROR: File not found in /path/to/data.

    lw "\\d+GB" -f data.log
    # Output:
    # ✅ Line 4: WARNING: Disk space low (20GB left).
    ```

6.  **Reading Input from Standard Input (stdin)**:
    If neither `-f` nor `-s` is provided, `lw` will read lines from standard input until an End-of-File (EOF) signal is received (`Ctrl+D` on Unix/macOS, `Ctrl+Z` then `Enter` on Windows).

    ```bash
    lw "keyword"
    # Output:
    # Enter text to match (Ctrl+D or Ctrl+Z to finish input):
    # This line contains a keyword.
    # ✅ Line 1: This line contains a keyword.
    # Another line without the word.
    # Final keyword test.
    # ✅ Line 3: Final keyword test.
    # (Press Ctrl+D or Ctrl+Z then Enter to finish input)
    # ❌ No matches found. (If no matches were found overall)
    ```

-----

## 🧪 Testing

A comprehensive suite of unit tests is included to ensure the integrity, accuracy, and reliability of the regex engine's behavior across various scenarios.

To execute the test suite:

1.  Navigate to the project's root directory in your terminal.
2.  Ensure `pytest` is installed (it should be if you installed with `pip install -e .`).
3.  Run the tests using the `pytest` command:
    ```bash
    pytest
    ```
    A successful execution will indicate that all tests have passed, confirming the engine's functionality across a wide range of regex constructs and edge cases.

-----

## 📈 Future Development & Roadmap

While Line-watch currently offers robust functionality for fundamental regex operations, the domain of regular expressions is expansive. Future enhancements I'm considering include:

  * **Performance Optimizations**:
      * **NFA to DFA Conversion**: Investigating and implementing algorithms to convert the NFA-based matching to a Deterministic Finite Automaton (DFA) for potentially superior performance and more predictable matching times, particularly with complex or pathological regexes.
      * **Optimized NFA Simulation**: Exploring and integrating more advanced NFA simulation techniques that can significantly reduce redundant backtracking and improve overall efficiency.
  * **Advanced Regex Constructs**:
      * **Capturing Groups (`()`)**: Extending functionality to capture and extract specific matched substrings for further processing.
      * **Alternation (`|`)**: Implementing "OR" logic within patterns (e.g., `(cat|dog)`).
      * **Non-greedy Quantifiers (`*?`, `+?`, `??`, `{n,m}?`)**: Introducing support for matching the shortest possible string segment that satisfies the pattern.
      * **Lookaheads and Lookbehinds**: Implementing zero-width assertions that assert conditions about what follows or precedes the current matching position without consuming characters.
      * **Word Boundaries (`\b`, `\B`)**: For precise matching at word edges.
      * **Whitespace Classes (`\s`, `\S`)**: For matching any whitespace character or non-whitespace character, respectively.
  * **Enhanced Error Handling and Reporting**: Developing more granular, specific, and user-friendly error messages for syntactically incorrect or malformed regex patterns.
  * **Formal Parser Implementation**: Transitioning to a more structured regex parser, potentially incorporating a dedicated lexer (tokenizer) and an Abstract Syntax Tree (AST) builder, to enhance extensibility, maintainability, and improve error recovery mechanisms.
  * **Full Unicode Support**: Expanding character matching and character class definitions to fully support the vast Unicode character set, enabling global application.

-----

## 🤝 Contribution Guidelines

I welcome and value contributions to the Line-watch project\! Your insights and expertise can significantly help improve it. To contribute effectively, please adhere to the following guidelines:

1.  **Fork the repository** on GitHub.
2.  **Create a new branch** for your feature or bug fix. Use descriptive names like `feature/add-alternation-operator` or `bugfix/resolve-anchor-issue`.
    ```bash
    git checkout -b feature/your-feature-name
    ```
3.  **Implement your changes**, ensuring they align with the project's architectural principles and coding style.
4.  **Write comprehensive unit tests** for any new functionality or bug fixes. This is crucial for maintaining the project's stability and reliability.
5.  **Commit your changes** with a clear, concise, and descriptive commit message. Follow conventional commit guidelines where applicable (e.g., `feat: Add new feature X`, `fix: Resolve issue with nested quantifiers`).
6.  **Push your branch** to your forked repository:
    ```bash
    git push origin feature/your-feature-name
    ```
7.  **Open a Pull Request (PR)** against the `main` branch of the original repository. Provide a detailed description of your changes, their rationale, and any relevant test results.

Before submitting a Pull Request, please ensure your code adheres to Python's best practices and successfully passes all existing tests.

-----

## 📜 License

This project is open-source and distributed under the terms of the **MIT License**. A copy of the license is available in the [LICENSE](https://github.com/SREEHARI-M-S/line-watch/blob/main/LICENSE) file within the repository.

-----