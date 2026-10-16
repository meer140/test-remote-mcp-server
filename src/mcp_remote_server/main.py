from fastmcp import FastMCP
import random

mcp = FastMCP("Simple Calculator")

@mcp.tool
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b

@mcp.tool
def generate_random_number(min_value: int =1, max_value: int = 100) -> int:
    """Generate a random number between min_value and max_value."""
    return random.randint(min_value, max_value)

if __name__ == "__main__": 
    mcp.run(transport = 'http', host = '0.0.0.0', port = 8000)
    