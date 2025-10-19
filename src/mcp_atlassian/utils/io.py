"""I/O utility functions for MCP Atlassian."""

from mcp_atlassian.utils.env import is_env_extended_truthy


def is_read_only_mode() -> bool:
    """Check if the server is running in read-only mode.

    Read-only mode prevents all write operations (create, update, delete)
    while allowing all read operations. This is useful for working with
    production Atlassian instances where you want to prevent accidental
    modifications.

    Returns:
        True if read-only mode is enabled, False otherwise
    """
    return is_env_extended_truthy("READ_ONLY_MODE", "false")


def should_ignore_comment_limit() -> bool:
    """Return True when comment limits should be ignored for Jira issues.

    Controlled via the IGNORE_COMMENT_LIMIT environment variable. Accepts
    the same truthy values as other boolean env flags ("true", "1", "yes",
    "y", "on"), case-insensitive.

    Returns:
        True if all comments should be retrieved, False otherwise.
    """
    return is_env_extended_truthy("IGNORE_COMMENT_LIMIT", "false")
