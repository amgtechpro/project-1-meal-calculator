import pandas as pd
import numpy as np
import requests
import os
import json
import csv
import pickle


class Food:
    
    def __init__(self, name, protein, carbs, fat):
        self.name = name
        self.protein = protein
        self.carbs = carbs
        self.fat = fat
        self.total_grams = protein + carbs + fat
        self.total_calories = (protein * 4) + (carbs * 4) + (fat * 9)
        
    def __repr__(self):
        return f"{self.name} contains {self.protein}grams of protein, {self.carbs}grams of carbs, and {self.fat}grams of fat. The total amount of macro-nutrients contained in {self.name} is {self.total_grams}, while the total calories amount to {self.total_calories}."
    


chocolate = Food("Chocolate", 8, 35, 20)

print(chocolate)

def main(): 
    food_dict = {}
    
    while True:
        
        print("\nMenu:")
        print("1. Add new food item")
        print("2. Calculate meal macros")
        print("3. See a list of currently stored food items.")
        print("4. Load data from JSON")
        print("5. Load data from CSV")
        print("6. Save and exit")
        choice = input("Select an option: ")
        
        if choice == '1':
            while True:
                
                name = input("Enter food name: ")
                protein = int(input("Enter protein content: "))
                carbs = int(input ("Enter carbs content: "))
                fat = int(input("Enter fat content: "))
                food_dict[name] = Food(name, protein, carbs, fat)
                print(f"Added {name} successfully.")
            
                return_to_menu = input("Press 'm' to return to the menu: ")
                if return_to_menu.lower() == 'm':
                    break
                else:
                    print("Invalid input. Please enter 'm' to return to the menu.")
        elif choice == '2':
            while True:
                
                meal_items = input("Enter food items, separated by commas: ").split(',')
                total_protein, total_carbs, total_fat = 0, 0, 0
                for item in meal_items:
                    food = food_dict.get(item.strip())
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
                for food_name in food_dict.keys():
                    print(f"{food_name}, ")
                
                return_to_menu = input("Press 'm' to return to the menu: ")
                if return_to_menu.lower() == 'm':
                    break
                else:
                    print("Invalid choice. Please enter 'm' to return to the menu.")
        elif choice == '6': 
            print("Data saved. Exiting...")
            break
        else: 
            print("Invalid choice. Please try again.")
            

if __name__ == "__main__":
    main()