"""
Analytics and reporting tab for the application.
"""

from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel,
                               QPushButton, QDateEdit, QComboBox, QTableWidget,
                               QTableWidgetItem, QMessageBox)
from PySide6.QtCore import Qt, QDate
from datetime import datetime
from data.database import DatabaseManager
from modules.analytics import ExpenseAnalytics
from ui.widgets import StatisticCard


class AnalyticsTab(QWidget):
    """Tab for analytics and reporting."""

    def __init__(self, parent=None):
        """Initialize analytics tab."""
        super().__init__(parent)
        self.db_manager = DatabaseManager()
        self.analytics = ExpenseAnalytics(self.db_manager)
        self.init_ui()
        self.load_analytics()

    def init_ui(self) -> None:
        """Initialize UI components."""
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(16, 16, 16, 16)
        main_layout.setSpacing(12)

        # Statistics section
        stats_layout = QHBoxLayout()
        self.total_stat = StatisticCard("Total Expenses", "$0.00", "All time")
        self.avg_stat = StatisticCard("Average Expense", "$0.00", "Per transaction")
        self.max_stat = StatisticCard("Maximum Expense", "$0.00", "Single transaction")
        self.median_stat = StatisticCard("Median Expense", "$0.00", "Middle value")
        stats_layout.addWidget(self.total_stat)
        stats_layout.addWidget(self.avg_stat)
        stats_layout.addWidget(self.max_stat)
        stats_layout.addWidget(self.median_stat)
        main_layout.addLayout(stats_layout)

        # Additional stats
        stats_layout2 = QHBoxLayout()
        self.min_stat = StatisticCard("Minimum Expense", "$0.00", "Single transaction")
        self.count_stat = StatisticCard("Total Transactions", "0", "Total count")
        self.daily_stat = StatisticCard("Daily Average", "$0.00", "Per day")
        self.reimbursable_stat = StatisticCard("Reimbursable Total", "$0.00", "To be reimbursed")
        stats_layout2.addWidget(self.min_stat)
        stats_layout2.addWidget(self.count_stat)
        stats_layout2.addWidget(self.daily_stat)
        stats_layout2.addWidget(self.reimbursable_stat)
        main_layout.addLayout(stats_layout2)

        # Category breakdown section
        cat_label = QLabel("Expense Breakdown by Category")
        cat_label.setStyleSheet("font-weight: bold; font-size: 12px;")
        main_layout.addWidget(cat_label)

        self.category_table = QTableWidget()
        self.category_table.setColumnCount(4)
        self.category_table.setHorizontalHeaderLabels(["Category", "Count", "Total Amount", "Percentage"])
        self.category_table.setMaximumHeight(150)
        main_layout.addWidget(self.category_table)

        # Payment method breakdown
        method_label = QLabel("Expense Breakdown by Payment Method")
        method_label.setStyleSheet("font-weight: bold; font-size: 12px;")
        main_layout.addWidget(method_label)

        self.method_table = QTableWidget()
        self.method_table.setColumnCount(4)
        self.method_table.setHorizontalHeaderLabels(["Payment Method", "Count", "Total Amount", "Percentage"])
        self.method_table.setMaximumHeight(150)
        main_layout.addWidget(self.method_table)

        # Top expenses section
        top_label = QLabel("Top 10 Expenses")
        top_label.setStyleSheet("font-weight: bold; font-size: 12px;")
        main_layout.addWidget(top_label)

        self.top_table = QTableWidget()
        self.top_table.setColumnCount(4)
        self.top_table.setHorizontalHeaderLabels(["Description", "Amount", "Category", "Date"])
        main_layout.addWidget(self.top_table)

        # Export button
        export_btn = QPushButton("⬇ Export Report")
        export_btn.setObjectName("exportButton")
        export_btn.clicked.connect(self._on_export_report)
        main_layout.addWidget(export_btn)

    def load_analytics(self) -> None:
        """Load and display analytics."""
        stats = self.analytics.get_expense_statistics()
        
        # Update statistics
        for i, label in enumerate(self.total_stat.findChildren(QLabel)):
            if i == 1:
                label.setText(f"${stats['total']:.2f}")

        for i, label in enumerate(self.avg_stat.findChildren(QLabel)):
            if i == 1:
                label.setText(f"${stats['average']:.2f}")

        for i, label in enumerate(self.max_stat.findChildren(QLabel)):
            if i == 1:
                label.setText(f"${stats['max']:.2f}")

        for i, label in enumerate(self.median_stat.findChildren(QLabel)):
            if i == 1:
                label.setText(f"${stats['median']:.2f}")

        for i, label in enumerate(self.min_stat.findChildren(QLabel)):
            if i == 1:
                label.setText(f"${stats['min']:.2f}")

        for i, label in enumerate(self.count_stat.findChildren(QLabel)):
            if i == 1:
                label.setText(str(stats['count']))

        daily_avg = self.analytics.get_daily_average()
        for i, label in enumerate(self.daily_stat.findChildren(QLabel)):
            if i == 1:
                label.setText(f"${daily_avg:.2f}")

        reimbursable = self.analytics.get_reimbursable_total()
        for i, label in enumerate(self.reimbursable_stat.findChildren(QLabel)):
            if i == 1:
                label.setText(f"${reimbursable:.2f}")

        # Load category breakdown
        self._load_category_breakdown()

        # Load payment method breakdown
        self._load_method_breakdown()

        # Load top expenses
        self._load_top_expenses()

    def _load_category_breakdown(self) -> None:
        """Load category breakdown table."""
        distribution = self.analytics.get_category_distribution()
        self.category_table.setRowCount(0)

        for category, data in distribution.items():
            row = self.category_table.rowCount()
            self.category_table.insertRow(row)
            self.category_table.setItem(row, 0, QTableWidgetItem(category))
            self.category_table.setItem(row, 1, QTableWidgetItem(str(data['count'])))
            self.category_table.setItem(row, 2, QTableWidgetItem(f"${data['amount']:.2f}"))
            self.category_table.setItem(row, 3, QTableWidgetItem(f"{data['percentage']:.1f}%"))

    def _load_method_breakdown(self) -> None:
        """Load payment method breakdown table."""
        distribution = self.analytics.get_payment_method_distribution()
        self.method_table.setRowCount(0)

        for method, data in distribution.items():
            row = self.method_table.rowCount()
            self.method_table.insertRow(row)
            self.method_table.setItem(row, 0, QTableWidgetItem(method))
            self.method_table.setItem(row, 1, QTableWidgetItem(str(data['count'])))
            self.method_table.setItem(row, 2, QTableWidgetItem(f"${data['amount']:.2f}"))
            self.method_table.setItem(row, 3, QTableWidgetItem(f"{data['percentage']:.1f}%"))

    def _load_top_expenses(self) -> None:
        """Load top expenses table."""
        top_expenses = self.analytics.get_top_expenses(10)
        self.top_table.setRowCount(0)

        for expense in top_expenses:
            row = self.top_table.rowCount()
            self.top_table.insertRow(row)
            self.top_table.setItem(row, 0, QTableWidgetItem(expense['description']))
            self.top_table.setItem(row, 1, QTableWidgetItem(f"${expense['amount']:.2f}"))
            self.top_table.setItem(row, 2, QTableWidgetItem(expense['category']))
            self.top_table.setItem(row, 3, QTableWidgetItem(str(expense['date'])))

    def _on_export_report(self) -> None:
        """Export analytics report."""
        from PySide6.QtWidgets import QFileDialog
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Export Report",
            f"expense_report_{datetime.now().strftime('%Y%m%d')}.txt",
            "Text Files (*.txt)"
        )
        if file_path:
            self._save_report_to_file(file_path)
            QMessageBox.information(self, "Success", f"Report exported to {file_path}")

    def _save_report_to_file(self, file_path: str) -> None:
        """Save report to file."""
        stats = self.analytics.get_expense_statistics()
        with open(file_path, 'w') as f:
            f.write("=" * 60 + "\n")
            f.write("EXPENSE ANALYTICS REPORT\n")
            f.write("=" * 60 + "\n\n")

            f.write("SUMMARY STATISTICS\n")
            f.write("-" * 60 + "\n")
            f.write(f"Total Expenses: ${stats['total']:.2f}\n")
            f.write(f"Number of Transactions: {stats['count']}\n")
            f.write(f"Average Expense: ${stats['average']:.2f}\n")
            f.write(f"Minimum: ${stats['min']:.2f}\n")
            f.write(f"Maximum: ${stats['max']:.2f}\n")
            f.write(f"Median: ${stats['median']:.2f}\n\n")

            f.write("CATEGORY BREAKDOWN\n")
            f.write("-" * 60 + "\n")
            distribution = self.analytics.get_category_distribution()
            for category, data in distribution.items():
                f.write(f"{category}: ${data['amount']:.2f} ({data['percentage']:.1f}%) - {data['count']} transactions\n")

            f.write("\n" + "=" * 60 + "\n")
            f.write(f"Report Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
