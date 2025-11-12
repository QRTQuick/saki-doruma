"""
README for saki-doruma - Company Expense Manager

## Overview

saki-doruma is a professional-grade expense management and accounting application 
built with PySide6. It provides comprehensive tools for tracking company expenses, 
performing accounting calculations, and generating detailed financial reports.

## Features

### 💰 Expense Management
- Add, edit, and delete expenses
- Categorize expenses (Travel, Meals, Supplies, Equipment, etc.)
- Track payment methods (Cash, Credit Card, Debit Card, Bank Transfer, Check)
- Mark expenses as reimbursable
- Add notes and receipt paths
- Search and filter expenses by description, category, or date
- Export expense data to CSV

### 🧮 Advanced Calculator
- Mini calculator with expression evaluation
- Basic arithmetic operations (add, subtract, multiply, divide)
- Calculation history tracking

### 💼 Accounting Tools
- **VAT Calculator**: Calculate Value Added Tax on amounts
- **Tax Calculator**: Calculate income/corporate tax
- **Discount Calculator**: Apply discounts to amounts
- **Markup Calculator**: Calculate selling prices with markups
- **Profit Margin Calculator**: Analyze profit margins
- **Break-Even Analysis**: Determine break-even points
- **Interest Calculator**: Simple and compound interest calculations

### 📊 Analytics & Reporting
- Comprehensive expense statistics
  - Total expenses
  - Average, minimum, maximum expenses
  - Median expense value
  - Daily average spending
  - Reimbursable total
- Expense breakdown by category
- Expense breakdown by payment method
- Top 10 expenses display
- Monthly trend analysis
- Export analytics reports to text files

### 🎨 Professional UI
- Modern dark theme with accent colors
- Tabbed interface for easy navigation
- Statistical cards for quick insights
- Professional table widgets with sorting
- Responsive layout
- Keyboard shortcuts in menus

## Project Structure

```
saki-doruma/
├── main.py                 # Application entry point
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── README.md             # This file
│
├── data/                 # Data layer
│   ├── __init__.py
│   ├── models.py        # Data models (Expense, ExpenseReport, etc.)
│   └── database.py      # Database operations (JSON persistence)
│
├── modules/             # Business logic layer
│   ├── __init__.py
│   ├── calculator.py    # Calculator and accounting functions
│   ├── expense_manager.py  # Expense management operations
│   └── analytics.py     # Analytics and reporting logic
│
└── ui/                  # User interface layer
    ├── __init__.py
    ├── stylesheet.py    # Application styling and themes
    ├── widgets.py       # Custom widgets (cards, forms, tables)
    ├── main_window.py   # Main application window
    ├── expense_tab.py   # Expense management tab
    ├── calculator_tab.py # Calculator and accounting tools tab
    └── analytics_tab.py # Analytics and reporting tab
```

## Installation

### Requirements
- Python 3.9+
- PySide6

### Setup

1. Clone or download the project:
   ```bash
   cd saki-doruma
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python main.py
   ```

## Usage

### Adding Expenses
1. Click on the "Expenses" tab
2. Click "+ Add Expense" button
3. Fill in the expense details:
   - Description
   - Amount
   - Category
   - Payment Method
   - Date
   - Additional notes (optional)
4. Mark as reimbursable if applicable
5. Click "Add Expense"

### Searching and Filtering
- Use the search box to find expenses by description
- Use the category filter dropdown to view expenses by category
- Select an expense row to enable Edit and Delete buttons

### Using the Calculator
1. Navigate to the "Calculator" tab
2. **Basic Calculator**: Enter mathematical expressions and click "Calculate"
3. **Accounting Tools**: 
   - Enter the required values for each calculation type
   - Click the respective "Calculate" button
   - Results display in the output field

### Viewing Analytics
1. Go to the "Analytics" tab
2. View summary statistics at the top
3. Review expense breakdown by category and payment method
4. Check the top 10 expenses
5. Export report for record keeping

### Exporting Data
- **CSV Export**: From Expenses tab, click "⬇ Export CSV"
- **Report Export**: From Analytics tab, click "⬇ Export Report"

## Features Details

### Expense Categories
- Travel
- Meals & Dining
- Office Supplies
- Equipment
- Utilities
- Rent
- Insurance
- Salaries
- Maintenance
- Marketing
- Other

### Payment Methods
- Cash
- Credit Card
- Debit Card
- Bank Transfer
- Check
- Other

### Accounting Calculations

#### VAT Calculator
Calculates Value Added Tax:
- Base amount × VAT rate / 100 = VAT amount
- Total = Base amount + VAT amount

#### Tax Calculator
Calculates income/corporate tax:
- Gross amount × Tax rate / 100 = Tax amount
- Net amount = Gross amount - Tax amount

#### Discount Calculator
Applies discounts:
- Original amount × Discount % / 100 = Discount amount
- Final amount = Original amount - Discount amount

#### Markup Calculator
Calculates selling price with markup:
- Cost × Markup % / 100 = Markup amount
- Selling price = Cost + Markup amount

#### Profit Margin
Analyzes profitability:
- Profit = Revenue - Cost
- Margin % = (Profit / Revenue) × 100

#### Break-Even Analysis
Determines sales needed to cover costs:
- Break-even units = Fixed costs / (Unit price - Unit cost)
- Break-even revenue = Break-even units × Unit price

#### Interest Calculator
- Simple Interest: Principal × Rate × Time / 100
- Compound Interest: Principal × (1 + Rate/100)^Time

## Data Storage

The application uses JSON files for data persistence:
- `data/storage/expenses.json` - All expense records
- `data/storage/reports.json` - Generated reports

Data is automatically saved when you add, edit, or delete expenses.

## Styling and Themes

The application features a professional dark theme with:
- Custom accent colors (blues, greens, oranges)
- Rounded corners on UI elements
- Hover effects on buttons
- Color-coded buttons (add/green, delete/red, edit/orange, export/purple)
- Professional typography

## Advanced Features

### Statistics & Insights
- Real-time calculation of expense statistics
- Monthly trend analysis
- Daily spending averages
- Forecasting based on historical data

### Data Management
- JSON-based persistent storage
- Efficient searching and filtering
- Batch export capabilities
- Report generation

### User Experience
- Responsive tabbed interface
- Clear visual feedback
- Intuitive form layouts
- Professional status cards

## Keyboard Shortcuts

- File → Export Expenses: Export all expenses to CSV
- File → Exit: Close the application
- View → Toggle Dark/Light Mode: Switch between themes
- Help → About: Show about dialog

## Troubleshooting

### Application won't start
- Ensure Python 3.9+ is installed
- Install PySide6: `pip install PySide6`
- Check that all files are in the correct directories

### Data not saving
- Ensure `data/storage/` directory exists and is writable
- Check file permissions
- Try creating the directories manually

### Calculator errors
- Ensure mathematical expressions are valid
- Division by zero is handled with error messages

## Future Enhancements

Potential features for future versions:
- Database backend (SQLite, PostgreSQL)
- Receipt image storage and management
- Multiple user accounts
- Budget tracking and alerts
- Recurring expenses
- Multi-currency support
- Email report distribution
- Mobile app integration
- Advanced forecasting

## License

This project is provided as-is for educational and commercial use.

## Support

For issues, questions, or suggestions, please refer to the application's help menu.

---

**Version**: 1.0.0
**Last Updated**: November 2025
"""
