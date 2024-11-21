def calculate_discount(price, discount_percent):
    # If the discount is 20% or higher, apply the discount
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # If the discount is less than 20%, return the original price
        return price

# Prompt the user for the original price and discount percentage
price = float(input("Enter the original price of the item: $"))
discount_percent = float(input("Enter the discount percentage: "))

# Call the function and print the final price
final_price = calculate_discount(price, discount_percent)

# Print the result
if final_price == price:
    print(f"No discount applied. The price remains: ${final_price:.2f}")
else:
    print(f"Discount applied! The final price is: ${final_price:.2f}")
