"""Sarah's Tickets"""
# This showcases a ticketing system that keeps track of tickets and drink packages for a theatrical event.

# Assign menu items and prices to lists for tickets and drinks
ticket_names = ["Standard Ticket", "VIP Ticket"]
ticket_prices = [35, 60]

drink_names = ["Wine Package", "Champagne Package"]
drink_prices = [30, 35]

# Create a list to build the customer's cart
cart_items = []
cart_prices = []

# Common input statements utilised
select = "Enter the number of the option you would like to choose:\n"
invalid = "This is not a valid option. Please enter a valid number."

# Display the ticketing menu options until checkout
done = False
while (not done):
    print("\n")
    print("-" * 80)
    print("Welcome to Sarah's Tickets!")


# Menu options
    print("-" * 80)
    print("Would you like to: ")
    print("1. Add a ticket to your cart")
    print("2. Remove a ticket from your cart")
    print("3. Add a drink package to your cart")
    print("4. Remove a drink package from your cart")
    print("5. View your cart")
    print("6. Checkout")
    choice = input(select)

# Select a ticket type to add to cart
    if choice == "1":
        print("What ticket type would you like:")
        print("1. Standard Ticket (£25)")
        print("2. VIP Ticket (£50)")
        ticket_selection = input(select)

        # Input how many tickets to add
        while True:
            try:
                ticket_amount = int(input("How many tickets would you like to buy? "))
                break
            except ValueError:
                print(invalid)

        # Add Standard Ticket to cart
        if ticket_selection == "1":
            cart_items.extend([ticket_names[0]] * ticket_amount)
            cart_prices.extend([ticket_prices[0]] * ticket_amount)
            print(f"{ticket_amount} {ticket_names[0]}(s) have been added to your cart successfully.")
            
        # Add VIP Ticket to cart
        elif ticket_selection == "2":
            cart_items.extend([ticket_names[1]] * ticket_amount)
            cart_prices.extend([ticket_prices[1]] * ticket_amount)
            print(f"{ticket_amount} {ticket_names[1]}(s) have been added to your cart successfully.")

        else:
            print(invalid)

    # Select a ticket type to remove from cart
    elif choice == "2":
        print("What ticket type would you like to remove:")
        print("1. Standard Ticket (£25)")
        print("2. VIP Ticket (£50)")
        ticket_selection = input(select)

        # Input how many tickets to remove
        while True:
            try:
                ticket_amount = int(input("How many tickets would you like to remove? "))
                break
            except ValueError:
                print(invalid)

        # Remove Standard Ticket from cart
        if ticket_selection == "1":
            cart_items.remove(ticket_names[0] * ticket_amount)
            cart_prices.remove(ticket_prices[0] * ticket_amount)
            print(f"{ticket_amount} {ticket_names[0]}(s) have been removed from your cart successfully.")

        # Remove VIP Ticket from cart
        elif ticket_selection == "2":
            cart_items.remove(ticket_names[1] * ticket_amount)
            cart_prices.remove(ticket_prices[1] * ticket_amount)
            print(f"{ticket_amount} {ticket_names[1]}(s) have been removed from your cart successfully.")
        
        else:
            print(invalid)

    # Select a drink package to add to cart
    elif choice == "3":
        print("What drink package would you like:")
        print("1. Wine Package - 2 glasses of wine provided upon arrival (£25)")
        print("2. Champagne Package - 2 glasses of champagne provided upon arrival (£30) ")
        package_selection = input(select)

        # Input how many drink packages to add
        while True:
            try:
                package_amount = int(input("How many drink packages would you like to add to your order? "))
                break
            except ValueError:
                print(invalid)

        # Add Wine Package to cart
        if package_selection == "1":
            cart_items.extend([drink_names[0]] * package_amount)
            cart_prices.extend([drink_prices[0]] * package_amount)
            print(f"{package_amount} {drink_names[0]}(s) has been added to your cart successfully.")

        # Add Champagne Package to cart
        elif package_selection == "2":
            cart_items.extend([drink_names[1]] * package_amount)
            cart_prices.extend([drink_prices[1]] * package_amount)
            print(f"{package_amount} {drink_names[1]}(s) have been added to your cart successfully.")
        
        else:
            print(invalid)

    # Select drink package to remove from cart
    elif choice == "4":
        print("What drink package would you like to remove:")
        print("1. Wine Package - 2 glasses of wine provided upon arrival (£25)")
        print("2. Champagne Package - 2 glasses of champagne provided upon arrival (£30) ")
        package_selection = input(select)

        # Input how many packages to remove
        while True:
            try:
                package_amount = int(input("How many drink packages would you like to remove? "))
                break
            except ValueError:
                print(invalid)

        # Remove Wine Package from cart
        if package_selection == "1":
            cart_items.remove(drink_names[0] * package_amount)
            cart_prices.remove(drink_prices[0] * package_amount)
            print(f"{package_amount} {drink_names[0]}(s) have been removed from your cart successfully.")

        # Remove Champagne Package from cart
        elif package_selection == "2":
            cart_items.remove(drink_names[1] * package_amount)
            cart_prices.remove(drink_prices[1] * package_amount)
            print(f"{package_amount} {drink_names[1]}(s) have been removed from your cart successfully.")
        
        else:
            print(invalid)

    # View cart of tickets and drink packages with prices listed next to each item and the total cost
    elif choice == "5":
        print("Your cart is:")
        cart = list(zip(cart_items, cart_prices))
        for i, p in cart:
            print(f"{i} (£{p})")
        print("-" * 3)
        print(f"Your cart total is: £{sum(cart_prices)} ")

    # Exit from the programme
    elif choice == "6":
        print("Thank you for your purchase. We look forward to welcoming you at the show!")
        done = True

    else:
        print(invalid)