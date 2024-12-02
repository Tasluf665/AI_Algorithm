# AI_Algorithm

This repository contains the implementation of the Depth-First Search (DFS), Breadth-First Search (BFS), Best-First Search (BFS) and A* Search algorithm using the `pyMaze` library.

## Problem in MacOS and Solution

When running the script, you may encounter the following error:

```
File "/Users/AI_Algorithm/DFS.py", line 1, in <module>
    from pyMaze import maze, agent, COLOR, textLabel
  File "/Users/AI_Algorithm/pyMaze.py", line 26, in <module>
    from tkinter import *
  File "/opt/homebrew/Cellar/python@3.13/3.13.0_1/Frameworks/Python.framework/Versions/3.13/lib/python3.13/tkinter/__init__.py", line 38, in <module>
    import _tkinter # If this fails your Python may not be configured for Tk
    ^^^^^^^^^^^^^^^
```

This error occurs because the `tkinter` module, required for `pyMaze`, is not properly configured in your Python installation.

## Solution

Follow these steps to resolve the issue:

### Step 1: Verify `tkinter` Installation
Run the following command to check if `tkinter` is installed and functional:
```bash
python3 -m tkinter
```
If a small GUI window opens, `tkinter` is installed and working. If you see an error, proceed to the next step.

### Step 2: Install `tkinter` for Python
If you installed Python using Homebrew, use the following command to install `tkinter`:
```bash
brew install python-tk
```

If the issue persists, ensure that your Python version is correctly linked to the `tkinter` installation. You may also need to reinstall Python with GUI support:
```bash
brew reinstall python
```
