import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class MicDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MiCDO Ordering System")
        self.root.geometry("500x600")

        # Data Initialization
        self.recent_orders = []
        self.all_orders = {}  # Stores orders with their totals per day
        self.total_earnings = 0.0
        self.customer_number = 1

        # Meal Prices and Options
        self.prices = [
            [129.0, 149.0, 135.0, 199.0],
            [99.0, 119.0, 169.0, 199.0],
            [89.0, 89.0, 89.0, 139.0],
            [49.0, 69.0, 99.0, 119.0],
        ]

        self.meals = {
            "Chicken Meal": [
                "1pc. Chicken MicDo with Medium IcedTea Meal",
                "8pc. Chicken MicNuggets with Rice and Coke Meal",
                "2pc. MicCrispy Chicken Fillet King with Rice and Coke Meal",
                "2pcs. Chicken MicDo with Rice and Coke Meal",
            ],
            "Burger Meal": [
                "YumMic Cheeseburger with MicFloat Meal",
                "YummyMic Double Cheeseburger with Fries and Coke Meal",
                "Quarter Pounder with Cheese with Fries and Coke Meal",
                "Big Mac CheesyMic Burger with Fries and Coke Meal",
            ],
            "Breakfast Meal": [
                "MicDo Tapsilog with IcedTea Meal",
                "MicDo Tosilog with IcedTea Meal",
                "MicDo Hotsilog with IcedTea Meal",
                "MicDo Sizzling Porksilog with Coke Meal",
            ],
            "Drinks": [
                "Medium Coke MicFloat",
                "Medium Iced Coffee Original with Vanilla",
                "MicCaf'e Coffee Float",
                "Medium Fries and Monster Coke MiCFloat",
            ],
        }

        self.build_main_menu()

    def build_main_menu(self):
        self.clear_window()

        # Header Layout
        tk.Label(self.root, text="*=======================*", font=("Courier", 12)).grid(row=0, column=0, columnspan=2, pady=5)
        tk.Label(self.root, text="Welcome to MiCDO!", font=("Times New Roman", 16, "italic bold")).grid(row=1, column=0, columnspan=2, pady=10)
        tk.Label(self.root, text="*=======================*", font=("Courier", 12)).grid(row=2, column=0, columnspan=2, pady=5)
        tk.Label(self.root, text="MENU", font=("Times New Roman", 16, "italic bold")).grid(row=3, column=0, columnspan=2, pady=5)
        tk.Label(self.root, text=f"Customer {self.customer_number}", font=("Times New Roman", 12)).grid(row=4, column=0, columnspan=2, pady=5)

        # Meal Buttons Layout (2 columns)
        row = 5
        col = 0
        for idx, (category, meals) in enumerate(self.meals.items()):
            tk.Button(self.root, text=category, command=lambda c=category: self.show_meal_menu(c)).grid(
                row=row, column=col, pady=5, padx=10, sticky="ew"
            )
            col += 1
            if col == 2:  # Reset column after 2 columns
                col = 0
                row += 1

        # Additional Action Buttons
        tk.Button(self.root, text="Checkout", command=self.checkout).grid(row=row+1, column=1, pady=10, sticky="e", padx=10)
        tk.Button(self.root, text="Cancel Order", command=self.cancel_order).grid(row=row+2, column=1, pady=10, sticky="e", padx=10)
        tk.Button(self.root, text="View Order History", command=self.view_order_history).grid(row=row+3, column=1, pady=10, sticky="e", padx=10)

    def show_meal_menu(self, category):
        self.clear_window()
        tk.Label(self.root, text=f"{category}", font=("Arial", 16, "bold")).pack(pady=10)

        for i, meal in enumerate(self.meals[category]):
            price = self.prices[list(self.meals.keys()).index(category)][i]
            tk.Button(self.root, text=f"{meal} - Php {price:.2f}", command=lambda m=meal, p=price: self.ask_quantity(m, p)).pack(pady=5)

        tk.Button(self.root, text="Back", command=self.build_main_menu).pack(pady=10)

    def ask_quantity(self, meal, price):
        self.clear_window()
        tk.Label(self.root, text=f"Enter quantity for {meal}", font=("Times New Roman", 14)).pack(pady=10)
        quantity_entry = tk.Entry(self.root)
        quantity_entry.pack(pady=5)

        def add_with_quantity():
            try:
                quantity = int(quantity_entry.get())
                if quantity <= 0:
                    messagebox.showerror("Invalid Quantity", "Quantity must be greater than 0.")
                    return
                self.add_order(meal, price, quantity)
                messagebox.showinfo("Order Added", f"{meal} x{quantity} added to your order!")
                self.build_main_menu()
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter a valid quantity.")

        tk.Button(self.root, text="Add to Order", command=add_with_quantity).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.build_main_menu).pack(pady=5)

    def add_order(self, meal, price, quantity):
        self.recent_orders.append((meal, price, quantity))

    def checkout(self):
        if not self.recent_orders:
            messagebox.showerror("No Orders", "You have no orders to checkout.")
            return

        total = sum(price * quantity for _, price, quantity in self.recent_orders)
        payment_window = tk.Toplevel(self.root)
        payment_window.title("Checkout")

        tk.Label(payment_window, text=f"Total: Php {total:.2f}", font=("Times New Roman", 14)).pack(pady=10)
        tk.Label(payment_window, text="Enter payment amount:").pack(pady=5)
        payment_entry = tk.Entry(payment_window)
        payment_entry.pack(pady=5)

        def process_payment():
            try:
                amount_paid = float(payment_entry.get())
                if amount_paid < total:
                    messagebox.showerror("Insufficient Payment", f"You need Php {total - amount_paid:.2f} more.")
                else:
                    change = amount_paid - total
                    self.generate_receipt(amount_paid)  # Generate the receipt first
                    self.save_order(total)  # Save the order with total
                    messagebox.showinfo("Payment Successful", f"Change: Php {change:.2f}")
                    payment_window.destroy()

                    # Increase customer number for next customer
                    self.customer_number += 1
                    self.build_main_menu()

            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter a valid numeric amount.")

        tk.Button(payment_window, text="Pay", command=process_payment).pack(pady=10)

    def generate_receipt(self, payment_amount):
        # Create a new window for the receipt
        receipt_window = tk.Toplevel(self.root)
        receipt_window.title("Receipt")

        # Title of the receipt
        tk.Label(receipt_window, text="Customer Receipt", font=("Times New Roman", 16, "bold")).pack(pady=10)

        # Items Ordered Section
        tk.Label(receipt_window, text="Items Ordered:", font=("Times New Roman", 12, "italic bold")).pack(pady=5)
        total_amount = 0  # Initialize total amount

        # Loop through recent orders and display them
        for meal, price, quantity in self.recent_orders:
            tk.Label(receipt_window, text=f"{meal} x{quantity} - Php {price * quantity:.2f}", font=("Times New Roman", 12)).pack()
            total_amount += price * quantity  # Add to total cost

        # Display total amount
        tk.Label(receipt_window, text=f"Total Amount: Php {total_amount:.2f}", font=("Times New Roman", 12, "bold")).pack(pady=5)

        # Display payment amount
        tk.Label(receipt_window, text=f"Payment: Php {payment_amount:.2f}", font=("Times New Roman", 12)).pack(pady=5)

                # Calculate and display change
        change = payment_amount - total_amount
        if change < 0:
            tk.Label(receipt_window, text="Error: Insufficient payment.", font=("Times New Roman", 12, "bold")).pack(pady=5)
        else:
            tk.Label(receipt_window, text=f"Change: Php {change:.2f}", font=("Times New Roman", 12, "bold")).pack(pady=5)

        # Footer of the receipt
        tk.Label(receipt_window, text="Thank you for your order!", font=("Times New Roman", 14, "italic")).pack(pady=20)

    def save_order(self, total):
        # Save the recent order with total earnings
        order_date = datetime.now().strftime("%Y-%m-%d")
        if order_date not in self.all_orders:
            self.all_orders[order_date] = []
        self.all_orders[order_date].append((self.recent_orders.copy(), total))
        self.total_earnings += total
        self.recent_orders.clear()  # Clear the recent orders after saving

    def view_order_history(self):
        self.clear_window()

        if not self.all_orders:
            tk.Label(self.root, text="No order history available.", font=("Times New Roman", 14)).pack(pady=20)
        else:
            tk.Label(self.root, text="Order History:", font=("Times New Roman", 16, "bold")).pack(pady=10)

            for order_date, orders in self.all_orders.items():
                tk.Label(self.root, text=f"Date: {order_date}", font=("Times New Roman", 14, "italic bold")).pack(pady=5)
                for order, total in orders:
                    for meal, price, quantity in order:
                        tk.Label(self.root, text=f"{meal} x{quantity} - Php {price * quantity:.2f}", font=("Times New Roman", 12)).pack()
                    tk.Label(self.root, text=f"Total: Php {total:.2f}", font=("Times New Roman", 14, "bold")).pack(pady=5)

        tk.Button(self.root, text="Back to Menu", command=self.build_main_menu).pack(pady=20)

    def cancel_order(self):
        self.recent_orders.clear()  # Clear any current order
        messagebox.showinfo("Order Cancelled", "Your order has been cancelled.")
        self.build_main_menu()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()  # Remove all widgets from the window


if __name__ == "__main__":
    root = tk.Tk()
    app = MicDoApp(root)
    root.mainloop()

