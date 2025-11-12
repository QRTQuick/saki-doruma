"""
EXAMPLE USAGE & WORKFLOWS
saki-doruma - Company Expense Manager

=================================================================================
EXAMPLE 1: BASIC EXPENSE ENTRY
=================================================================================

Scenario: Adding a travel expense for a business trip

Steps:
1. Launch application: python main.py
2. Click "Expenses" tab
3. Click "+ Add Expense" button
4. Fill in the form:
   - Description: "Flight to New York - Business Conference"
   - Amount: 450.00
   - Category: Travel
   - Payment Method: Credit Card
   - Date: [Today's date]
   - Notes: "Delta Airlines, Conference trip for Q4 planning"
5. Click "Add Expense"

Result: Expense added to database and displayed in table

Database entry (expenses.json):
{
  "id": "a1b2c3d4-e5f6-47g8-h9i0-j1k2l3m4n5o6",
  "description": "Flight to New York - Business Conference",
  "amount": 450.00,
  "category": "Travel",
  "payment_method": "Credit Card",
  "date": "2025-11-12T00:00:00",
  "notes": "Delta Airlines, Conference trip for Q4 planning",
  "receipt_path": null,
  "is_reimbursable": false,
  "created_at": "2025-11-12T14:30:00",
  "updated_at": "2025-11-12T14:30:00"
}

=================================================================================
EXAMPLE 2: CALCULATING VAT ON PURCHASE
=================================================================================

Scenario: Company purchases office equipment for $2,000 + VAT

Steps:
1. Go to "Calculator" tab
2. Click "Accounting Tools"
3. Click "VAT Calculator" tab
4. Enter:
   - Base Amount: 2000.00
   - VAT Rate: 20
5. Click "Calculate VAT"

Result displayed:
Base: $2,000.00 | VAT: $400.00 | Total: $2,400.00

Use case: 
- Understand total cost of purchase
- Record expense with VAT amount
- Track VAT liability for tax purposes

=================================================================================
EXAMPLE 3: ANALYZING PROFIT MARGIN
=================================================================================

Scenario: Product costs $100 to make, sells for $250

Steps:
1. Go to "Calculator" tab
2. Click "Accounting Tools"
3. Click "Profit Margin" tab
4. Enter:
   - Revenue: 250.00
   - Cost: 100.00
5. Click "Calculate Margin"

Result displayed:
Revenue: $250.00 | Profit: $150.00 | Margin: 60.00%

Interpretation:
- 60% profit margin is excellent
- For every $1 spent, make $1.50 profit
- Business is operating at healthy margins

=================================================================================
EXAMPLE 4: BREAK-EVEN ANALYSIS
=================================================================================

Scenario: Coffee shop analyzing break-even point
- Fixed costs: $5,000/month (rent, utilities, salaries)
- Price per coffee: $5.00
- Cost per coffee: $1.50

Steps:
1. Go to "Calculator" tab
2. Click "Accounting Tools"
3. Click "Break-Even" tab
4. Enter:
   - Fixed Costs: 5000.00
   - Unit Price: 5.00
   - Unit Cost: 1.50
5. Click "Calculate Break-Even"

Result displayed:
Units: 1667 | Revenue: $8,335.00

Interpretation:
- Need to sell 1,667 coffees to break even
- At 100 coffees/day, breaks even in ~17 days
- Anything sold after break-even is profit

=================================================================================
EXAMPLE 5: MONTHLY EXPENSE REVIEW
=================================================================================

Scenario: Manager wants to review November expenses

Steps:
1. Go to "Analytics" tab
2. View statistics cards at top
3. See category breakdown table
4. See payment method distribution
5. Review top 10 expenses
6. Click "⬇ Export Report"
7. Save to file: "November_Expenses.txt"

Example Output:
============================================================
EXPENSE ANALYTICS REPORT
============================================================

SUMMARY STATISTICS
------------------------------------------------------------
Total Expenses: $15,250.00
Number of Transactions: 145
Average Expense: $105.17
Minimum: $5.00
Maximum: $2,450.00
Median: $75.00

CATEGORY BREAKDOWN
------------------------------------------------------------
Travel: $4,500.00 (29.5%) - 8 transactions
Meals & Dining: $2,100.00 (13.8%) - 42 transactions
Office Supplies: $1,800.00 (11.8%) - 35 transactions
Equipment: $2,450.00 (16.0%) - 2 transactions
Other: $4,400.00 (28.8%) - 58 transactions

============================================================
Report Generated: 2025-11-12 14:45:30

=================================================================================
EXAMPLE 6: SEARCHING SPECIFIC EXPENSES
=================================================================================

Scenario: Manager needs to find all meal expenses related to a client

Steps:
1. Go to "Expenses" tab
2. In search box type: "Client lunch"
3. Press Enter or wait for real-time filter
4. Table updates showing matching results

Results might show:
| Description               | Amount | Category      | Date       |
|---------------------------|--------|---------------|-----------|
| Client lunch - ABC Corp   | $85.00 | Meals & Dining| 11-10-2025|
| Client lunch - XYZ Inc    | $120.00| Meals & Dining| 11-08-2025|
| Client lunch follow-up    | $65.00 | Meals & Dining| 11-05-2025|

Alternative: Use category filter dropdown
- Select "Meals & Dining"
- View only meal expenses
- Get total spending on meals

=================================================================================
EXAMPLE 7: EDITING AN EXPENSE
=================================================================================

Scenario: Amount was entered incorrectly for an expense

Steps:
1. Go to "Expenses" tab
2. Find and click on the expense row
3. Click "✎ Edit" button
4. In dialog, modify:
   - From Amount: $150.00
   - To Amount: $175.00
5. Click "Update Expense"

Result:
- Expense updated in database
- Table refreshed with new amount
- Statistics recalculated automatically
- Updated timestamp recorded

=================================================================================
EXAMPLE 8: EXPORTING DATA
=================================================================================

Scenario: Finance team needs expense data for accounting software

Steps:
1. Go to "Expenses" tab
2. Click "⬇ Export CSV" button
3. Choose location: C:\Reports\
4. Filename: expenses_nov2025.csv
5. Click Save

CSV Format:
id,description,amount,category,payment_method,date,notes,...
a1b2c3d4,Office Supplies,150.00,Office Supplies,Credit Card,2025-11-12,...
e5f6g7h8,Lunch meeting,85.00,Meals & Dining,Cash,2025-11-12,...
i9j0k1l2,Hotel,250.00,Travel,Credit Card,2025-11-12,...

Can be imported into:
- Excel/Google Sheets
- Accounting software (QuickBooks, Xero)
- Database systems
- Business intelligence tools

=================================================================================
EXAMPLE 9: TAX CALCULATION
=================================================================================

Scenario: Calculate taxes on company income

Situation:
- Company gross income: $100,000
- Tax rate: 21% (federal corporate tax)

Steps:
1. Go to "Calculator" tab
2. Click "Accounting Tools"
3. Click "Tax Calculator"
4. Enter:
   - Gross Amount: 100000.00
   - Tax Rate: 21
5. Click "Calculate Tax"

Result displayed:
Gross: $100,000.00 | Tax: $21,000.00 | Net: $79,000.00

Interpretation:
- Taxes owed: $21,000
- Net income: $79,000
- Effective tax rate: 21%

=================================================================================
EXAMPLE 10: SIMPLE INTEREST CALCULATION
=================================================================================

Scenario: Calculate interest on company loan

Parameters:
- Loan amount (principal): $50,000
- Interest rate: 5% annually
- Time: 2 years

Steps:
1. Go to "Calculator" tab
2. Click "Accounting Tools"
3. Click "Interest Calculator"
4. Enter:
   - Principal: 50000.00
   - Rate: 5
   - Time: 2
   - Type: Simple Interest
5. Click "Calculate Interest"

Result displayed:
Principal: $50,000.00 | Interest: $5,000.00 | Total: $55,000.00

Calculation:
Interest = (50,000 × 5 × 2) / 100 = $5,000

Use for:
- Loan repayment planning
- Interest expense tracking
- Financial forecasting

=================================================================================
EXAMPLE 11: COMPOUND INTEREST CALCULATION
=================================================================================

Scenario: Calculate compound interest on company savings

Parameters:
- Initial investment: $100,000
- Interest rate: 4% annually
- Time: 5 years
- Compounds: 4 times per year (quarterly)

Steps:
1. Go to "Calculator" tab
2. Click "Accounting Tools"
3. Click "Interest Calculator"
4. Enter:
   - Principal: 100000.00
   - Rate: 4
   - Time: 5
   - Type: Compound Interest
5. Click "Calculate Interest"

Result displayed:
Principal: $100,000.00 | Interest: $21,911.23 | Total: $121,911.23

Formula:
Amount = 100,000 × (1 + 0.04/4)^(4×5) = $121,911.23

Advantage over simple interest:
- Additional $1,911.23 from compounding effect
- Shows power of compound interest over time

=================================================================================
EXAMPLE 12: DISCOUNT CALCULATION FOR BULK PURCHASE
=================================================================================

Scenario: Supplier offers 15% discount on $10,000 order

Steps:
1. Go to "Calculator" tab
2. Click "Accounting Tools"
3. Click "Discount Calculator"
4. Enter:
   - Original Amount: 10000.00
   - Discount: 15
5. Click "Calculate Discount"

Result displayed:
Original: $10,000.00 | Discount: $1,500.00 | Final: $8,500.00

Use case:
- Negotiate bulk purchases
- Track savings
- Budget planning
- Supplier cost comparison

=================================================================================
EXAMPLE 13: MARKUP CALCULATION FOR RESALE
=================================================================================

Scenario: Product costs $100, apply 50% markup

Steps:
1. Go to "Calculator" tab
2. Click "Accounting Tools"
3. Click "Markup Calculator"
4. Enter:
   - Cost: 100.00
   - Markup: 50
5. Click "Calculate Markup"

Result displayed:
Cost: $100.00 | Markup: $50.00 | Price: $150.00

Variations:
- 20% markup: Selling price = $120
- 50% markup: Selling price = $150
- 100% markup: Selling price = $200 (double cost)

Use for:
- Setting product prices
- Determining profit targets
- Competitive pricing analysis

=================================================================================
EXAMPLE 14: MULTI-STEP FINANCIAL ANALYSIS
=================================================================================

Scenario: Complete financial analysis of a product line

Product Details:
- Sells for: $50 per unit
- Costs: $20 per unit
- Monthly fixed costs: $10,000
- Current sales: 500 units/month

Analysis Steps:

Step 1: Calculate Markup
- Markup Calculator
- Cost: 20, Selling: 50
- Markup: 150% ✓

Step 2: Calculate Profit Margin
- Profit Margin Calculator
- Revenue: 50, Cost: 20
- Margin: 60% ✓

Step 3: Calculate Break-Even
- Break-Even Calculator
- Fixed costs: 10,000
- Unit price: 50, Unit cost: 20
- Break-even: 334 units
- Current sales: 500 > 334 ✓ (Profitable!)

Step 4: Calculate Expected Profit
- Profit = (50 - 20) × 500 - 10,000
- Profit = $15,000 - $10,000 = $5,000

Conclusion: Product line is profitable with healthy margins

=================================================================================
EXAMPLE 15: MANAGING REIMBURSABLE EXPENSES
=================================================================================

Scenario: Employee reimburses personal meal expense

Initial Entry:
1. Add expense:
   - Description: "Team lunch - Reimbursable"
   - Amount: $120.00
   - Category: Meals & Dining
   - Payment Method: Cash
   - Check "Reimbursable"

Later Review:
1. Go to "Analytics" tab
2. View "Reimbursable Total" card
3. Shows: $120.00 to be reimbursed
4. Export report shows all reimbursable items
5. Use for:
   - Expense reimbursement tracking
   - Employee reimbursement processing
   - Budget allocation

=================================================================================
WORKFLOW OPTIMIZATION TIPS
=================================================================================

Efficient Expense Entry:
1. Batch entries: Enter multiple expenses at once
2. Use consistent descriptions
3. Set dates immediately
4. Add notes for clarification
5. Mark reimbursables as you go

Efficient Searching:
1. Use specific search terms
2. Filter by category first
3. Export then analyze in spreadsheet
4. Use date range filters

Efficient Reporting:
1. Generate monthly reports
2. Review quarterly
3. Export and archive
4. Compare month-to-month trends

Calculator Usage:
1. Keep calculator open for quick calculations
2. Use for pricing decisions
3. Reference for financial meetings
4. Document important calculations

Analytics Reviews:
1. Monthly review habit
2. Compare to previous months
3. Watch for spending trends
4. Identify cost-saving opportunities

=================================================================================
COMMON CALCULATIONS QUICK REFERENCE
=================================================================================

VAT (20% rate):
Amount × 1.20 = Total with VAT
Example: $1,000 × 1.20 = $1,200

Tax (21% rate):
Amount × 0.21 = Tax owed
Example: $100,000 × 0.21 = $21,000

Discount (15% off):
Amount × (1 - 0.15) = Final price
Example: $1,000 × 0.85 = $850

Markup (50% profit):
Cost × 1.50 = Selling price
Example: $100 × 1.50 = $150

Profit Margin:
(Revenue - Cost) / Revenue × 100 = %
Example: ($250 - $100) / $250 × 100 = 60%

Break-Even:
Fixed Costs / (Price - Cost) = Units
Example: $5,000 / ($5 - $1.50) = 1,667 units

=================================================================================
DATA BACKUP WORKFLOW
=================================================================================

Daily Backup:
1. Use Windows backup feature
2. Include data/storage/ folder
3. Cloud sync (OneDrive, Google Drive)

Weekly Backup:
1. Copy entire saki-doruma folder
2. Store on external drive
3. Name: saki-doruma-backup-2025-11-12

Monthly Archive:
1. Export all data to CSV
2. Export all reports
3. Create PDF summary
4. Store in archive folder

Recovery Procedure:
1. Copy data/storage/ from backup
2. Restart application
3. Verify data integrity
4. Check statistics

=================================================================================
"""
