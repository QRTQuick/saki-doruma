"""
Mini calculator and accounting utilities module.
"""

import re
from typing import Union


class MiniCalculator:
    """Simple calculator with basic operations."""

    def __init__(self):
        """Initialize calculator."""
        self.history = []
        self.last_result = 0

    def add(self, a: Union[int, float], b: Union[int, float]) -> float:
        """Add two numbers."""
        result = a + b
        self.last_result = result
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a: Union[int, float], b: Union[int, float]) -> float:
        """Subtract two numbers."""
        result = a - b
        self.last_result = result
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a: Union[int, float], b: Union[int, float]) -> float:
        """Multiply two numbers."""
        result = a * b
        self.last_result = result
        self.history.append(f"{a} * {b} = {result}")
        return result

    def divide(self, a: Union[int, float], b: Union[int, float]) -> Union[float, str]:
        """Divide two numbers."""
        if b == 0:
            return "Error: Division by zero"
        result = a / b
        self.last_result = result
        self.history.append(f"{a} / {b} = {result}")
        return result

    def percentage(self, amount: Union[int, float], percent: Union[int, float]) -> float:
        """Calculate percentage of amount."""
        result = (amount * percent) / 100
        self.last_result = result
        self.history.append(f"{percent}% of {amount} = {result}")
        return result

    def evaluate(self, expression: str) -> Union[float, str]:
        """Evaluate mathematical expression."""
        try:
            # Remove spaces and validate
            expression = expression.replace(" ", "")
            # Use eval with restricted namespace for safety
            result = eval(expression, {"__builtins__": {}}, {})
            self.last_result = result
            self.history.append(f"{expression} = {result}")
            return result
        except Exception as e:
            return f"Error: {str(e)}"

    def get_history(self, limit: int = 10) -> list:
        """Get calculation history."""
        return self.history[-limit:]

    def clear_history(self) -> None:
        """Clear calculation history."""
        self.history.clear()
        self.last_result = 0


class AccountingCalculator:
    """Advanced accounting calculations."""

    @staticmethod
    def calculate_vat(amount: float, vat_rate: float) -> dict:
        """Calculate VAT (Value Added Tax)."""
        vat_amount = (amount * vat_rate) / 100
        total = amount + vat_amount
        return {
            'base_amount': amount,
            'vat_rate': vat_rate,
            'vat_amount': round(vat_amount, 2),
            'total': round(total, 2)
        }

    @staticmethod
    def calculate_tax(amount: float, tax_rate: float) -> dict:
        """Calculate tax on amount."""
        tax_amount = (amount * tax_rate) / 100
        net_amount = amount - tax_amount
        return {
            'gross_amount': amount,
            'tax_rate': tax_rate,
            'tax_amount': round(tax_amount, 2),
            'net_amount': round(net_amount, 2)
        }

    @staticmethod
    def calculate_discount(amount: float, discount_percent: float) -> dict:
        """Calculate discount on amount."""
        discount_amount = (amount * discount_percent) / 100
        final_amount = amount - discount_amount
        return {
            'original_amount': amount,
            'discount_percent': discount_percent,
            'discount_amount': round(discount_amount, 2),
            'final_amount': round(final_amount, 2)
        }

    @staticmethod
    def calculate_markup(cost: float, markup_percent: float) -> dict:
        """Calculate markup on cost."""
        markup_amount = (cost * markup_percent) / 100
        selling_price = cost + markup_amount
        return {
            'cost': cost,
            'markup_percent': markup_percent,
            'markup_amount': round(markup_amount, 2),
            'selling_price': round(selling_price, 2)
        }

    @staticmethod
    def calculate_profit_margin(revenue: float, cost: float) -> dict:
        """Calculate profit margin."""
        profit = revenue - cost
        margin_percent = (profit / revenue * 100) if revenue > 0 else 0
        return {
            'revenue': revenue,
            'cost': cost,
            'profit': round(profit, 2),
            'margin_percent': round(margin_percent, 2)
        }

    @staticmethod
    def calculate_break_even(fixed_costs: float, unit_price: float, unit_cost: float) -> dict:
        """Calculate break-even point."""
        if unit_price <= unit_cost:
            return {'error': 'Unit price must be greater than unit cost'}
        contribution_margin = unit_price - unit_cost
        break_even_units = fixed_costs / contribution_margin
        return {
            'fixed_costs': fixed_costs,
            'unit_price': unit_price,
            'unit_cost': unit_cost,
            'break_even_units': round(break_even_units, 2),
            'break_even_revenue': round(break_even_units * unit_price, 2)
        }

    @staticmethod
    def calculate_simple_interest(principal: float, rate: float, time: float) -> dict:
        """Calculate simple interest."""
        interest = (principal * rate * time) / 100
        total_amount = principal + interest
        return {
            'principal': principal,
            'rate': rate,
            'time': time,
            'interest': round(interest, 2),
            'total_amount': round(total_amount, 2)
        }

    @staticmethod
    def calculate_compound_interest(principal: float, rate: float, time: float, compounds: int = 1) -> dict:
        """Calculate compound interest."""
        rate_decimal = rate / 100
        amount = principal * ((1 + rate_decimal / compounds) ** (compounds * time))
        interest = amount - principal
        return {
            'principal': principal,
            'rate': rate,
            'time': time,
            'compounds': compounds,
            'interest': round(interest, 2),
            'total_amount': round(amount, 2)
        }

    @staticmethod
    def average(numbers: list) -> float:
        """Calculate average of numbers."""
        if not numbers:
            return 0
        return sum(numbers) / len(numbers)

    @staticmethod
    def total(numbers: list) -> float:
        """Calculate total of numbers."""
        return sum(numbers)

    @staticmethod
    def percentage_of_total(amount: float, total: float) -> float:
        """Calculate percentage of total."""
        if total == 0:
            return 0
        return (amount / total) * 100
