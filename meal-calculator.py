import pandas as pd
import numpy as np
import random
import os
import json
import csv
import pickle

#1. Class definition
class Food:
    
    def __init__(self, name, protein, carbs, fat):
        self.name = name
        self.protein = protein
        self.carbs = carbs
        self.fat = fat
        self.total_grams = protein + carbs + fat
        self.total_calories = (protein * 4) + (carbs * 4) + (fat * 9)
        
    def __repr__(self):
        return f"{self.name} contains {self.protein} grams of protein, {self.carbs} grams of carbs, and {self.fat} grams of fat. The total amount of macro-nutrients contained in {self.name} is {self.total_grams} grams, while the total calories amount to {self.total_calories} calories."
    


chocolate = Food("Chocolate", 5, 61, 31)
print("\n\nAll food item values are measured against a 100 gram portion. So for any food item, when you see the protein, carb and fat macro-nutrient amounts, they are the amounts contained in a 100g portion of that food item. Any discrepancy between the final amount of macro-nutrients (the sum of protein, carb and fat) is likely due to the amount of water and fibre that the food item contains.\n\n")
print(chocolate)


# 2. Utility Data and Functions


#2.1 Data for random quote function:

healthy_eating_quotes = {
    1: "The food you eat can be either the safest and most powerful form of medicine or the slowest form of poison.",
    2: "Your diet is a bank account. Good food choices are good investments.",
    3: "To eat is a necessity, but to eat intelligently is an art.",
    4: "Eating healthy is a form of self-respect.",
    5: "Health is not about the weight you lose, but about the life you gain.",
    6: "The first wealth is health.",
    7: "Let food be thy medicine and medicine be thy food.",
    8: "Eating well is a form of self-love.",
    9: "Healthy eating is not about strict dietary limitations, but rather about feeling great, having more energy, and improving your health.",
    10: "A healthy outside starts from the inside."
}

def get_random_quote():
    """Selects and returns a random quote from the healthy eating quotes dictionary."""
    random_key = random.choice(list(healthy_eating_quotes.keys()))
    return healthy_eating_quotes[random_key]
    
# Load functions

def load_from_json(filepath):
    with open(filepath, 'r') as file:
        data = json.load(file)
        return {name: Food(name, *values) for name, values in data.items()}

def load_from_csv(filepath):
    food_dict = {}
    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name, protein, carbs, fat = row
            food_dict[name] = Food(name, int(protein), int(carbs), int(fat))
    return food_dict

def load_from_pickle(filepath):
    with open(filepath, 'rb') as file:
        return pickle.load(file)

# Save function

def save_data(food_dict):
    # Save to JSON
    with open('food_database.json', 'w') as json_file:
        json.dump({key: vars(food) for key, food in food_dict.items()}, json_file)
    
    # Save to CSV
    with open('food_database.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Name', 'Protein', 'Carbs', 'Fat', 'Total Grams', 'Total Calories'])
        for food in food_dict.values():
            writer.writerow([food.name, food.protein, food.carbs, food.fat, food.total_grams, food.total_calories])
    
    # Save to Pickle
    with open('food_database.pkl', 'wb') as pickle_file:
        pickle.dump(food_dict, pickle_file)
    
    print("Data saved to JSON, CSV, and Pickle files successfully.")



#3. Main Function - where the program logic resides
def main(): 
    food_dict = {}
    
    while True:
        
        print("\nMenu:")
        print("1. Add new food item")
        print("2. Calculate meal macros")
        print("3. See a list of currently stored food items.")
        print("4. Load data")
        print("5. Save and exit")
        print("6. Get a random quote about healthy eating")
        choice = input("Select an option: ")
        
        if choice == '1':
            while True:
                
                name = input("Enter food name: ").strip().lower().title()
                protein = int(input("Enter protein content: "))
                carbs = int(input ("Enter carb content: "))
                fat = int(input("Enter fat content: "))
                food_dict[name] = Food(name, protein, carbs, fat)
                print(food_dict[name])
                print(f"Added {name} successfully.")
            
                return_to_menu = input("Press 'm' to return to the menu: ")
                if return_to_menu.lower() == 'm':
                    break
                else:
                    print("Invalid input. Please enter 'm' to return to the menu.")
        elif choice == '2':
            while True:
                
                meal_items = input("Enter food items, separated by commas: ").strip().lower().split(',')
                total_protein, total_carbs, total_fat = 0, 0, 0
                for item in meal_items:
                    item = item.strip().title()
                    food = food_dict.get(item)
                    if food:
                        total_protein += food.protein
                        total_carbs += food.carbs
                        total_fat += food.fat
                print(f"Total Macros - Protein: {total_protein}, Carbs: {total_carbs}, Fat: {total_fat}")
                
                return_to_menu = input("Press 'm' to return to the menu: ")
                if return_to_menu.lower() == 'm':
                    break
                else:
                    print("Invalid input. Please enter 'm' to return to the menu.")
                    
        elif choice == '3':
            print("Current food items: ")
            while True:
                for food_name, food_item in food_dict.items():
                    print(f"{food_name} has Protein: {food_item.protein} grams, Carbs: {food_item.carbs} grams, and Fat: {food_item.fat} grams, for a total of {food_item.total_calories} calories.")
                
                return_to_menu = input("Press 'm' to return to the menu: ")
                if return_to_menu.lower() == 'm':
                    break
                else:
                    print("Invalid choice. Please enter 'm' to return to the menu.")
        
        elif choice == '4':
            
            while True:
                print("\nLoad Data Menu:")
                print("1. Load from JSON")
                print("2. Load from CSV")
                print("3. Load from Pickle")
                print("4. Return to Main Menu")
                load_choice = input("Select an option: ")
                
                if load_choice == '1':
                    food_dict = load_from_json('food_database.json')
                    print("Data loaded from JSON file.")
                    print(f"Loaded {len(food_dict)} items.")
                elif load_choice == '2':
                    food_dict = load_from_csv('food_database.csv')
                    print("Data loaded from CSV file.")
                    print(f"Loaded {len(food_dict)} items.")
                elif load_choice == '3':
                    food_dict = load_from_pickle('food_database.pkl')
                    print("Data loaded from Pickle file.")
                    print(f"Loaded {len(food_dict)} items.")
                elif load_choice == '4':
                    break
                else:
                    print("Invalid choice. Please try again.")
                
                return_to_menu = input("Press 'm' to return to the load data menu: ")
                if return_to_menu.lower() == 'm':
                    continue
                else:
                    print("Invalid input. Returning to load data menu.")
            
            
            
        elif choice == '5': 
            while True:
                save_data(food_dict)  # Save the data in all formats
                print("Data saved successfully.")
                exit_choice = input("Press 'x' to exit or 'm' to return to the main menu: ").strip().lower()
        
                if exit_choice == 'x':
                    print("Exiting the program. Goodbye!")
                    return  # Exits the main() function, terminating the program
                elif exit_choice == 'm':
                    break  # Exits the save loop, returning to the main menu
                else:
                    print("Invalid input. Please press 'x' to exit or 'm' to return to the main menu.")
        
        elif choice == '6':
            while True:
                
                print("\n Quote about Healthy Eating:")
                print("'" + get_random_quote() + "'")
                
                return_to_menu = input("Press 'm' to return to the menu: ")
                if return_to_menu.lower() == 'm':
                    break
                else:
                    print("Invalid choice. Please enter 'm' to return to the menu.")
            
        else: 
            print("Invalid choice. Please try again.")
            
#4. Program entry point
if __name__ == "__main__":
    main()