"""
Analytics and reporting module for expense data insights.
"""

from datetime import datetime, timedelta
from typing import List, Dict, Optional
from data.database import DatabaseManager


class ExpenseAnalytics:
    """Provides analytics and insights on expense data."""

    def __init__(self, db_manager: DatabaseManager):
        """Initialize analytics module."""
        self.db = db_manager

    def get_monthly_trend(self, months: int = 12) -> dict:
        """Get monthly expense trends."""
        trends = {}
        for i in range(months, 0, -1):
            date = datetime.now() - timedelta(days=30*i)
            year, month = date.year, date.month
            month_key = f"{year}-{month:02d}"
            expenses = self.db.get_expenses_by_date_range(
                datetime(year, month, 1),
                datetime(year, month + 1, 1) - timedelta(days=1)
                if month < 12 else datetime(year + 1, 1, 1) - timedelta(days=1)
            )
            trends[month_key] = sum(e['amount'] for e in expenses)
        return trends

    def get_category_distribution(self) -> dict:
        """Get distribution of expenses by category."""
        expenses = self.db.get_expenses()
        distribution = {}
        total = sum(e['amount'] for e in expenses)

        for expense in expenses:
            category = expense['category']
            if category not in distribution:
                distribution[category] = {'amount': 0, 'count': 0}
            distribution[category]['amount'] += expense['amount']
            distribution[category]['count'] += 1

        for category in distribution:
            percentage = (distribution[category]['amount'] / total * 100) if total > 0 else 0
            distribution[category]['percentage'] = round(percentage, 2)

        return distribution

    def get_payment_method_distribution(self) -> dict:
        """Get distribution by payment method."""
        expenses = self.db.get_expenses()
        distribution = {}
        total = sum(e['amount'] for e in expenses)

        for expense in expenses:
            method = expense['payment_method']
            if method not in distribution:
                distribution[method] = {'amount': 0, 'count': 0}
            distribution[method]['amount'] += expense['amount']
            distribution[method]['count'] += 1

        for method in distribution:
            percentage = (distribution[method]['amount'] / total * 100) if total > 0 else 0
            distribution[method]['percentage'] = round(percentage, 2)

        return distribution

    def get_top_expenses(self, limit: int = 10) -> List[dict]:
        """Get top expenses by amount."""
        expenses = self.db.get_expenses()
        sorted_expenses = sorted(expenses, key=lambda x: x['amount'], reverse=True)
        return sorted_expenses[:limit]

    def get_expense_statistics(self) -> dict:
        """Get statistical summary of expenses."""
        expenses = self.db.get_expenses()
        if not expenses:
            return {
                'total': 0,
                'count': 0,
                'average': 0,
                'min': 0,
                'max': 0,
                'median': 0
            }

        amounts = [e['amount'] for e in expenses]
        amounts_sorted = sorted(amounts)
        total = sum(amounts)
        count = len(amounts)
        average = total / count

        # Calculate median
        if count % 2 == 0:
            median = (amounts_sorted[count // 2 - 1] + amounts_sorted[count // 2]) / 2
        else:
            median = amounts_sorted[count // 2]

        return {
            'total': round(total, 2),
            'count': count,
            'average': round(average, 2),
            'min': round(min(amounts), 2),
            'max': round(max(amounts), 2),
            'median': round(median, 2)
        }

    def get_reimbursable_total(self) -> float:
        """Get total reimbursable expenses."""
        expenses = self.db.get_expenses()
        return sum(e['amount'] for e in expenses if e.get('is_reimbursable', False))

    def get_daily_average(self) -> float:
        """Get average daily expense."""
        expenses = self.db.get_expenses()
        if not expenses:
            return 0

        # Calculate date range
        dates = []
        for expense in expenses:
            from datetime import datetime
            date = datetime.fromisoformat(expense['date']).date()
            dates.append(date)

        if not dates:
            return 0

        date_range = (max(dates) - min(dates)).days + 1
        total = sum(e['amount'] for e in expenses)
        return round(total / date_range if date_range > 0 else 0, 2)

    def get_forecast(self, days_ahead: int = 30) -> dict:
        """Simple forecast based on daily average."""
        daily_avg = self.get_daily_average()
        return {
            'days_ahead': days_ahead,
            'daily_average': round(daily_avg, 2),
            'projected_total': round(daily_avg * days_ahead, 2)
        }
