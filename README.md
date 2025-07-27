# 1st-app MCP Server

A Model Context Protocol (MCP) server built with FastMCP 2.0, providing simple utility tools for AI assistants.

**Important notice: UV and pydantic is not working on python 3.14. Need to downgrade to 3.13**

## Features

- **Greeting Tool**: Personalized greetings
- **Math Operations**: Basic arithmetic calculations  
- **App Information**: Server metadata and details

## Quick Start

### Prerequisites

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) package manager

### Installation

```bash
# Clone and navigate to the project
git clone <repository-url>
cd 1st_app

# Install dependencies
uv sync
```

**Note**: On Windows, FastMCP requires Visual Studio Build Tools. Install from [here](https://visualstudio.microsoft.com/visual-cpp-build-tools/) if you encounter build errors.

### Running the Server

```bash
# Run the MCP server
python main.py

# Or activate virtual environment first
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate   # Windows
python main.py
```

## Available Tools

| Tool | Parameters | Description |
|------|------------|-------------|
| `greet` | `name: str` | Returns a personalized greeting |
| `add_numbers` | `a: int, b: int` | Adds two numbers together |
| `get_app_info` | None | Returns server information |

## Usage Examples

When connected to an AI assistant that supports MCP:

```
Assistant: I'll greet you using the MCP server.
> greet("Alice")
"Hello from 1st-app, Alice!"