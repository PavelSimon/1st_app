# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a minimal Python application called "1st-app" built with modern Python packaging standards. The project uses pyproject.toml for configuration and requires Python 3.14+.

## Development Commands

### Running the Application
```bash
python main.py
```

### Python Environment
- The project requires Python 3.14 or higher
- Uses pyproject.toml for project configuration
- No external dependencies currently defined

## Project Structure

- `main.py` - Entry point with a simple main() function that prints a greeting
- `pyproject.toml` - Project configuration and metadata
- `.gitignore` - Standard Python gitignore excluding __pycache__, build artifacts, and virtual environments

## Architecture Notes

This is a basic Python application with minimal structure. The main functionality is contained in main.py with a standard if __name__ == "__main__" pattern for script execution.