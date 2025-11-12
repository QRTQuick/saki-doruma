"""
ARCHITECTURE & DESIGN DOCUMENTATION
saki-doruma - Company Expense Manager

=================================================================================
ARCHITECTURAL OVERVIEW
=================================================================================

The application follows a clean three-layer architecture pattern:

┌──────────────────────────────────────────────────────────────────────┐
│                          PRESENTATION LAYER (UI)                    │
│  ┌────────────────────────────────────────────────────────────────┐ │
│  │ Main Window (main_window.py)                                  │ │
│  │ ├── Expense Tab (expense_tab.py)                              │ │
│  │ │   ├── ExpenseTable widget                                   │ │
│  │ │   ├── ExpenseForm dialog                                    │ │
│  │ │   └── Statistics cards                                      │ │
│  │ ├── Calculator Tab (calculator_tab.py)                        │ │
│  │ │   ├── Mini Calculator                                       │ │
│  │ │   ├── VAT Calculator                                        │ │
│  │ │   ├── Tax Calculator                                        │ │
│  │ │   └── ... (7 more tools)                                    │ │
│  │ └── Analytics Tab (analytics_tab.py)                          │ │
│  │     ├── Statistics display                                    │ │
│  │     ├── Category breakdown                                    │ │
│  │     ├── Payment method breakdown                              │ │
│  │     └── Top expenses view                                     │ │
│  └────────────────────────────────────────────────────────────────┘ │
│  Theme: stylesheet.py (Dark theme)                                  │
│  Widgets: widgets.py (Custom UI components)                         │
└──────────────────────────────────────────────────────────────────────┘
                                    ↓
┌──────────────────────────────────────────────────────────────────────┐
│                       BUSINESS LOGIC LAYER                           │
│  ┌────────────────────────────────────────────────────────────────┐ │
│  │ Modules Package (modules/)                                    │ │
│  │ ├── calculator.py                                             │ │
│  │ │   ├── MiniCalculator                                        │ │
│  │ │   └── AccountingCalculator                                  │ │
│  │ ├── expense_manager.py                                        │ │
│  │ │   ├── ExpenseManager                                        │ │
│  │ │   └── ReportGenerator                                       │ │
│  │ └── analytics.py                                              │ │
│  │     └── ExpenseAnalytics                                      │ │
│  └────────────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────────────┘
                                    ↓
┌──────────────────────────────────────────────────────────────────────┐
│                         DATA LAYER                                   │
│  ┌────────────────────────────────────────────────────────────────┐ │
│  │ Data Package (data/)                                          │ │
│  │ ├── models.py                                                 │ │
│  │ │   ├── ExpenseCategory (Enum)                                │ │
│  │ │   ├── PaymentMethod (Enum)                                  │ │
│  │ │   ├── Expense (Dataclass)                                   │ │
│  │ │   ├── ExpenseReport (Dataclass)                             │ │
│  │ │   └── Company (Dataclass)                                   │ │
│  │ └── database.py                                               │ │
│  │     └── DatabaseManager                                       │ │
│  │         ├── File: expenses.json                               │ │
│  │         └── File: reports.json                                │ │
│  └────────────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────────────┘

=================================================================================
DATA MODELS
=================================================================================

Expense Model:
{
  "id": "uuid-string",
  "description": "string",
  "amount": float,
  "category": "string (enum)",
  "payment_method": "string (enum)",
  "date": "ISO datetime",
  "notes": "string or null",
  "receipt_path": "string or null",
  "is_reimbursable": boolean,
  "created_at": "ISO datetime",
  "updated_at": "ISO datetime"
}

ExpenseReport Model:
{
  "report_id": "uuid-string",
  "title": "string",
  "start_date": "ISO datetime",
  "end_date": "ISO datetime",
  "expenses": [Expense array],
  "notes": "string or null",
  "created_at": "ISO datetime"
}

=================================================================================
CLASS HIERARCHY
=================================================================================

Presentation Layer:
├── QMainWindow
│   └── MainWindow
├── QWidget
│   ├── ExpenseTab
│   ├── CalculatorTab
│   ├── AnalyticsTab
│   └── ExpenseForm
├── QFrame
│   └── StatisticCard
├── QTableWidget
│   └── ExpenseTable
└── Other PySide6 components

Business Logic:
├── MiniCalculator
│   └── Methods: add(), subtract(), multiply(), divide(), evaluate(), etc.
├── AccountingCalculator
│   └── Methods: calculate_vat(), calculate_tax(), calculate_markup(), etc.
├── ExpenseManager
│   └── Methods: create_expense(), get_expenses(), search(), etc.
├── ReportGenerator
│   └── Methods: create_report(), get_summary()
└── ExpenseAnalytics
    └── Methods: get_monthly_trend(), get_category_distribution(), etc.

Data Layer:
├── DatabaseManager
│   └── Methods: save_expense(), get_expenses(), delete_expense(), etc.
├── Expense (dataclass)
├── ExpenseReport (dataclass)
├── ExpenseCategory (Enum)
├── PaymentMethod (Enum)
└── Company (dataclass)

=================================================================================
USER INTERACTION FLOW
=================================================================================

EXPENSE WORKFLOW:
1. User launches main.py
2. MainWindow loads with 3 tabs
3. User clicks "Add Expense" button
4. ExpenseFormDialog opens
5. User fills form with expense details
6. Form validation occurs
7. ExpenseManager.create_expense() called
8. DatabaseManager saves to JSON
9. ExpenseTable refreshed with new data
10. StatisticCard widgets update

SEARCH/FILTER WORKFLOW:
1. User enters search query or selects category
2. ExpenseManager.search_expenses() or get_expenses_by_category()
3. Results filtered from database
4. ExpenseTable populated with filtered results
5. Statistics updated for filtered set

CALCULATOR WORKFLOW:
1. User navigates to Calculator tab
2. Selects calculator type (Basic, VAT, Tax, etc.)
3. Enters required values
4. Clicks "Calculate" button
5. Calculation function invoked
6. Results displayed in output field
7. History updated (where applicable)

ANALYTICS WORKFLOW:
1. User navigates to Analytics tab
2. AnalyticsTab loads on initialization
3. ExpenseAnalytics.get_expense_statistics() called
4. Statistics displayed in StatisticCard widgets
5. Category/Payment method distribution calculated
6. Tables populated with breakdown data
7. Top expenses identified and displayed
8. User can export report

EXPORT WORKFLOW:
1. User clicks Export button
2. QFileDialog opens for file selection
3. User chooses location and filename
4. DatabaseManager.export_expenses_csv() called
5. Data written to CSV format
6. Success message displayed
7. File saved to user's chosen location

=================================================================================
KEY DESIGN PATTERNS
=================================================================================

1. SEPARATION OF CONCERNS
   - UI logic isolated in ui/ package
   - Business logic in modules/ package
   - Data access in data/ package
   - Each layer has specific responsibilities

2. MVC-like ARCHITECTURE
   - Model: data models (Expense, ExpenseReport, etc.)
   - View: UI components (widgets, dialogs, tabs)
   - Controller: Manager classes (ExpenseManager, ReportGenerator)

3. DEPENDENCY INJECTION
   - DatabaseManager injected into ExpenseManager
   - ExpenseManager used by ExpenseTab
   - Loose coupling between layers

4. DATACLASS PATTERN
   - Models use @dataclass decorator
   - Immutable value objects
   - Type hints for clarity

5. ENUM PATTERN
   - ExpenseCategory as Enum
   - PaymentMethod as Enum
   - Type-safe category/method selection

6. SINGLETON-LIKE PATTERN
   - DatabaseManager initialized once
   - Reused throughout application
   - Centralized data access

7. DIALOG PATTERN
   - ExpenseFormDialog for adding/editing
   - Modal dialogs for user interaction
   - Result codes for acceptance/cancellation

=================================================================================
MODULE RESPONSIBILITIES
=================================================================================

data/models.py:
- Define data structures
- Expense, ExpenseReport, Company models
- ExpenseCategory and PaymentMethod enums
- to_dict() methods for serialization

data/database.py:
- JSON file operations
- CRUD operations for expenses and reports
- CSV export functionality
- Date range queries

modules/calculator.py:
- MiniCalculator: basic arithmetic, expression evaluation
- AccountingCalculator: VAT, tax, discount, markup, etc.
- Interest calculations (simple & compound)
- Calculation history

modules/expense_manager.py:
- ExpenseManager: expense CRUD, filtering, searching
- ReportGenerator: create reports, summarize data
- Category/payment method breakdowns
- Date range queries

modules/analytics.py:
- ExpenseAnalytics: statistical analysis
- Trend analysis
- Distribution calculations
- Forecasting based on averages

ui/stylesheet.py:
- Dark theme color scheme
- Widget styling
- Component-specific styles
- Responsive design helpers

ui/widgets.py:
- StatisticCard: displays key metrics
- ExpenseForm: form for expense input
- ExpenseTable: displays expense list
- Custom UI elements

ui/main_window.py:
- Application main window
- Tab initialization
- Menu bar setup
- About dialogs

ui/expense_tab.py:
- Expense management interface
- Add/edit/delete operations
- Search and filter UI
- Export functionality

ui/calculator_tab.py:
- Calculator interface
- 10+ accounting tools
- Calculation displays
- History tracking

ui/analytics_tab.py:
- Analytics interface
- Statistics display
- Breakdown tables
- Report export

=================================================================================
CONFIGURATION MANAGEMENT
=================================================================================

config.py contains:
- Application metadata (name, version, author)
- Directory paths (base, data, logs, exports)
- Database paths
- UI settings (dark mode, currency, decimal places)
- Default values (category, payment method)
- Date/time formats
- Feature flags

=================================================================================
DATA PERSISTENCE
=================================================================================

Storage Format: JSON (Human-readable, portable)

Directory Structure:
saki-doruma/
├── data/
│   └── storage/
│       ├── expenses.json (all expense records)
│       └── reports.json (generated reports)
└── exports/ (CSV and text exports)

Backup Recommendation:
- Manual backup: Copy data/storage/ folder
- Automated: Set up scheduled copies
- Cloud: Consider cloud storage sync
- Frequency: Weekly or after major changes

=================================================================================
SCALABILITY CONSIDERATIONS
=================================================================================

Current Implementation:
- JSON-based storage (suitable for < 50,000 records)
- All data loaded into memory
- Linear search operations

Future Improvements:
- SQLite database for larger datasets
- Indexed searches
- Pagination for large result sets
- Caching mechanisms
- Background processing for exports

=================================================================================
SECURITY CONSIDERATIONS
=================================================================================

Current:
- Local JSON storage (no encryption)
- No authentication
- No access control

Recommendations:
- Add file encryption
- Implement user authentication
- Add audit logging
- Secure sensitive data
- Implement backup encryption

=================================================================================
PERFORMANCE OPTIMIZATION
=================================================================================

Current Optimizations:
- Direct JSON operations
- Efficient filtering
- Lazy loading of analytics

Further Optimizations:
- Database indexing
- Query optimization
- Caching frequently accessed data
- Lazy loading of large datasets
- Background processing

=================================================================================
ERROR HANDLING
=================================================================================

Strategy:
- Try-except blocks in database operations
- User-friendly error messages
- Validation before operations
- Logging of errors
- Graceful failure handling

Error Types Handled:
- File I/O errors
- JSON parsing errors
- Division by zero in calculations
- Invalid input data
- Missing database files

=================================================================================
TESTING CONSIDERATIONS
=================================================================================

Unit Testing:
- Test calculator functions
- Test database operations
- Test analytics calculations

Integration Testing:
- Test expense creation to display
- Test filtering and searching
- Test exports

UI Testing:
- Test form input validation
- Test button actions
- Test navigation between tabs

=================================================================================
DEPLOYMENT
=================================================================================

Requirements:
- Python 3.9+
- PySide6 installed via pip

Executable Creation:
- PyInstaller for Windows/Mac/Linux
- py2exe for Windows only
- cx_Freeze for cross-platform

Distribution:
- Standalone executable
- Installation package
- Python package (PyPI)

=================================================================================
"""
