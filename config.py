"""
Configuration and settings for saki-doruma.
"""

import os
from pathlib import Path

# Application info
APP_NAME = "saki-doruma"
APP_VERSION = "1.0.0"
APP_AUTHOR = "Expense Management Team"

# Paths
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data" / "storage"
LOG_DIR = BASE_DIR / "logs"

# Create directories if they don't exist
DATA_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)

# Database settings
DATABASE_PATH = DATA_DIR / "expenses.json"
REPORTS_PATH = DATA_DIR / "reports.json"

# UI Settings
DARK_MODE = True
DEFAULT_CURRENCY = "USD"
DECIMAL_PLACES = 2

# Expense Settings
DEFAULT_CATEGORY = "Other"
DEFAULT_PAYMENT_METHOD = "Cash"

# Date format
DATE_FORMAT = "%Y-%m-%d"
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

# Export settings
EXPORT_DIR = BASE_DIR / "exports"
EXPORT_DIR.mkdir(parents=True, exist_ok=True)

# Feature flags
ENABLE_RECEIPTS = True
ENABLE_REIMBURSEMENTS = True
ENABLE_ATTACHMENTS = True
