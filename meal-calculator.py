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