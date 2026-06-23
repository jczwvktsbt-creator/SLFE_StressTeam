import os
import sys
import webbrowser
import tkinter as tk
from tkinter import messagebox
from pathlib import Path

# =============================================================
#  AUTHORISED USERS
#  Edit this list to add or remove users.
#  Use Windows login username (lowercase).
#  To find a username: open CMD and type:  whoami
#  It shows DOMAIN\john.smith  ->  use  john.smith
# =============================================================
ALLOWED_USERS = [
    "mohammed.ali2",
    "admin",
    "engineer1",
    "engineer2",
    # Add more users below:
    # "firstname.lastname",
    # "john.smith",
]
# =============================================================

# Locate the HTML tool (must be in same folder as this exe)
if getattr(sys, "frozen", False):
    BASE_DIR = Path(sys.executable).parent
else:
    BASE_DIR = Path(__file__).parent

HTML_FILE = BASE_DIR / "piping_loading_tool.html"


def get_windows_username():
    return os.environ.get("USERNAME", "").strip().lower()


def show_access_denied(username):
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    messagebox.showerror(
        "Access Denied",
        f"Access Denied\n\n"
        f"User '{username}' is not authorised to use this tool.\n\n"
        f"Please contact your administrator to request access."
    )
    root.destroy()


def show_error(message):
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    messagebox.showerror("Error", message)
    root.destroy()


def main():
    username = get_windows_username()
    allowed = [u.strip().lower() for u in ALLOWED_USERS]

    if username not in allowed:
        show_access_denied(username or "(unknown)")
        sys.exit(1)

    if not HTML_FILE.exists():
        show_error(
            f"Tool file not found:\n{HTML_FILE}\n\n"
            f"Make sure 'piping_loading_tool.html' is in the same folder as this exe."
        )
        sys.exit(1)

    webbrowser.open(HTML_FILE.as_uri())


if __name__ == "__main__":
    main()
