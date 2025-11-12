"""
Quick Start Guide for saki-doruma Expense Manager

INSTALLATION & SETUP
====================

1. Navigate to the project directory:
   cd c:\Users\DELL\OneDrive\Pictures\saki-doruma

2. Install required dependencies:
   pip install -r requirements.txt

3. Run the application:
   python main.py

FIRST TIME SETUP
================

When you first launch the application:
- The application automatically creates necessary directories
- A data/storage/ directory is created for storing expense records
- An exports/ directory is created for report exports

THE INTERFACE
=============

Main Window Layout:
┌─────────────────────────────────────────────────────┐
│ File  View  Help                                    │
├─────────────────────────────────────────────────────┐
│  💰 Expenses  │  🧮 Calculator  │  📊 Analytics    │
├──────────────────────────────────────────────────────┤
│                                                      │
│                    Tab Content                      │
│                                                      │
└──────────────────────────────────────────────────────┘

TABS OVERVIEW
=============

1. 💰 EXPENSES TAB
   - Add new expenses with full details
   - View all expenses in a searchable table
   - Filter by category or payment method
   - Edit or delete existing expenses
   - Export data to CSV
   - Statistics cards showing totals and averages

2. 🧮 CALCULATOR TAB
   - Basic Calculator: Mathematical expressions
   - VAT Calculator: Calculate sales tax/VAT
   - Tax Calculator: Income/corporate tax
   - Discount Calculator: Apply discounts
   - Markup Calculator: Calculate selling prices
   - Profit Margin: Analyze profitability
   - Break-Even: Find break-even points
   - Interest Calculator: Simple/compound interest

3. 📊 ANALYTICS TAB
   - Comprehensive expense statistics
   - Expense breakdown by category (with percentages)
   - Expense breakdown by payment method
   - Top 10 expenses view
   - Daily average spending
   - Export detailed reports

QUICK TASKS
===========

Adding Your First Expense:
1. Click on the "Expenses" tab
2. Click the "+ Add Expense" button
3. Fill in the form:
   - Description: e.g., "Office Supplies"
   - Amount: e.g., 150.00
   - Category: Select from dropdown
   - Payment Method: Select from dropdown
   - Date: Select date
   - Notes: Optional additional info
4. Check "Reimbursable" if needed
5. Click "Add Expense"

Finding an Expense:
1. Use the search box to type a description
2. Or select a category from the filter dropdown
3. Click on the expense in the table to select it
4. Click "Edit" or "Delete" as needed

Calculating VAT:
1. Go to Calculator tab
2. Click "Accounting Tools"
3. Click "VAT Calculator" sub-tab
4. Enter base amount and VAT rate
5. Click "Calculate VAT"
6. See results immediately

Viewing Analytics:
1. Go to Analytics tab
2. View statistics cards at the top
3. Scroll down to see category breakdown
4. Check payment method distribution
5. Review top 10 expenses
6. Click "Export Report" to save as text file

DATA MANAGEMENT
===============

Where is my data stored?
- All expense records: data/storage/expenses.json
- All reports: data/storage/reports.json
- Data is saved automatically

Backing up your data:
- Copy the data/storage/ folder to a safe location
- Backup the entire project folder regularly

FEATURES BY TAB
===============

EXPENSES TAB:
✓ Add expenses with full metadata
✓ Edit existing expenses
✓ Delete expenses with confirmation
✓ Search by description
✓ Filter by category
✓ Statistics display (total, count, average)
✓ Export to CSV
✓ Table view with sorting capability

CALCULATOR TAB:
✓ Expression evaluator
✓ Calculation history
✓ VAT/Tax calculations
✓ Discount and markup calculations
✓ Profit margin analysis
✓ Break-even calculations
✓ Simple and compound interest

ANALYTICS TAB:
✓ Statistical summary (min, max, average, median)
✓ Daily average tracking
✓ Reimbursable totals
✓ Category distribution with percentages
✓ Payment method breakdown
✓ Top expenses ranking
✓ Export reports to text format

PROJECT STRUCTURE
=================

saki-doruma/
├── main.py                    # Start here!
├── config.py                  # Configuration settings
├── requirements.txt           # Dependencies
├── README.md                  # Full documentation
│
├── data/
│   ├── models.py             # Expense and Report models
│   └── database.py           # Data persistence layer
│
├── modules/
│   ├── calculator.py         # Calculator logic
│   ├── expense_manager.py    # Expense operations
│   └── analytics.py          # Analytics calculations
│
└── ui/
    ├── stylesheet.py         # Dark theme styling
    ├── widgets.py            # Custom UI widgets
    ├── main_window.py        # Main application window
    ├── expense_tab.py        # Expense management interface
    ├── calculator_tab.py     # Calculator interface
    └── analytics_tab.py      # Analytics interface

KEYBOARD SHORTCUTS
==================

File Menu:
- Export Expenses: Export current data to CSV
- Exit: Close the application

View Menu:
- Toggle Dark/Light Mode: Switch theme (coming soon)

Help Menu:
- About: Show application information

COMMON OPERATIONS
=================

Add Multiple Expenses:
1. Click "Add Expense"
2. Fill form and click "Add Expense"
3. Repeat for each expense

Batch Export:
1. Go to Expenses tab
2. Click "⬇ Export CSV"
3. Choose location and filename
4. Data exported as CSV file

Review Monthly Expenses:
1. Go to Analytics tab
2. View statistics at top
3. Category breakdown shows monthly totals
4. Export report for records

TROUBLESHOOTING
===============

Problem: Application won't start
Solution: 
- Check Python version (3.9+)
- Run: pip install --upgrade PySide6
- Try: python main.py

Problem: Data not saving
Solution:
- Check if data/storage/ exists
- Run application with admin privileges
- Check disk space

Problem: Calculator errors
Solution:
- Use valid mathematical expressions
- Example: 100 * 1.2 + 50
- Avoid division by zero

TIPS & TRICKS
=============

1. Use descriptive names for expenses
   - Good: "Office Supplies - Printer Paper"
   - Avoid: "Stuff"

2. Set dates carefully for accurate analytics
3. Use categories consistently
4. Mark reimbursable expenses for tracking
5. Export reports regularly for backups
6. Review analytics monthly for insights

SYSTEM REQUIREMENTS
===================

Minimum:
- Python 3.9+
- 50MB disk space
- 200MB RAM

Recommended:
- Python 3.10+
- 100MB disk space
- 512MB RAM
- Solid State Drive for faster data access

SUPPORT & HELP
==============

For more information:
1. See README.md for comprehensive documentation
2. Check Help menu in the application
3. Review inline tooltips on buttons and fields

VERSION & UPDATES
=================

Current Version: 1.0.0
Last Updated: November 2025

FEATURES CHECKLIST
==================

✓ Add/Edit/Delete expenses
✓ Multiple categories
✓ Multiple payment methods
✓ Advanced calculator
✓ Accounting tools
✓ Analytics and reports
✓ Data export (CSV)
✓ Professional UI
✓ Dark theme
✓ Search and filter
✓ Statistics
✓ Break-even analysis

NEXT STEPS
==========

1. Install the application
2. Add your first expense
3. Explore each tab
4. Try the calculator features
5. Review your analytics
6. Export a report
7. Familiarize yourself with all features

Enjoy using saki-doruma! 🎉
"""
