"""
Send desktop notifications across Linux, macOS, and Windows.
This snippet uses the plyer library for cross platform support
"""
from plyer import notification
from pathlib import Path

def send_notification(title: str, message: str, timeout: int = 5) -> None:
    """
    Show system notification.
    
    Args:
        title: Notification title.
        message: Notification body.
        timeout: Duration in seconds (may vary by OS).

    Return:
        None
    """
    if not title.strip():
        raise ValueError("Notification title cannot be empty")
    if not message.strip():
        raise ValueError("Notification message cannot be empty")

    notification.notify(
        app_icon=str(Path(__file__).resolve().parents[2] / "assets" / "icon.ico"),
        title=title,
        message=message,
        timeout=timeout
    )
