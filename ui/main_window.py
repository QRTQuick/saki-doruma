"""
Main application window for saki-doruma expense manager.
"""

from PySide6.QtWidgets import QMainWindow, QTabWidget, QVBoxLayout, QWidget, QMenuBar, QMenu
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from ui.stylesheet import get_stylesheet
from ui.expense_tab import ExpenseTab
from ui.calculator_tab import CalculatorTab
from ui.analytics_tab import AnalyticsTab


class MainWindow(QMainWindow):
    """Main application window."""

    def __init__(self):
        """Initialize main window."""
        super().__init__()
        self.setWindowTitle("saki-doruma - Company Expense Manager")
        self.setGeometry(100, 100, 1400, 900)
        self.setStyleSheet(get_stylesheet(dark_mode=True))
        self.init_ui()
        self.create_menu_bar()

    def init_ui(self) -> None:
        """Initialize UI components."""
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(0, 0, 0, 0)

        # Tab widget
        self.tabs = QTabWidget()
        
        # Create tabs
        self.expense_tab = ExpenseTab()
        self.calculator_tab = CalculatorTab()
        self.analytics_tab = AnalyticsTab()

        # Add tabs
        self.tabs.addTab(self.expense_tab, "💰 Expenses")
        self.tabs.addTab(self.calculator_tab, "🧮 Calculator")
        self.tabs.addTab(self.analytics_tab, "📊 Analytics")

        layout.addWidget(self.tabs)

    def create_menu_bar(self) -> None:
        """Create application menu bar."""
        menubar = self.menuBar()

        # File menu
        file_menu = menubar.addMenu("File")
        
        export_action = file_menu.addAction("Export Expenses")
        export_action.triggered.connect(self.expense_tab._on_export)
        
        file_menu.addSeparator()
        
        exit_action = file_menu.addAction("Exit")
        exit_action.triggered.connect(self.close)

        # View menu
        view_menu = menubar.addMenu("View")
        
        # Theme toggle
        theme_action = view_menu.addAction("Toggle Dark/Light Mode")
        theme_action.triggered.connect(self.toggle_theme)

        # Help menu
        help_menu = menubar.addMenu("Help")
        
        about_action = help_menu.addAction("About")
        about_action.triggered.connect(self.show_about)

    def toggle_theme(self) -> None:
        """Toggle between dark and light theme."""
        # This would require more implementation for full theme switching
        pass

    def show_about(self) -> None:
        """Show about dialog."""
        from PySide6.QtWidgets import QMessageBox
        QMessageBox.about(
            self,
            "About saki-doruma",
            "saki-doruma - Company Expense Manager\n\n"
            "Version 1.0.0\n\n"
            "A professional expense management and accounting application "
            "with advanced features including analytics, calculations, and reporting.\n\n"
            "© 2025 All rights reserved."
        )
