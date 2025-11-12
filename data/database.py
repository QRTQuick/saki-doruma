"""
Database management for expense data persistence.
"""

import json
import os
from datetime import datetime
from typing import List, Optional
from pathlib import Path
from .models import Expense, ExpenseReport, ExpenseCategory, PaymentMethod


class DatabaseManager:
    """Manages persistence of expense data to JSON files."""

    def __init__(self, data_dir: str = "data/storage"):
        """Initialize database manager."""
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.expenses_file = self.data_dir / "expenses.json"
        self.reports_file = self.data_dir / "reports.json"
        self._initialize_files()

    def _initialize_files(self) -> None:
        """Create JSON files if they don't exist."""
        if not self.expenses_file.exists():
            self._save_json(self.expenses_file, [])
        if not self.reports_file.exists():
            self._save_json(self.reports_file, [])

    def _save_json(self, filepath: Path, data: any) -> None:
        """Save data to JSON file."""
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2, default=str)

    def _load_json(self, filepath: Path) -> any:
        """Load data from JSON file."""
        if not filepath.exists():
            return None
        with open(filepath, 'r') as f:
            return json.load(f)

    def save_expense(self, expense: Expense) -> bool:
        """Save or update an expense."""
        try:
            expenses = self._load_json(self.expenses_file) or []
            expense_dict = expense.to_dict()

            # Check if expense exists and update
            existing_idx = next((i for i, e in enumerate(expenses) if e['id'] == expense.id), None)
            if existing_idx is not None:
                expenses[existing_idx] = expense_dict
            else:
                expenses.append(expense_dict)

            self._save_json(self.expenses_file, expenses)
            return True
        except Exception as e:
            print(f"Error saving expense: {e}")
            return False

    def get_expenses(self, category: Optional[ExpenseCategory] = None) -> List[dict]:
        """Get all expenses or filter by category."""
        expenses = self._load_json(self.expenses_file) or []
        if category:
            expenses = [e for e in expenses if e['category'] == category.value]
        return expenses

    def get_expense_by_id(self, expense_id: str) -> Optional[dict]:
        """Get expense by ID."""
        expenses = self._load_json(self.expenses_file) or []
        return next((e for e in expenses if e['id'] == expense_id), None)

    def delete_expense(self, expense_id: str) -> bool:
        """Delete an expense."""
        try:
            expenses = self._load_json(self.expenses_file) or []
            expenses = [e for e in expenses if e['id'] != expense_id]
            self._save_json(self.expenses_file, expenses)
            return True
        except Exception as e:
            print(f"Error deleting expense: {e}")
            return False

    def get_expenses_by_date_range(self, start_date: datetime, end_date: datetime) -> List[dict]:
        """Get expenses within date range."""
        expenses = self._load_json(self.expenses_file) or []
        filtered = []
        for expense in expenses:
            exp_date = datetime.fromisoformat(expense['date'])
            if start_date <= exp_date <= end_date:
                filtered.append(expense)
        return filtered

    def save_report(self, report: ExpenseReport) -> bool:
        """Save or update a report."""
        try:
            reports = self._load_json(self.reports_file) or []
            report_dict = {
                'report_id': report.report_id,
                'title': report.title,
                'start_date': report.start_date.isoformat(),
                'end_date': report.end_date.isoformat(),
                'expenses': [e.to_dict() for e in report.expenses],
                'notes': report.notes,
                'created_at': report.created_at.isoformat(),
            }

            existing_idx = next((i for i, r in enumerate(reports) if r['report_id'] == report.report_id), None)
            if existing_idx is not None:
                reports[existing_idx] = report_dict
            else:
                reports.append(report_dict)

            self._save_json(self.reports_file, reports)
            return True
        except Exception as e:
            print(f"Error saving report: {e}")
            return False

    def get_reports(self) -> List[dict]:
        """Get all reports."""
        return self._load_json(self.reports_file) or []

    def delete_report(self, report_id: str) -> bool:
        """Delete a report."""
        try:
            reports = self._load_json(self.reports_file) or []
            reports = [r for r in reports if r['report_id'] != report_id]
            self._save_json(self.reports_file, reports)
            return True
        except Exception as e:
            print(f"Error deleting report: {e}")
            return False

    def export_expenses_csv(self, filepath: str, expenses: Optional[List[dict]] = None) -> bool:
        """Export expenses to CSV file."""
        try:
            import csv
            expenses = expenses or self.get_expenses()
            if not expenses:
                return False

            with open(filepath, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=expenses[0].keys())
                writer.writeheader()
                writer.writerows(expenses)
            return True
        except Exception as e:
            print(f"Error exporting to CSV: {e}")
            return False
