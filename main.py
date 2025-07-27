# MCP Server Implementation
# Note: FastMCP installation requires Windows build tools
# This is a demonstration of the structure

try:
    from fastmcp import FastMCP
    
    # Create MCP server
    mcp = FastMCP("1st-app MCP Server")

    @mcp.tool
    def greet(name: str) -> str:
        """Greet a person by name."""
        return f"Hello from 1st-app, {name}!"

    @mcp.tool
    def add_numbers(a: int, b: int) -> int:
        """Add two numbers together."""
        return a + b

    @mcp.tool
    def get_app_info() -> str:
        """Get information about this application."""
        return "This is the 1st-app MCP server built with FastMCP 2.0"

    def main():
        print("Starting MCP server...")
        mcp.run()

except ImportError:
    print("FastMCP not available. Install it with: uv add fastmcp")
    print("Note: On Windows, you may need Visual Studio Build Tools")
    
    def main():
        print("MCP Server Structure Ready!")
        print("Available tools would be:")
        print("- greet(name: str) -> str")
        print("- add_numbers(a: int, b: int) -> int") 
        print("- get_app_info() -> str")


if __name__ == '__main__':
    mcp.run(transport='stdio')