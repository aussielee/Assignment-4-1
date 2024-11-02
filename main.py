"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
charge = 0.00

# Get user inputs
numChars = int(input("Enter the numchar: "))
woodType = input("Enter the wood type (pine, oak): ").strip().lower()
color = input("Enter the color (black, white, gold): ").strip().lower()

# Base price for the sign
base_price = 35.00

# Additional cost per character
additional_char_cost = 4.00

# Additional cost for gold color
gold_color_cost = 15.00

# Additional cost for oak wood
oak_wood_cost = 20.00

# Calculate the charge
charge = base_price

# Add cost for additional characters beyond the first five
if numChars > 5:
    charge += (numChars - 5) * additional_char_cost

# Add cost for gold color
if color == "gold":
    charge += gold_color_cost

# Add cost for oak wood
if woodType == "oak":
    charge += oak_wood_cost

# Output Charge for this sign.
print("The charge for this sign is $" + "{:.1f}".format(charge))
