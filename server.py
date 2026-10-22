
from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    "calculator",
    host="127.0.0.1",
    port=8001,
    streamable_http_path="/mcp",
)


@mcp.tool()
def add(a: float, b: float) -> float:
    print(f"[MCP TOOL CALLED] add(a={a}, b={b})", flush=True)

    result = a + b

    print(f"[MCP TOOL RESULT] add -> {result}", flush=True)
    return result


@mcp.tool()
def subtract(a: float, b: float) -> float:
    print(f"[MCP TOOL CALLED] subtract(a={a}, b={b})", flush=True)

    result = a - b

    print(f"[MCP TOOL RESULT] subtract -> {result}", flush=True)
    return result


@mcp.tool()
def multiply(a: float, b: float) -> float:
    print(f"[MCP TOOL CALLED] multiply(a={a}, b={b})", flush=True)

    result = a * b

    print(f"[MCP TOOL RESULT] multiply -> {result}", flush=True)
    return result


@mcp.tool()
def divide(a: float, b: float) -> float:
    print(f"[MCP TOOL CALLED] divide(a={a}, b={b})", flush=True)

    if b == 0:
        print("[MCP TOOL ERROR] Division by zero", flush=True)
        raise ValueError("Division by zero is not allowed.")

    result = a / b

    print(f"[MCP TOOL RESULT] divide -> {result}", flush=True)
    return result


@mcp.tool()
def validate_call(token: str = "", message: str = "") -> dict:
    print(
        f"[MCP TOOL CALLED] validate_call("
        f"token={token}, message={message})",
        flush=True,
    )

    result = {
        "validated": True,
        "token": token,
        "message": message,
    }

    print(f"[MCP TOOL RESULT] validate_call -> {result}", flush=True)
    return result


if __name__ == "__main__":
    print("[MCP SERVER] Starting on http://127.0.0.1:8001/mcp")
    mcp.run(transport="streamable-http")