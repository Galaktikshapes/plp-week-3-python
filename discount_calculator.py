def calculate_discount(price, discount_percent):
    # If the discount is 20% or more, apply the discount
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        # If the discount is less than 20%, don't apply any discount
        return price

# Ask the user to enter the original price and the discount percentage
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Call the function to calculate the final price
    final_price = calculate_discount(price, discount_percent)

    # Let the user know if a discount was applied or not
    if discount_percent >= 20:
        print(f"Discount applied. Final price: R{final_price:.2f}")
    else:
        print(f"No discount applied. Final price: R{final_price:.2f}")

# Catch any input errors (like typing in letters instead of numbers)
except ValueError:
    print("Oops! Please enter valid numbers for both price and discount.")
