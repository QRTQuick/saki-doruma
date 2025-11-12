"""
Expense management module.
"""

import uuid
from datetime import datetime, timedelta
from typing import List, Optional
from data.models import Expense, ExpenseReport, ExpenseCategory, PaymentMethod
from data.database import DatabaseManager


class ExpenseManager:
    """Manages expense operations."""

    def __init__(self, db_manager: DatabaseManager):
        """Initialize expense manager."""
        self.db = db_manager

    def create_expense(
        self,
        description: str,
        amount: float,
        category: ExpenseCategory,
        payment_method: PaymentMethod,
        date: Optional[datetime] = None,
        notes: Optional[str] = None,
        receipt_path: Optional[str] = None,
        is_reimbursable: bool = False
    ) -> Expense:
        """Create a new expense."""
        expense = Expense(
            id=str(uuid.uuid4()),
            description=description,
            amount=amount,
            category=category,
            payment_method=payment_method,
            date=date or datetime.now(),
            notes=notes,
            receipt_path=receipt_path,
            is_reimbursable=is_reimbursable
        )
        self.db.save_expense(expense)
        return expense

    def get_all_expenses(self) -> List[dict]:
        """Get all expenses."""
        return self.db.get_expenses()

    def get_expense(self, expense_id: str) -> Optional[dict]:
        """Get expense by ID."""
        return self.db.get_expense_by_id(expense_id)

    def update_expense(self, expense_id: str, **kwargs) -> Optional[Expense]:
        """Update an expense."""
        expense_data = self.db.get_expense_by_id(expense_id)
        if not expense_data:
            return None

        # Update the fields
        for key, value in kwargs.items():
            if key in expense_data:
                expense_data[key] = value
        expense_data['updated_at'] = datetime.now().isoformat()

        # Recreate expense object
        expense = self._dict_to_expense(expense_data)
        self.db.save_expense(expense)
        return expense

    def delete_expense(self, expense_id: str) -> bool:
        """Delete an expense."""
        return self.db.delete_expense(expense_id)

    def get_expenses_by_category(self, category: ExpenseCategory) -> List[dict]:
        """Get expenses by category."""
        return self.db.get_expenses(category)

    def get_expenses_by_date_range(self, start_date: datetime, end_date: datetime) -> List[dict]:
        """Get expenses within date range."""
        return self.db.get_expenses_by_date_range(start_date, end_date)

    def get_expenses_by_month(self, year: int, month: int) -> List[dict]:
        """Get expenses for specific month."""
        start_date = datetime(year, month, 1)
        if month == 12:
            end_date = datetime(year + 1, 1, 1) - timedelta(days=1)
        else:
            end_date = datetime(year, month + 1, 1) - timedelta(days=1)
        return self.get_expenses_by_date_range(start_date, end_date)

    def get_total_expenses(self, expenses: Optional[List[dict]] = None) -> float:
        """Get total of expenses."""
        expenses = expenses or self.get_all_expenses()
        return sum(e['amount'] for e in expenses)

    def get_category_breakdown(self) -> dict:
        """Get expense breakdown by category."""
        expenses = self.get_all_expenses()
        breakdown = {}
        for expense in expenses:
            category = expense['category']
            if category not in breakdown:
                breakdown[category] = {'count': 0, 'total': 0}
            breakdown[category]['count'] += 1
            breakdown[category]['total'] += expense['amount']
        return breakdown

    def get_payment_method_breakdown(self) -> dict:
        """Get expense breakdown by payment method."""
        expenses = self.get_all_expenses()
        breakdown = {}
        for expense in expenses:
            method = expense['payment_method']
            if method not in breakdown:
                breakdown[method] = {'count': 0, 'total': 0}
            breakdown[method]['count'] += 1
            breakdown[method]['total'] += expense['amount']
        return breakdown

    def search_expenses(self, query: str) -> List[dict]:
        """Search expenses by description."""
        expenses = self.get_all_expenses()
        query_lower = query.lower()
        return [e for e in expenses if query_lower in e['description'].lower()]

    def _dict_to_expense(self, data: dict) -> Expense:
        """Convert dictionary to Expense object."""
        return Expense(
            id=data['id'],
            description=data['description'],
            amount=data['amount'],
            category=ExpenseCategory(data['category']),
            payment_method=PaymentMethod(data['payment_method']),
            date=datetime.fromisoformat(data['date']),
            notes=data.get('notes'),
            receipt_path=data.get('receipt_path'),
            is_reimbursable=data.get('is_reimbursable', False),
            created_at=datetime.fromisoformat(data.get('created_at', datetime.now().isoformat())),
            updated_at=datetime.fromisoformat(data.get('updated_at', datetime.now().isoformat()))
        )


class ReportGenerator:
    """Generates expense reports."""

    def __init__(self, db_manager: DatabaseManager):
        """Initialize report generator."""
        self.db = db_manager

    def create_report(
        self,
        title: str,
        start_date: datetime,
        end_date: datetime,
        notes: Optional[str] = None
    ) -> ExpenseReport:
        """Create a new expense report."""
        report = ExpenseReport(
            report_id=str(uuid.uuid4()),
            title=title,
            start_date=start_date,
            end_date=end_date,
            notes=notes
        )

        # Get expenses for date range
        expenses_data = self.db.get_expenses_by_date_range(start_date, end_date)
        for exp_data in expenses_data:
            expense = self._dict_to_expense(exp_data)
            report.add_expense(expense)

        self.db.save_report(report)
        return report

    def get_report_summary(self, report: ExpenseReport) -> dict:
        """Get summary of a report."""
        return {
            'title': report.title,
            'period': f"{report.start_date.date()} to {report.end_date.date()}",
            'total_expenses': report.get_total(),
            'expense_count': len(report.expenses),
            'category_breakdown': report.get_category_totals(),
            'average_expense': report.get_total() / len(report.expenses) if report.expenses else 0
        }

    def _dict_to_expense(self, data: dict) -> Expense:
        """Convert dictionary to Expense object."""
        return Expense(
            id=data['id'],
            description=data['description'],
            amount=data['amount'],
            category=ExpenseCategory(data['category']),
            payment_method=PaymentMethod(data['payment_method']),
            date=datetime.fromisoformat(data['date']),
            notes=data.get('notes'),
            receipt_path=data.get('receipt_path'),
            is_reimbursable=data.get('is_reimbursable', False),
            created_at=datetime.fromisoformat(data.get('created_at', datetime.now().isoformat())),
            updated_at=datetime.fromisoformat(data.get('updated_at', datetime.now().isoformat()))
        )
