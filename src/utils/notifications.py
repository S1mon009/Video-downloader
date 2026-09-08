"""
Send desktop notifications across Linux, macOS, and Widnows.
This snippet uses the plyer library for cross platform support
"""
from plyer import notification

def send_notification(title: str, message: str, timeout: int = 5) -> None:
    """
    Show system notification.
    
    Args:
        title: Notification title.
        message: Notification body.
        timeout: Duration in seconds (may vary bt OS).
    
    Return:
        None
    """
    if not title.strip():
        raise ValueError("Notification title cannot be empty")
    if not message.strip():
        raise ValueError("Notification message cannot be empty")
    
    notification.notify(
        title=title,
        message=message,
        timeout=timeout
    )