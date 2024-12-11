import csv
import os

# Function to append a single entry to the CSV file
def append_to_csv(number, letter):
    # Check if the CSV file already exists
    file_exists = os.path.isfile('letters.csv')
    
    with open('letters.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        # Write header if the file is being created for the first time
        if not file_exists:
            writer.writerow(['Number', 'Letter'])
        # Write the new entry
        writer.writerow([number, letter])

# Function to get the letter corresponding to a number
def get_letter(number):
    return chr(96 + number)  # 96 + 1 = 97 ('a'), 96 + 2 = 98 ('b'), etc.

def main():
    try:
        user_input = int(input("Enter a number between 1 and 26: "))
        if 1 <= user_input <= 26:
            letter = get_letter(user_input)
            print(f"The letter corresponding to {user_input} is '{letter}'.")
            # Append the number and letter to the CSV file
            append_to_csv(user_input, letter)
        else:
            print("Please enter a valid number between 1 and 26.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()