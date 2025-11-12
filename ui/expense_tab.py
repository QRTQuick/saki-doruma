"""
Expense management tab for the application.
"""

from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel,
                               QPushButton, QLineEdit, QComboBox, QDateEdit,
                               QMessageBox, QDialog, QScrollArea)
from PySide6.QtCore import Qt, QDate, QDateTime, Signal
from datetime import datetime
from data.database import DatabaseManager
from data.models import ExpenseCategory, PaymentMethod
from modules.expense_manager import ExpenseManager
from ui.widgets import ExpenseTable, ExpenseForm, StatisticCard


class ExpenseTab(QWidget):
    """Tab for managing expenses."""

    def __init__(self, parent=None):
        """Initialize expense tab."""
        super().__init__(parent)
        self.db_manager = DatabaseManager()
        self.expense_manager = ExpenseManager(self.db_manager)
        self.init_ui()
        self.load_expenses()

    def init_ui(self) -> None:
        """Initialize UI components."""
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(16, 16, 16, 16)
        main_layout.setSpacing(12)

        # Statistics section
        stats_layout = QHBoxLayout()
        self.total_stat = StatisticCard("Total Expenses", "$0.00", "All time")
        self.count_stat = StatisticCard("Number of Expenses", "0", "Total count")
        self.avg_stat = StatisticCard("Average Expense", "$0.00", "Per transaction")
        stats_layout.addWidget(self.total_stat)
        stats_layout.addWidget(self.count_stat)
        stats_layout.addWidget(self.avg_stat)
        main_layout.addLayout(stats_layout)

        # Toolbar
        toolbar_layout = QHBoxLayout()
        
        # Search
        search_label = QLabel("Search:")
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search by description...")
        self.search_input.setMaximumWidth(250)
        self.search_input.textChanged.connect(self._on_search)
        toolbar_layout.addWidget(search_label)
        toolbar_layout.addWidget(self.search_input)

        # Filter by category
        cat_label = QLabel("Category:")
        self.category_filter = QComboBox()
        self.category_filter.addItem("All Categories")
        self.category_filter.addItems([cat.value for cat in ExpenseCategory])
        self.category_filter.setMaximumWidth(150)
        self.category_filter.currentTextChanged.connect(self._on_filter_category)
        toolbar_layout.addWidget(cat_label)
        toolbar_layout.addWidget(self.category_filter)

        toolbar_layout.addStretch()

        # Add Button
        add_btn = QPushButton("+ Add Expense")
        add_btn.setObjectName("addButton")
        add_btn.clicked.connect(self._on_add_expense)
        toolbar_layout.addWidget(add_btn)

        # Edit Button
        self.edit_btn = QPushButton("✎ Edit")
        self.edit_btn.setObjectName("editButton")
        self.edit_btn.clicked.connect(self._on_edit_expense)
        self.edit_btn.setEnabled(False)
        toolbar_layout.addWidget(self.edit_btn)

        # Delete Button
        self.delete_btn = QPushButton("✕ Delete")
        self.delete_btn.setObjectName("deleteButton")
        self.delete_btn.clicked.connect(self._on_delete_expense)
        self.delete_btn.setEnabled(False)
        toolbar_layout.addWidget(self.delete_btn)

        # Export Button
        export_btn = QPushButton("⬇ Export CSV")
        export_btn.setObjectName("exportButton")
        export_btn.clicked.connect(self._on_export)
        toolbar_layout.addWidget(export_btn)

        main_layout.addLayout(toolbar_layout)

        # Expense table
        self.expense_table = ExpenseTable()
        self.expense_table.itemSelectionChanged.connect(self._on_table_selection_changed)
        main_layout.addWidget(self.expense_table)

    def load_expenses(self) -> None:
        """Load expenses from database."""
        expenses = self.expense_manager.get_all_expenses()
        self.expense_table.clear_table()
        for expense in expenses:
            self.expense_table.add_row(expense)
        self._update_statistics()

    def _update_statistics(self) -> None:
        """Update statistics cards."""
        expenses = self.expense_manager.get_all_expenses()
        total = self.expense_manager.get_total_expenses(expenses)
        count = len(expenses)
        avg = total / count if count > 0 else 0

        self.total_stat.findChild(QLabel, None).setText(f"${total:.2f}") if self.total_stat.findChild(QLabel) else None
        # Update labels directly
        for i, label in enumerate(self.total_stat.findChildren(QLabel)):
            if i == 1:  # value label
                label.setText(f"${total:.2f}")

        for i, label in enumerate(self.count_stat.findChildren(QLabel)):
            if i == 1:
                label.setText(str(count))

        for i, label in enumerate(self.avg_stat.findChildren(QLabel)):
            if i == 1:
                label.setText(f"${avg:.2f}")

    def _on_add_expense(self) -> None:
        """Open add expense dialog."""
        dialog = ExpenseFormDialog(self)
        if dialog.exec() == QDialog.Accepted:
            data = dialog.expense_form.get_form_data()
            from data.models import ExpenseCategory, PaymentMethod
            expense = self.expense_manager.create_expense(
                description=data['description'],
                amount=data['amount'],
                category=ExpenseCategory(data['category']),
                payment_method=PaymentMethod(data['payment_method']),
                date=datetime.combine(data['date'], datetime.min.time()),
                notes=data['notes'],
                is_reimbursable=data['is_reimbursable']
            )
            self.load_expenses()
            QMessageBox.information(self, "Success", "Expense added successfully!")

    def _on_edit_expense(self) -> None:
        """Edit selected expense."""
        expense_id = self.expense_table.get_selected_id()
        if not expense_id:
            QMessageBox.warning(self, "Warning", "Please select an expense to edit.")
            return

        expense_data = self.expense_manager.get_expense(expense_id)
        dialog = ExpenseFormDialog(self, expense_data)
        if dialog.exec() == QDialog.Accepted:
            data = dialog.expense_form.get_form_data()
            from data.models import ExpenseCategory, PaymentMethod
            self.expense_manager.update_expense(
                expense_id,
                description=data['description'],
                amount=data['amount'],
                category=ExpenseCategory(data['category']).value,
                payment_method=PaymentMethod(data['payment_method']).value,
                date=datetime.combine(data['date'], datetime.min.time()).isoformat(),
                notes=data['notes'],
                is_reimbursable=data['is_reimbursable']
            )
            self.load_expenses()
            QMessageBox.information(self, "Success", "Expense updated successfully!")

    def _on_delete_expense(self) -> None:
        """Delete selected expense."""
        expense_id = self.expense_table.get_selected_id()
        if not expense_id:
            QMessageBox.warning(self, "Warning", "Please select an expense to delete.")
            return

        reply = QMessageBox.question(
            self,
            "Confirm Delete",
            "Are you sure you want to delete this expense?",
            QMessageBox.Yes | QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            if self.expense_manager.delete_expense(expense_id):
                self.load_expenses()
                QMessageBox.information(self, "Success", "Expense deleted successfully!")
            else:
                QMessageBox.critical(self, "Error", "Failed to delete expense.")

    def _on_search(self) -> None:
        """Search expenses."""
        query = self.search_input.text()
        if not query:
            self.load_expenses()
            return

        results = self.expense_manager.search_expenses(query)
        self.expense_table.clear_table()
        for expense in results:
            self.expense_table.add_row(expense)

    def _on_filter_category(self) -> None:
        """Filter expenses by category."""
        category_text = self.category_filter.currentText()
        if category_text == "All Categories":
            self.load_expenses()
            return

        try:
            category = ExpenseCategory(category_text)
            expenses = self.expense_manager.get_expenses_by_category(category)
            self.expense_table.clear_table()
            for expense in expenses:
                self.expense_table.add_row(expense)
        except ValueError:
            self.load_expenses()

    def _on_export(self) -> None:
        """Export expenses to CSV."""
        from PySide6.QtWidgets import QFileDialog
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Export Expenses",
            "",
            "CSV Files (*.csv)"
        )
        if file_path:
            if self.db_manager.export_expenses_csv(file_path):
                QMessageBox.information(self, "Success", f"Expenses exported to {file_path}")
            else:
                QMessageBox.critical(self, "Error", "Failed to export expenses.")

    def _on_table_selection_changed(self) -> None:
        """Handle table selection change."""
        has_selection = len(self.expense_table.selectedIndexes()) > 0
        self.edit_btn.setEnabled(has_selection)
        self.delete_btn.setEnabled(has_selection)


class ExpenseFormDialog(QDialog):
    """Dialog for adding/editing expenses."""

    def __init__(self, parent=None, expense_data=None):
        """Initialize dialog."""
        super().__init__(parent)
        self.setWindowTitle("Add Expense" if not expense_data else "Edit Expense")
        self.setMinimumWidth(600)
        self.expense_data = expense_data
        self.init_ui()

    def init_ui(self) -> None:
        """Initialize UI."""
        layout = QVBoxLayout(self)
        self.expense_form = ExpenseForm()
        layout.addWidget(self.expense_form)

        if self.expense_data:
            self.expense_form.set_form_data(self.expense_data)
            self.expense_form.submit_button.setText("Update Expense")

        self.expense_form.submit_clicked.connect(self.accept)
        self.expense_form.cancel_clicked.connect(self.reject)
