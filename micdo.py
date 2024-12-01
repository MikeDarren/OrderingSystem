from collections import defaultdict

recent_orders = []
all_orders = []
total_earnings = 0.0

def menu():
    print(" [1] Chicken \t\t [2] Burger ")
    print(" [3] Breakfast Meal\t [4] Drinks \n")

def chicken_meal():
    print(" [1] 1pc. Chicken MicDo with Medium IcedTea Meal \t\t "
          "[2] 8pc. Chicken MicNuggets with Rice and Coke Meal")
    print(" [3] 2pc. MicCrispy Chicken Fillet King with Rice and Coke Meal\t "
          "[4] 2pcs. Chicken MicDo with Rice and Coke Meal \n")

def burger_meal():
    print(" [1] YumMic Cheeseburger with MicFloat Meal \t\t "
          "  [2] YummyMic Double Cheeseburger with Fries and Coke Meal")
    print(" [3] Quarter Pounder with Cheese with Fries and Coke Meal"
          "  [4] Big Mac CheesyMic Burger with Fries and Coke Meal \n")

def breakfast_meal():
    print(" [1] MicDo Tapsilog with IcedTea Meal \t\t          [2] MicDo Tosilog with IcedTea Meal")
    print(" [3] MicDo Hotsilog with IcedTea Meal\t\t          [4] MicDo Sizzling Porksilog with Coke Meal \n")

def drinks_meal():
    print(" [1] Medium Coke MicFloat  \t\t  [2] Medium Iced Coffee Original with Vanilla")
    print(" [3] MicCaf'e Coffee Float  \t\t  [4] Medium Fries and Monster Coke MiCFloat \n")

def show_recent_orders(customer_number):
    if recent_orders:
        print("=======================")
        print(f"Customer {customer_number}:")

        total = 0.0
        for order, price in recent_orders:
            print(f"{order} - Php {price:.2f}")
            total += price
        print(f"Total: Php {total:.2f}")
        print("=======================\n")
        return total
    return 0.0

def show_all_orders():
    print("=======================")
    print("\nAll Orders of the Day:\n")
    print("=======================")
    customer_number = 1
    for orders in all_orders:
        print(f"Customer {customer_number}:")
        total = 0.0
        for order, price in orders:
            print(f"{order} - Php {price:.2f}")
            total += price
        print(f"Total: Php {total:.2f}")
        print("=======================\n")
        customer_number += 1

def show_total_earnings():
    print("=======================")
    print("Total Earnings for the Day:")
    print(f"Php {total_earnings:.2f}")
    print("=======================\n")

def checkout(customer_number):
    total = show_recent_orders(customer_number)
    if total:

        while True:
            try:
                amount_paid = float(input("Enter the amount you will pay: Php "))
                if amount_paid < total:
                    print(f"Insufficient payment. You need Php {total - amount_paid:.2f} more.")
                else:
                    change = amount_paid - total
                    print("\nProcessing your payment...")
                    print("Payment successful! Here is your receipt:\n")
                    print("=======================")
                    print(f"Receipt for Customer {customer_number}")
                    print("=======================")
                    total_price = 0.0
                    for order, price in recent_orders:
                        print(f"{order} - Php {price:.2f}")
                        total_price += price
                    print("=======================")
                    print(f"Total Orders: Php {total_price:.2f}")
                    print(f"Amount Paid: Php {amount_paid:.2f}")
                    print(f"Change: Php {change:.2f}")
                    print("=======================")
                    print("Thank you for your purchase!\n")
                    print("Thank you for visiting MiCDO! We hope to see you again!\n")
                    return True
            except ValueError:
                print("Invalid input. Please enter a valid numeric amount.")
    return False

def cancel_order():
    print("Your order has been canceled. Proceeding to the next customer.\n")

def main():
    global total_earnings
    prices = [
        [129.0, 149.0, 135.0, 199.0],
        [99.0, 119.0, 169.0, 199.0],
        [89.0, 89.0, 89.0, 139.0],
        [49.0, 69.0, 99.0, 119.0]
    ]

    print("=======================")
    print("* Welcome to MiCDO! *")

    customer_number = 1

    while True:
        print("=======================\n")
        print(f"*   Welcome Customer {customer_number}!  *")
        print("\n=======================\n")

        print("=======================")
        print("*        MENU           *")
        print("=======================\n")
        menu()

        menu_no = int(input("Please select your order: "))
        print()

        if menu_no == 1:
            print("=======================")
            print("*      Chicken Meal     *")
            print("=======================\n")
            chicken_meal()
            meal_choice = int(input("Enter your choice: "))
            if 1 <= meal_choice <= 4:
                meal_names = [
                    "1pc. Chicken MicDo with Medium IcedTea Meal",
                    "8pc. Chicken MicNuggets with Rice and Coke Meal",
                    "2pc. MicCrispy Chicken Fillet King with Rice and Coke Meal",
                    "2pcs. Chicken MicDo with Rice and Coke Meal"
                ]
                selected_order = meal_names[meal_choice - 1]
                cost = prices[0][meal_choice - 1]
                print(f"Your Order is: {selected_order}")
                print(f"Cost: Php {cost:.2f}")
                recent_orders.append((selected_order, cost))

        elif menu_no == 2:
            print("=======================")
            print("*       Burger Meal      *")
            print("=======================\n")
            burger_meal()
            meal_choice = int(input("Enter your choice: "))
            if 1 <= meal_choice <= 4:
                meal_names = [
                    "YumMic Cheeseburger with MicFloat Meal",
                    "YummyMic Double Cheeseburger with Fries and Coke Meal",
                    "Quarter Pounder with Cheese with Fries and Coke Meal",
                    "Big Mac CheesyMic Burger with Fries and Coke Meal"
                ]
                selected_order = meal_names[meal_choice - 1]
                cost = prices[1][meal_choice - 1]
                print(f"Your Order is: {selected_order}")
                print(f"Cost: Php {cost:.2f}")
                recent_orders.append((selected_order, cost))

        elif menu_no == 3:
            print("=======================")
            print("*    Breakfast Meal     *")
            print("=======================\n")
            breakfast_meal()
            meal_choice = int(input("Enter your choice: "))
            if 1 <= meal_choice <= 4:
                meal_names = [
                    "MicDo Tapsilog with IcedTea Meal",
                    "MicDo Tosilog with IcedTea Meal",
                    "MicDo Hotsilog with IcedTea Meal",
                    "MicDo Sizzling Porksilog with Coke Meal"
                ]
                selected_order = meal_names[meal_choice - 1]
                cost = prices[2][meal_choice - 1]
                print(f"Your Order is: {selected_order}")
                print(f"Cost: Php {cost:.2f}")
                recent_orders.append((selected_order, cost))

        elif menu_no == 4:
            print("=======================")
            print("*       Drinks          *")
            print("=======================\n")
            drinks_meal()
            drink_choice = int(input("Enter your choice: "))
            if 1 <= drink_choice <= 4:
                drink_names = [
                    "Medium Coke MicFloat",
                    "Medium Iced Coffee Original with Vanilla",
                    "MicCaf'e Coffee Float",
                    "Medium Fries and Monster Coke MiCFloat"
                ]
                selected_order = drink_names[drink_choice - 1]
                cost = prices[3][drink_choice - 1]
                print(f"Your Order is: {selected_order}")
                print(f"Cost: Php {cost:.2f}")
                recent_orders.append((selected_order, cost))

        else:
            print("Invalid menu option. Please try again.")

        next_step = input("Do you want to checkout, add another order or cancel your order? (checkout/add/cancel): ").lower()
        if next_step == "checkout":
            if checkout(customer_number):
                total_earnings += sum(price for _, price in recent_orders)
                all_orders.append(recent_orders.copy())
                recent_orders.clear()
                customer_number += 1

                if input("Do you want to see all orders of the day? (y/n): ").lower() == 'y':
                    show_all_orders()
                    show_total_earnings()
                    break
            else:
                print("You canceled the payment. Returning to the menu.")
        elif next_step == "add":
            print("Adding another order.")
        elif next_step == "cancel":
            cancel_order()
            customer_number += 1
            recent_orders.clear()
        else:
            print("Invalid input. Returning to menu.")

if __name__ == "__main__":
    main()
