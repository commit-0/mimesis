"""Import optional dependencies only when needed."""
try:
    import pytz
except ImportError:
    pytz = None