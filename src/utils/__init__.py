"""
This module provides utility functions related to the console.

Modules:
- `clear_console`: Clears the terminal screen on both Windows and Unix-based systems.
"""

from .console import clear_console
from .notifications import send_notification

__all__ = ['clear_console', 'send_notification']
