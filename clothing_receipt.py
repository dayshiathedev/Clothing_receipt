def print_divider():
    print("--------------------------")
def print_receipt(shirt_qty, jean_jacket_qty, hoodie_qty):
    shirt_price = 5.03
    jean_jacket_price = 8.16
    hoodie_price = 10.35
    tax = 0.08

    shirt_total = shirt_price * shirt_qty
    jean_jacket_total = jean_jacket_price * jean_jacket_qty
    hoodie_total = hoodie_price * hoodie_qty

    cart_subtotal = shirt_total + jean_jacket_total + hoodie_total
    tax_amount = cart_subtotal * tax
    total_with_tax = cart_subtotal + tax_amount

    print("----- Receipt -----")
    print(f"Shirts (x{shirt_qty}): ${shirt_total:.2f}")
    print(f"Jean jackets (x{jean_jacket_qty}): ${jean_jacket_total:.2f}")
    print(f"Hoodies (x{hoodie_qty}): ${hoodie_total:.2f}")
    print("--------------------------")
    print(f"Subtotal: ${cart_subtotal:.2f}")
    print(f"Tax: ${tax_amount:.2f}")
    print(f"Your total today is ${total_with_tax:.2f}")
    print("---------------------------")
    print("Thank you for shopping with us!")


print_receipt(3, 2, 2)
print_receipt(1, 0, 5)  # 1 shirt, 0 jackets, 5 hoodies