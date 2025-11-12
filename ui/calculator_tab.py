"""
Calculator tab for the application.
"""

from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel,
                               QPushButton, QLineEdit, QComboBox, QDoubleSpinBox,
                               QTableWidget, QTableWidgetItem, QTabWidget, QGroupBox)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from modules.calculator import MiniCalculator, AccountingCalculator


class CalculatorTab(QWidget):
    """Tab for calculator and accounting functions."""

    def __init__(self, parent=None):
        """Initialize calculator tab."""
        super().__init__(parent)
        self.calculator = MiniCalculator()
        self.accounting_calc = AccountingCalculator()
        self.init_ui()

    def init_ui(self) -> None:
        """Initialize UI components."""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(12)

        # Create tab widget for different calculators
        calc_tabs = QTabWidget()

        # Mini Calculator Tab
        mini_calc_widget = self._create_mini_calculator()
        calc_tabs.addTab(mini_calc_widget, "Basic Calculator")

        # Accounting Tools Tab
        accounting_widget = self._create_accounting_tools()
        calc_tabs.addTab(accounting_widget, "Accounting Tools")

        layout.addWidget(calc_tabs)

    def _create_mini_calculator(self) -> QWidget:
        """Create mini calculator interface."""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setSpacing(12)

        # Display
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        font = QFont()
        font.setPointSize(14)
        self.display.setFont(font)
        layout.addWidget(self.display)

        # Input layout
        input_layout = QHBoxLayout()
        input_label = QLabel("Expression:")
        self.expr_input = QLineEdit()
        self.expr_input.setPlaceholderText("e.g., 100 * 1.2 + 50")
        input_layout.addWidget(input_label)
        input_layout.addWidget(self.expr_input)
        layout.addLayout(input_layout)

        # Buttons layout
        button_layout = QHBoxLayout()
        
        calc_button = QPushButton("Calculate")
        calc_button.setObjectName("addButton")
        calc_button.clicked.connect(self._on_calculate)
        button_layout.addWidget(calc_button)

        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self._on_clear_calc)
        button_layout.addWidget(clear_button)

        clear_hist_button = QPushButton("Clear History")
        clear_hist_button.clicked.connect(self._on_clear_history)
        button_layout.addWidget(clear_hist_button)

        layout.addLayout(button_layout)

        # History
        history_label = QLabel("History:")
        layout.addWidget(history_label)

        self.history_table = QTableWidget()
        self.history_table.setColumnCount(1)
        self.history_table.setHorizontalHeaderLabels(["Calculation"])
        self.history_table.setMaximumHeight(150)
        layout.addWidget(self.history_table)

        layout.addStretch()
        return widget

    def _create_accounting_tools(self) -> QWidget:
        """Create accounting tools interface."""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setSpacing(12)

        # Create accounting tabs
        acc_tabs = QTabWidget()

        # VAT Calculator
        vat_widget = self._create_vat_calculator()
        acc_tabs.addTab(vat_widget, "VAT Calculator")

        # Tax Calculator
        tax_widget = self._create_tax_calculator()
        acc_tabs.addTab(tax_widget, "Tax Calculator")

        # Discount Calculator
        discount_widget = self._create_discount_calculator()
        acc_tabs.addTab(discount_widget, "Discount Calculator")

        # Markup Calculator
        markup_widget = self._create_markup_calculator()
        acc_tabs.addTab(markup_widget, "Markup Calculator")

        # Profit Margin
        margin_widget = self._create_profit_margin()
        acc_tabs.addTab(margin_widget, "Profit Margin")

        # Break Even
        breakeven_widget = self._create_break_even()
        acc_tabs.addTab(breakeven_widget, "Break-Even")

        # Interest Calculator
        interest_widget = self._create_interest_calculator()
        acc_tabs.addTab(interest_widget, "Interest Calculator")

        layout.addWidget(acc_tabs)
        return widget

    def _create_vat_calculator(self) -> QWidget:
        """Create VAT calculator."""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setSpacing(10)

        # Base Amount
        amount_layout = QHBoxLayout()
        amount_layout.addWidget(QLabel("Base Amount:"))
        self.vat_amount = QDoubleSpinBox()
        self.vat_amount.setRange(0, 999999.99)
        self.vat_amount.setDecimals(2)
        amount_layout.addWidget(self.vat_amount)
        layout.addLayout(amount_layout)

        # VAT Rate
        rate_layout = QHBoxLayout()
        rate_layout.addWidget(QLabel("VAT Rate (%):"))
        self.vat_rate = QDoubleSpinBox()
        self.vat_rate.setValue(20)
        self.vat_rate.setRange(0, 100)
        rate_layout.addWidget(self.vat_rate)
        layout.addLayout(rate_layout)

        # Calculate button
        calc_btn = QPushButton("Calculate VAT")
        calc_btn.setObjectName("addButton")
        calc_btn.clicked.connect(self._on_calculate_vat)
        layout.addWidget(calc_btn)

        # Results
        self.vat_results = QLineEdit()
        self.vat_results.setReadOnly(True)
        layout.addWidget(QLabel("Results:"))
        layout.addWidget(self.vat_results)

        layout.addStretch()
        return widget

    def _create_tax_calculator(self) -> QWidget:
        """Create tax calculator."""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setSpacing(10)

        amount_layout = QHBoxLayout()
        amount_layout.addWidget(QLabel("Gross Amount:"))
        self.tax_amount = QDoubleSpinBox()
        self.tax_amount.setRange(0, 999999.99)
        self.tax_amount.setDecimals(2)
        amount_layout.addWidget(self.tax_amount)
        layout.addLayout(amount_layout)

        rate_layout = QHBoxLayout()
        rate_layout.addWidget(QLabel("Tax Rate (%):"))
        self.tax_rate = QDoubleSpinBox()
        self.tax_rate.setValue(15)
        self.tax_rate.setRange(0, 100)
        rate_layout.addWidget(self.tax_rate)
        layout.addLayout(rate_layout)

        calc_btn = QPushButton("Calculate Tax")
        calc_btn.setObjectName("addButton")
        calc_btn.clicked.connect(self._on_calculate_tax)
        layout.addWidget(calc_btn)

        self.tax_results = QLineEdit()
        self.tax_results.setReadOnly(True)
        layout.addWidget(QLabel("Results:"))
        layout.addWidget(self.tax_results)

        layout.addStretch()
        return widget

    def _create_discount_calculator(self) -> QWidget:
        """Create discount calculator."""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setSpacing(10)

        amount_layout = QHBoxLayout()
        amount_layout.addWidget(QLabel("Original Amount:"))
        self.disc_amount = QDoubleSpinBox()
        self.disc_amount.setRange(0, 999999.99)
        self.disc_amount.setDecimals(2)
        amount_layout.addWidget(self.disc_amount)
        layout.addLayout(amount_layout)

        percent_layout = QHBoxLayout()
        percent_layout.addWidget(QLabel("Discount (%):"))
        self.disc_percent = QDoubleSpinBox()
        self.disc_percent.setRange(0, 100)
        percent_layout.addWidget(self.disc_percent)
        layout.addLayout(percent_layout)

        calc_btn = QPushButton("Calculate Discount")
        calc_btn.setObjectName("addButton")
        calc_btn.clicked.connect(self._on_calculate_discount)
        layout.addWidget(calc_btn)

        self.disc_results = QLineEdit()
        self.disc_results.setReadOnly(True)
        layout.addWidget(QLabel("Results:"))
        layout.addWidget(self.disc_results)

        layout.addStretch()
        return widget

    def _create_markup_calculator(self) -> QWidget:
        """Create markup calculator."""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setSpacing(10)

        cost_layout = QHBoxLayout()
        cost_layout.addWidget(QLabel("Cost:"))
        self.markup_cost = QDoubleSpinBox()
        self.markup_cost.setRange(0, 999999.99)
        self.markup_cost.setDecimals(2)
        cost_layout.addWidget(self.markup_cost)
        layout.addLayout(cost_layout)

        percent_layout = QHBoxLayout()
        percent_layout.addWidget(QLabel("Markup (%):"))
        self.markup_percent = QDoubleSpinBox()
        self.markup_percent.setRange(0, 100)
        percent_layout.addWidget(self.markup_percent)
        layout.addLayout(percent_layout)

        calc_btn = QPushButton("Calculate Markup")
        calc_btn.setObjectName("addButton")
        calc_btn.clicked.connect(self._on_calculate_markup)
        layout.addWidget(calc_btn)

        self.markup_results = QLineEdit()
        self.markup_results.setReadOnly(True)
        layout.addWidget(QLabel("Results:"))
        layout.addWidget(self.markup_results)

        layout.addStretch()
        return widget

    def _create_profit_margin(self) -> QWidget:
        """Create profit margin calculator."""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setSpacing(10)

        rev_layout = QHBoxLayout()
        rev_layout.addWidget(QLabel("Revenue:"))
        self.margin_revenue = QDoubleSpinBox()
        self.margin_revenue.setRange(0, 999999.99)
        self.margin_revenue.setDecimals(2)
        rev_layout.addWidget(self.margin_revenue)
        layout.addLayout(rev_layout)

        cost_layout = QHBoxLayout()
        cost_layout.addWidget(QLabel("Cost:"))
        self.margin_cost = QDoubleSpinBox()
        self.margin_cost.setRange(0, 999999.99)
        self.margin_cost.setDecimals(2)
        cost_layout.addWidget(self.margin_cost)
        layout.addLayout(cost_layout)

        calc_btn = QPushButton("Calculate Margin")
        calc_btn.setObjectName("addButton")
        calc_btn.clicked.connect(self._on_calculate_margin)
        layout.addWidget(calc_btn)

        self.margin_results = QLineEdit()
        self.margin_results.setReadOnly(True)
        layout.addWidget(QLabel("Results:"))
        layout.addWidget(self.margin_results)

        layout.addStretch()
        return widget

    def _create_break_even(self) -> QWidget:
        """Create break-even calculator."""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setSpacing(10)

        fixed_layout = QHBoxLayout()
        fixed_layout.addWidget(QLabel("Fixed Costs:"))
        self.be_fixed = QDoubleSpinBox()
        self.be_fixed.setRange(0, 999999.99)
        self.be_fixed.setDecimals(2)
        fixed_layout.addWidget(self.be_fixed)
        layout.addLayout(fixed_layout)

        price_layout = QHBoxLayout()
        price_layout.addWidget(QLabel("Unit Price:"))
        self.be_price = QDoubleSpinBox()
        self.be_price.setRange(0, 999999.99)
        self.be_price.setDecimals(2)
        price_layout.addWidget(self.be_price)
        layout.addLayout(price_layout)

        cost_layout = QHBoxLayout()
        cost_layout.addWidget(QLabel("Unit Cost:"))
        self.be_cost = QDoubleSpinBox()
        self.be_cost.setRange(0, 999999.99)
        self.be_cost.setDecimals(2)
        cost_layout.addWidget(self.be_cost)
        layout.addLayout(cost_layout)

        calc_btn = QPushButton("Calculate Break-Even")
        calc_btn.setObjectName("addButton")
        calc_btn.clicked.connect(self._on_calculate_breakeven)
        layout.addWidget(calc_btn)

        self.be_results = QLineEdit()
        self.be_results.setReadOnly(True)
        layout.addWidget(QLabel("Results:"))
        layout.addWidget(self.be_results)

        layout.addStretch()
        return widget

    def _create_interest_calculator(self) -> QWidget:
        """Create interest calculator."""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setSpacing(10)

        principal_layout = QHBoxLayout()
        principal_layout.addWidget(QLabel("Principal:"))
        self.int_principal = QDoubleSpinBox()
        self.int_principal.setRange(0, 999999.99)
        self.int_principal.setDecimals(2)
        principal_layout.addWidget(self.int_principal)
        layout.addLayout(principal_layout)

        rate_layout = QHBoxLayout()
        rate_layout.addWidget(QLabel("Rate (%):"))
        self.int_rate = QDoubleSpinBox()
        self.int_rate.setRange(0, 100)
        self.int_rate.setDecimals(2)
        rate_layout.addWidget(self.int_rate)
        layout.addLayout(rate_layout)

        time_layout = QHBoxLayout()
        time_layout.addWidget(QLabel("Time (Years):"))
        self.int_time = QDoubleSpinBox()
        self.int_time.setRange(0, 100)
        self.int_time.setDecimals(2)
        time_layout.addWidget(self.int_time)
        layout.addLayout(time_layout)

        type_layout = QHBoxLayout()
        type_layout.addWidget(QLabel("Type:"))
        self.int_type = QComboBox()
        self.int_type.addItems(["Simple Interest", "Compound Interest"])
        type_layout.addWidget(self.int_type)
        layout.addLayout(type_layout)

        calc_btn = QPushButton("Calculate Interest")
        calc_btn.setObjectName("addButton")
        calc_btn.clicked.connect(self._on_calculate_interest)
        layout.addWidget(calc_btn)

        self.int_results = QLineEdit()
        self.int_results.setReadOnly(True)
        layout.addWidget(QLabel("Results:"))
        layout.addWidget(self.int_results)

        layout.addStretch()
        return widget

    def _on_calculate(self) -> None:
        """Handle basic calculator calculation."""
        expr = self.expr_input.text()
        result = self.calculator.evaluate(expr)
        self.display.setText(str(result))
        self._update_history()

    def _on_clear_calc(self) -> None:
        """Clear calculator."""
        self.expr_input.clear()
        self.display.clear()

    def _on_clear_history(self) -> None:
        """Clear calculation history."""
        self.calculator.clear_history()
        self._update_history()

    def _update_history(self) -> None:
        """Update history table."""
        self.history_table.setRowCount(0)
        for calc in self.calculator.get_history():
            row = self.history_table.rowCount()
            self.history_table.insertRow(row)
            self.history_table.setItem(row, 0, QTableWidgetItem(calc))

    def _on_calculate_vat(self) -> None:
        """Calculate VAT."""
        result = self.accounting_calc.calculate_vat(
            self.vat_amount.value(),
            self.vat_rate.value()
        )
        text = f"Base: ${result['base_amount']:.2f} | VAT: ${result['vat_amount']:.2f} | Total: ${result['total']:.2f}"
        self.vat_results.setText(text)

    def _on_calculate_tax(self) -> None:
        """Calculate tax."""
        result = self.accounting_calc.calculate_tax(
            self.tax_amount.value(),
            self.tax_rate.value()
        )
        text = f"Gross: ${result['gross_amount']:.2f} | Tax: ${result['tax_amount']:.2f} | Net: ${result['net_amount']:.2f}"
        self.tax_results.setText(text)

    def _on_calculate_discount(self) -> None:
        """Calculate discount."""
        result = self.accounting_calc.calculate_discount(
            self.disc_amount.value(),
            self.disc_percent.value()
        )
        text = f"Original: ${result['original_amount']:.2f} | Discount: ${result['discount_amount']:.2f} | Final: ${result['final_amount']:.2f}"
        self.disc_results.setText(text)

    def _on_calculate_markup(self) -> None:
        """Calculate markup."""
        result = self.accounting_calc.calculate_markup(
            self.markup_cost.value(),
            self.markup_percent.value()
        )
        text = f"Cost: ${result['cost']:.2f} | Markup: ${result['markup_amount']:.2f} | Price: ${result['selling_price']:.2f}"
        self.markup_results.setText(text)

    def _on_calculate_margin(self) -> None:
        """Calculate profit margin."""
        result = self.accounting_calc.calculate_profit_margin(
            self.margin_revenue.value(),
            self.margin_cost.value()
        )
        text = f"Revenue: ${result['revenue']:.2f} | Profit: ${result['profit']:.2f} | Margin: {result['margin_percent']:.2f}%"
        self.margin_results.setText(text)

    def _on_calculate_breakeven(self) -> None:
        """Calculate break-even."""
        result = self.accounting_calc.calculate_break_even(
            self.be_fixed.value(),
            self.be_price.value(),
            self.be_cost.value()
        )
        if 'error' in result:
            self.be_results.setText(result['error'])
        else:
            text = f"Units: {result['break_even_units']:.0f} | Revenue: ${result['break_even_revenue']:.2f}"
            self.be_results.setText(text)

    def _on_calculate_interest(self) -> None:
        """Calculate interest."""
        principal = self.int_principal.value()
        rate = self.int_rate.value()
        time = self.int_time.value()

        if self.int_type.currentText() == "Simple Interest":
            result = self.accounting_calc.calculate_simple_interest(principal, rate, time)
        else:
            result = self.accounting_calc.calculate_compound_interest(principal, rate, time)

        text = f"Principal: ${result['principal']:.2f} | Interest: ${result['interest']:.2f} | Total: ${result['total_amount']:.2f}"
        self.int_results.setText(text)
