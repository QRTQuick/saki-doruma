"""
Stylesheet and theme configuration for the application.
"""

DARK_STYLESHEET = """
/* Main Window */
QMainWindow {
    background-color: #0f1419;
    color: #ffffff;
}

/* Tab Widget */
QTabWidget::pane {
    border: 1px solid #1e2633;
    background-color: #0f1419;
}

QTabBar::tab {
    background-color: #1a1f2e;
    border: 1px solid #2d3748;
    padding: 8px 20px;
    margin-right: 2px;
    color: #b0bec5;
    font-weight: 500;
}

QTabBar::tab:selected {
    background-color: #2d3e8f;
    color: #ffffff;
    border-bottom: 3px solid #5b8def;
}

QTabBar::tab:hover {
    background-color: #252d3d;
}

/* Buttons */
QPushButton {
    background-color: #2d3e8f;
    color: #ffffff;
    border: none;
    padding: 8px 16px;
    border-radius: 4px;
    font-weight: 500;
    border: 1px solid #3d4e9f;
}

QPushButton:hover {
    background-color: #3d4e9f;
    border: 1px solid #4d5eaf;
}

QPushButton:pressed {
    background-color: #1d2e7f;
}

QPushButton:disabled {
    background-color: #1a1f2e;
    color: #707880;
}

/* Add Button */
QPushButton#addButton {
    background-color: #10b981;
    border: 1px solid #059669;
}

QPushButton#addButton:hover {
    background-color: #059669;
}

/* Delete Button */
QPushButton#deleteButton {
    background-color: #ef4444;
    border: 1px solid #dc2626;
}

QPushButton#deleteButton:hover {
    background-color: #dc2626;
}

/* Edit Button */
QPushButton#editButton {
    background-color: #f59e0b;
    border: 1px solid #d97706;
}

QPushButton#editButton:hover {
    background-color: #d97706;
}

/* Export Button */
QPushButton#exportButton {
    background-color: #8b5cf6;
    border: 1px solid #7c3aed;
}

QPushButton#exportButton:hover {
    background-color: #7c3aed;
}

/* Input Fields */
QLineEdit, QTextEdit {
    background-color: #1a1f2e;
    color: #ffffff;
    border: 1px solid #2d3748;
    border-radius: 4px;
    padding: 8px;
    selection-background-color: #2d3e8f;
}

QLineEdit:focus, QTextEdit:focus {
    border: 2px solid #2d3e8f;
}

QLineEdit::placeholder {
    color: #707880;
}

/* ComboBox */
QComboBox {
    background-color: #1a1f2e;
    color: #ffffff;
    border: 1px solid #2d3748;
    border-radius: 4px;
    padding: 6px 10px;
    selection-background-color: #2d3e8f;
}

QComboBox:focus {
    border: 2px solid #2d3e8f;
}

QComboBox::drop-down {
    border: none;
    padding-right: 10px;
}

QComboBox::down-arrow {
    image: none;
    background-color: transparent;
}

QComboBox QAbstractItemView {
    background-color: #1a1f2e;
    color: #ffffff;
    selection-background-color: #2d3e8f;
    border: 1px solid #2d3748;
}

/* Spin Box */
QSpinBox, QDoubleSpinBox {
    background-color: #1a1f2e;
    color: #ffffff;
    border: 1px solid #2d3748;
    border-radius: 4px;
    padding: 6px;
}

QSpinBox:focus, QDoubleSpinBox:focus {
    border: 2px solid #2d3e8f;
}

/* Date/Time Edit */
QDateEdit, QTimeEdit, QDateTimeEdit {
    background-color: #1a1f2e;
    color: #ffffff;
    border: 1px solid #2d3748;
    border-radius: 4px;
    padding: 6px;
}

QDateEdit:focus, QTimeEdit:focus, QDateTimeEdit:focus {
    border: 2px solid #2d3e8f;
}

/* Labels */
QLabel {
    color: #e2e8f0;
    font-weight: 500;
}

QLabel#titleLabel {
    color: #ffffff;
    font-size: 14px;
    font-weight: bold;
}

QLabel#valueLabel {
    color: #2d3e8f;
    font-size: 18px;
    font-weight: bold;
}

QLabel#subtitleLabel {
    color: #cbd5e1;
    font-size: 11px;
}

/* Table Widget */
QTableWidget, QTableView {
    background-color: #1a1f2e;
    alternate-background-color: #151b28;
    color: #ffffff;
    border: 1px solid #2d3748;
    gridline-color: #2d3748;
}

QTableWidget::item, QTableView::item {
    padding: 6px;
    color: #e2e8f0;
}

QTableWidget::item:selected, QTableView::item:selected {
    background-color: #2d3e8f;
    color: #ffffff;
}

QTableWidget::item:hover, QTableView::item:hover {
    background-color: #252d3d;
}

QHeaderView::section {
    background-color: #0f1419;
    color: #e2e8f0;
    padding: 6px;
    border: none;
    border-right: 1px solid #2d3748;
    border-bottom: 2px solid #2d3e8f;
    font-weight: bold;
}

/* Scrollbar */
QScrollBar:vertical {
    background-color: #0f1419;
    width: 12px;
}

QScrollBar::handle:vertical {
    background-color: #2d3748;
    border-radius: 6px;
    min-height: 20px;
}

QScrollBar::handle:vertical:hover {
    background-color: #3d4758;
}

QScrollBar:horizontal {
    background-color: #0f1419;
    height: 12px;
}

QScrollBar::handle:horizontal {
    background-color: #2d3748;
    border-radius: 6px;
    min-width: 20px;
}

QScrollBar::handle:horizontal:hover {
    background-color: #3d4758;
}

QScrollBar::add-line, QScrollBar::sub-line {
    border: none;
    background: none;
}

/* GroupBox */
QGroupBox {
    color: #e2e8f0;
    border: 1px solid #2d3748;
    border-radius: 4px;
    margin-top: 10px;
    padding-top: 10px;
    font-weight: 500;
}

QGroupBox::title {
    subcontrol-origin: margin;
    left: 10px;
    padding: 0 3px 0 3px;
}

/* Frame */
QFrame {
    background-color: #0f1419;
    border: none;
}

QFrame#cardFrame {
    background-color: #1a1f2e;
    border: 1px solid #2d3748;
    border-radius: 6px;
    padding: 12px;
}

/* Splitter */
QSplitter::handle {
    background-color: #2d3748;
}

QSplitter::handle:hover {
    background-color: #3d4758;
}

/* Menu Bar */
QMenuBar {
    background-color: #1a1f2e;
    color: #e2e8f0;
    border-bottom: 1px solid #2d3748;
}

QMenuBar::item:selected {
    background-color: #2d3e8f;
}

QMenu {
    background-color: #1a1f2e;
    color: #e2e8f0;
    border: 1px solid #2d3748;
}

QMenu::item:selected {
    background-color: #2d3e8f;
}

/* Status Bar */
QStatusBar {
    background-color: #1a1f2e;
    color: #e2e8f0;
    border-top: 1px solid #2d3748;
}

/* Dialog */
QDialog {
    background-color: #0f1419;
    color: #ffffff;
}

/* CheckBox */
QCheckBox {
    color: #e2e8f0;
    spacing: 5px;
}

QCheckBox::indicator {
    width: 18px;
    height: 18px;
    background-color: #1a1f2e;
    border: 1px solid #2d3748;
    border-radius: 3px;
}

QCheckBox::indicator:checked {
    background-color: #2d3e8f;
    border: 1px solid #3d4e9f;
    image: url(check);
}

/* RadioButton */
QRadioButton {
    color: #e2e8f0;
    spacing: 5px;
}

QRadioButton::indicator {
    width: 18px;
    height: 18px;
}

QRadioButton::indicator::unchecked {
    background-color: #1a1f2e;
    border: 1px solid #2d3748;
    border-radius: 9px;
}

QRadioButton::indicator::checked {
    background-color: #2d3e8f;
    border: 1px solid #3d4e9f;
    border-radius: 9px;
}
"""

LIGHT_STYLESHEET = """
/* Light theme stylesheet - similar structure but with light colors */
QMainWindow {
    background-color: #f8fafc;
    color: #1e293b;
}

QTabWidget::pane {
    border: 1px solid #e2e8f0;
    background-color: #f8fafc;
}

QTabBar::tab {
    background-color: #f1f5f9;
    border: 1px solid #cbd5e1;
    padding: 8px 20px;
    margin-right: 2px;
    color: #64748b;
    font-weight: 500;
}

QTabBar::tab:selected {
    background-color: #3b82f6;
    color: #ffffff;
    border-bottom: 3px solid #1e40af;
}

QTabBar::tab:hover {
    background-color: #e2e8f0;
}

QPushButton {
    background-color: #3b82f6;
    color: #ffffff;
    border: none;
    padding: 8px 16px;
    border-radius: 4px;
    font-weight: 500;
}

QPushButton:hover {
    background-color: #2563eb;
}

QPushButton:pressed {
    background-color: #1d4ed8;
}

QLineEdit, QTextEdit {
    background-color: #ffffff;
    color: #1e293b;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    padding: 8px;
}

QLineEdit:focus, QTextEdit:focus {
    border: 2px solid #3b82f6;
}

QLabel {
    color: #475569;
}

QTableWidget, QTableView {
    background-color: #ffffff;
    alternate-background-color: #f8fafc;
    color: #1e293b;
    border: 1px solid #e2e8f0;
    gridline-color: #e2e8f0;
}

QTableWidget::item:selected, QTableView::item:selected {
    background-color: #3b82f6;
    color: #ffffff;
}
"""

def get_stylesheet(dark_mode: bool = True) -> str:
    """Get the appropriate stylesheet."""
    return DARK_STYLESHEET if dark_mode else LIGHT_STYLESHEET
