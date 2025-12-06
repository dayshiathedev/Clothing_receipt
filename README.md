# Clothing Receipt Generator 🧾

A small Python project that generates a receipt for a clothing store.  
It uses item prices, quantities, tax, and nicely formatted output to show a clear final total.

## Features

- Defines prices for multiple clothing items (shirts, jean jackets, hoodies)
- Uses quantities to calculate line-item subtotals
- Calculates:
  - Cart subtotal
  - Tax amount
  - Final total
- Prints a clean, readable receipt using f-strings and two-decimal money format

## What I Practiced

This project helped me practice:

- Variables for prices and quantities
- Basic arithmetic (`+`, `*`)
- Calculating tax
- Using `print()` with labels and values
- Formatting money with f-strings: `f"${value:.2f}"`

## How to Run

1. Make sure you have Python installed.
2. Clone this repository:

   ```bash
   git clone https://github.com/dayshiathedev/Clothing_receipt.git
   cd Clothing_receipt
   ```

3. Run the script:

   ```bash
   python clothing_receipt.py
   ```

(Replace `clothing_receipt.py` with your actual file name if it’s different.)

## Possible Improvements

In the future, I might:

- Add a store name and discounts
- Add more items or categories
- Let the user choose quantities (later, when I learn about input)

---

Thank you for checking out my project!
