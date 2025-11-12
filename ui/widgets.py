"""
Widgets for the expense management application.
"""

from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel,
                               QPushButton, QLineEdit, QComboBox, QSpinBox,
                               QDoubleSpinBox, QTableWidget, QTableWidgetItem,
                               QDateEdit, QTextEdit, QFrame, QGroupBox)
from PySide6.QtCore import Qt, QDate, Signal
from PySide6.QtGui import QFont
from data.models import ExpenseCategory, PaymentMethod


class StatisticCard(QFrame):
    """Card widget for displaying statistics."""

    def __init__(self, title: str, value: str, subtitle: str = "", parent=None):
        """Initialize statistic card."""
        super().__init__(parent)
        self.setObjectName("cardFrame")
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 12, 16, 12)
        layout.setSpacing(4)

        # Title label
        title_label = QLabel(title)
        title_label.setObjectName("subtitleLabel")
        layout.addWidget(title_label)

        # Value label
        value_label = QLabel(value)
        value_label.setObjectName("valueLabel")
        layout.addWidget(value_label)

        # Subtitle label
        if subtitle:
            subtitle_label = QLabel(subtitle)
            subtitle_label.setObjectName("subtitleLabel")
            layout.addWidget(subtitle_label)

        layout.addStretch()
        self.setMinimumHeight(100)


class ExpenseForm(QWidget):
    """Form widget for adding/editing expenses."""
    
    submit_clicked = Signal(dict)
    cancel_clicked = Signal()

    def __init__(self, parent=None):
        """Initialize expense form."""
        super().__init__(parent)
        self.init_ui()

    def init_ui(self) -> None:
        """Initialize UI components."""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(12)

        # Description
        desc_layout = QHBoxLayout()
        desc_label = QLabel("Description:")
        self.description_input = QLineEdit()
        self.description_input.setPlaceholderText("Enter expense description...")
        desc_layout.addWidget(desc_label, 1)
        desc_layout.addWidget(self.description_input, 3)
        layout.addLayout(desc_layout)

        # Amount and Category
        amount_cat_layout = QHBoxLayout()
        
        amount_label = QLabel("Amount:")
        self.amount_input = QDoubleSpinBox()
        self.amount_input.setRange(0, 999999.99)
        self.amount_input.setDecimals(2)
        self.amount_input.setSingleStep(0.01)
        amount_cat_layout.addWidget(amount_label, 1)
        amount_cat_layout.addWidget(self.amount_input, 1)

        cat_label = QLabel("Category:")
        self.category_combo = QComboBox()
        self.category_combo.addItems([cat.value for cat in ExpenseCategory])
        amount_cat_layout.addWidget(cat_label, 1)
        amount_cat_layout.addWidget(self.category_combo, 1)
        layout.addLayout(amount_cat_layout)

        # Payment Method and Date
        method_date_layout = QHBoxLayout()

        method_label = QLabel("Payment Method:")
        self.method_combo = QComboBox()
        self.method_combo.addItems([method.value for method in PaymentMethod])
        method_date_layout.addWidget(method_label, 1)
        method_date_layout.addWidget(self.method_combo, 1)

        date_label = QLabel("Date:")
        self.date_input = QDateEdit()
        self.date_input.setDate(QDate.currentDate())
        method_date_layout.addWidget(date_label, 1)
        method_date_layout.addWidget(self.date_input, 1)
        layout.addLayout(method_date_layout)

        # Notes
        notes_label = QLabel("Notes:")
        layout.addWidget(notes_label)
        self.notes_input = QTextEdit()
        self.notes_input.setPlaceholderText("Add any additional notes...")
        self.notes_input.setMaximumHeight(100)
        layout.addWidget(self.notes_input)

        # Reimbursable checkbox
        self.reimbursable_checkbox = QCheckBox("Mark as Reimbursable")
        layout.addWidget(self.reimbursable_checkbox)

        # Buttons
        button_layout = QHBoxLayout()
        button_layout.addStretch()

        self.submit_button = QPushButton("Add Expense")
        self.submit_button.setObjectName("addButton")
        self.submit_button.clicked.connect(self._on_submit)
        button_layout.addWidget(self.submit_button)

        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.cancel_clicked.emit)
        button_layout.addWidget(self.cancel_button)

        layout.addLayout(button_layout)

    def get_form_data(self) -> dict:
        """Get form data as dictionary."""
        return {
            'description': self.description_input.text(),
            'amount': self.amount_input.value(),
            'category': self.category_combo.currentText(),
            'payment_method': self.method_combo.currentText(),
            'date': self.date_input.date().toPython(),
            'notes': self.notes_input.toPlainText() or None,
            'is_reimbursable': self.reimbursable_checkbox.isChecked(),
        }

    def set_form_data(self, data: dict) -> None:
        """Set form data from dictionary."""
        if 'description' in data:
            self.description_input.setText(data['description'])
        if 'amount' in data:
            self.amount_input.setValue(float(data['amount']))
        if 'category' in data:
            index = self.category_combo.findText(data['category'])
            if index >= 0:
                self.category_combo.setCurrentIndex(index)
        if 'payment_method' in data:
            index = self.method_combo.findText(data['payment_method'])
            if index >= 0:
                self.method_combo.setCurrentIndex(index)
        if 'date' in data:
            from datetime import datetime
            if isinstance(data['date'], str):
                date_obj = datetime.fromisoformat(data['date']).date()
            else:
                date_obj = data['date']
            self.date_input.setDate(date_obj)
        if 'notes' in data:
            self.notes_input.setPlainText(data['notes'] or "")
        if 'is_reimbursable' in data:
            self.reimbursable_checkbox.setChecked(data['is_reimbursable'])

    def reset(self) -> None:
        """Reset form to default values."""
        self.description_input.clear()
        self.amount_input.setValue(0.0)
        self.category_combo.setCurrentIndex(0)
        self.method_combo.setCurrentIndex(0)
        self.date_input.setDate(QDate.currentDate())
        self.notes_input.clear()
        self.reimbursable_checkbox.setChecked(False)

    def _on_submit(self) -> None:
        """Handle submit button click."""
        self.submit_clicked.emit(self.get_form_data())


class ExpenseTable(QTableWidget):
    """Table widget for displaying expenses."""

    def __init__(self, parent=None):
        """Initialize expense table."""
        super().__init__(parent)
        self.init_ui()

    def init_ui(self) -> None:
        """Initialize table UI."""
        self.setColumnCount(6)
        self.setHorizontalHeaderLabels([
            "Description", "Amount", "Category", "Payment Method", "Date", "Notes"
        ])
        self.setColumnWidth(0, 200)
        self.setColumnWidth(1, 100)
        self.setColumnWidth(2, 120)
        self.setColumnWidth(3, 120)
        self.setColumnWidth(4, 100)
        self.setColumnWidth(5, 150)
        self.setAlternatingRowColors(True)
        from PySide6.QtWidgets import QAbstractItemView
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setSelectionMode(QAbstractItemView.SingleSelection)

    def add_row(self, expense_data: dict) -> None:
        """Add expense row to table."""
        row_position = self.rowCount()
        self.insertRow(row_position)

        # Store the expense ID in the row
        self.setItem(row_position, 0, QTableWidgetItem(expense_data.get('description', '')))
        self.item(row_position, 0).setData(Qt.UserRole, expense_data.get('id', ''))

        self.setItem(row_position, 1, QTableWidgetItem(f"${expense_data.get('amount', 0):.2f}"))
        self.setItem(row_position, 2, QTableWidgetItem(expense_data.get('category', '')))
        self.setItem(row_position, 3, QTableWidgetItem(expense_data.get('payment_method', '')))
        self.setItem(row_position, 4, QTableWidgetItem(str(expense_data.get('date', ''))))
        self.setItem(row_position, 5, QTableWidgetItem(expense_data.get('notes', '') or ''))

    def get_selected_id(self) -> str:
        """Get the ID of selected row."""
        selected_rows = self.selectedIndexes()
        if selected_rows:
            row = selected_rows[0].row()
            return self.item(row, 0).data(Qt.UserRole)
        return ""

    def clear_table(self) -> None:
        """Clear all rows from table."""
        self.setRowCount(0)


# Import QCheckBox for the form
from PySide6.QtWidgets import QCheckBox
