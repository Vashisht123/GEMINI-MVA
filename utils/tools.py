"""
Utility tools for common helper operations.
"""

import re
import datetime

def extract_dates(text):
    """Extract date-like words"""
    words = text.split()
    return [w for w in words if re.search(r"\\d{4}|today|tomorrow", w.lower())]

def current_time():
    """Return current timestamp string"""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def clean_text(text):
    """Normalize whitespace"""
    return " ".join(text.split())
