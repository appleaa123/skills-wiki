"""Skill: Contributing."""

from fastmcp import FastMCP

mcp = FastMCP("contributing")


_GUIDANCE = {'display_name': 'Contributing', 'description': 'Contributions are welcome:\n\n- **New platform adapters**: Write `platforms.', 'guidance': 'Contributions are welcome:\n\n- **New platform adapters**: Write `platforms.md` adapter configs for other content platforms\n- **Template improvements**: Improve the knowledge distillation template structure\n- **Engine enhancements**: Optimize the saturation assessment model, search term generation strategies\n- **Sub-Skill sharing**: Share your high-quality generated sub-Skills with the community\n\n---'}


@mcp.tool()
def get_guidance() -> dict:
    """Get the full guidance for this skill."""
    return _GUIDANCE
