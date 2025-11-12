"""
Data models for expense management and accounting.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional
from enum import Enum


class ExpenseCategory(Enum):
    """Expense categories for organization."""
    TRAVEL = "Travel"
    MEALS = "Meals & Dining"
    SUPPLIES = "Office Supplies"
    EQUIPMENT = "Equipment"
    UTILITIES = "Utilities"
    RENT = "Rent"
    INSURANCE = "Insurance"
    SALARIES = "Salaries"
    MAINTENANCE = "Maintenance"
    MARKETING = "Marketing"
    OTHER = "Other"


class PaymentMethod(Enum):
    """Payment methods for transactions."""
    CASH = "Cash"
    CREDIT_CARD = "Credit Card"
    DEBIT_CARD = "Debit Card"
    BANK_TRANSFER = "Bank Transfer"
    CHECK = "Check"
    OTHER = "Other"


@dataclass
class Expense:
    """Model for individual expense records."""
    id: str
    description: str
    amount: float
    category: ExpenseCategory
    payment_method: PaymentMethod
    date: datetime
    notes: Optional[str] = None
    receipt_path: Optional[str] = None
    is_reimbursable: bool = False
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    def to_dict(self) -> dict:
        """Convert expense to dictionary."""
        return {
            'id': self.id,
            'description': self.description,
            'amount': self.amount,
            'category': self.category.value,
            'payment_method': self.payment_method.value,
            'date': self.date.isoformat(),
            'notes': self.notes,
            'receipt_path': self.receipt_path,
            'is_reimbursable': self.is_reimbursable,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
        }


@dataclass
class ExpenseReport:
    """Model for expense reports and summaries."""
    report_id: str
    title: str
    start_date: datetime
    end_date: datetime
    expenses: List[Expense] = field(default_factory=list)
    notes: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.now)

    def add_expense(self, expense: Expense) -> None:
        """Add expense to report."""
        self.expenses.append(expense)

    def remove_expense(self, expense_id: str) -> None:
        """Remove expense from report by ID."""
        self.expenses = [e for e in self.expenses if e.id != expense_id]

    def get_total(self) -> float:
        """Get total expenses in report."""
        return sum(expense.amount for expense in self.expenses)

    def get_by_category(self) -> dict:
        """Get expenses grouped by category."""
        grouped = {}
        for expense in self.expenses:
            category = expense.category.value
            if category not in grouped:
                grouped[category] = []
            grouped[category].append(expense)
        return grouped

    def get_category_totals(self) -> dict:
        """Get total amount per category."""
        totals = {}
        for category, expenses in self.get_by_category().items():
            totals[category] = sum(e.amount for e in expenses)
        return totals


@dataclass
class Company:
    """Model for company information."""
    name: str
    tax_id: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    fiscal_year_start: int = 1  # Month (1-12)
    currency: str = "USD"
