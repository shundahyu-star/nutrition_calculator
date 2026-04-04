import random
import os
# DATABASE 1: 50 ingrdients
# Values are per 100g (cal, pro, fat, car)
ingr_dg = {
    #protein sources (MEAT)
    "chicken_breast": {"cal": 165, "p": 31, "f": 3.6,"c": 0},
    "turkey_breast": {"cal": 135, "p": 30, "f": 1.0, "c": 0},
    "lean_beef": {"cal": 250, "p": 26, "f": 15, "c": 0},
    "pork_loin": {"cal": 143, "p": 26, "f": 3.5, "c": 0},
    "salmon": {"cal": 208, "p": 20, "f": 13, "c": 0},
    "tuna_canned": {"cal": 116, "p": 26, "f": 0.8, "c": 0},
    "shrimp": {"cal": 99, "p": 24, "f": 0.3, "c": 0.2},
    # protein souces (vegan or vegetarian)
    "tofu_firm": {"cal": 144, "p": 15, "f": 8.7, "c": 2.8},
    "tempeh": {"cal": 192, "p": 19, "f": 11, "c": 9},
    "seitan": {"cal": 370, "p": 75, "f": 1.9, "c": 14},
    "eggs": {"cal": 143, "p": 12.5, "f": 9.5, "c": 0.7},
    "egg_whites": {"cal": 52, "p": 11, "f": 0.2, "c": 0.7},
    "greek_yogurt": {"cal": 59, "p": 10, "f": 0.4, "c": 3.6},
    "cottage_cheese": {"cal": 98, "p": 11, "f": 4.3, "c": 3.4},
    "whole_milk": {"cal": 61, "p": 3.2, "f": 3.3, "c": 4.8},
    "almond_milk": {"cal": 15, "p": 0.4, "f": 1.0, "c": 0.3},
    # cars section
    "oats": {"cal": 389, "p": 16.9, "f": 6.9, "c": 66.3},
    "brown_rice": {"cal": 111, "p": 2.6, "f": 0.9, "c": 23},
    "white_rice": {"cal": 130, "p": 2.7, "f": 0.3, "c": 28},
    "quinoa": {"cal": 120, "p": 4.4, "f": 1.9, "c": 21.3},
    "whole_wheat_bread": {"cal": 252, "p": 12.5, "f": 3.4, "c": 43},
    "pasta": {"cal": 131, "p": 5.8, "f": 1.1, "c": 25},
    "sweet_potato": {"cal": 86, "p": 1.6, "f": 0.1, "c": 20},
    "potato": {"cal": 77, "p": 2, "f": 0.1, "c": 17},
    "lentils": {"cal": 116, "p": 9, "f": 0.4, "c": 20},
    "chickpeas": {"cal": 164, "p": 8.9, "f": 2.6, "c": 27.4},
    "black_beans": {"cal": 132, "p": 8.9, "f": 0.5, "c": 23.7},
    #fat
    "olive_oil": {"cal": 884, "p": 0, "f": 100, "c": 0},
    "butter": {"cal": 717, "p": 0.8, "f": 81, "c": 0.1},
    "avocado": {"cal": 160, "p": 2, "f": 14.7, "c": 8.5},
    "almonds": {"cal": 579, "p": 21, "f": 50, "c": 22},
    "walnuts": {"cal": 654, "p": 15, "f": 65, "c": 14},
    "peanut_butter": {"cal": 588, "p": 25, "f": 50, "c": 20},
    "chia_seeds": {"cal": 486, "p": 16.5, "f": 30.7, "c": 42.1},
    "flax_seeds": {"cal": 534, "p": 18.3, "f": 42.2, "c": 28.9},
    #vegiez
    "spinach": {"cal": 23, "p": 2.9, "f": 0.4, "c": 3.6},
    "kale": {"cal": 49, "p": 4.3, "f": 0.9, "c": 8.8},
    "broccoli": {"cal": 34, "p": 2.8, "f": 0.4, "c": 7},
    "cauliflower": {"cal": 25, "p": 1.9, "f": 0.3, "c": 5},
    "bell_pepper": {"cal": 20, "p": 0.9, "f": 0.2, "c": 4.6},
    "onion": {"cal": 40, "p": 1.1, "f": 0.1, "c": 9.3},
    "garlic": {"cal": 149, "p": 6.4, "f": 0.5, "c": 33},
    "tomato": {"cal": 18, "p": 0.9, "f": 0.2, "c": 3.9},
    "zucchini": {"cal": 17, "p": 1.2, "f": 0.3, "c": 3.1},
    "carrot": {"cal": 41, "p": 0.9, "f": 0.2, "c": 9.6},
    #fruits and sweeteners
    "apple": {"cal": 52, "p": 0.3, "f": 0.2, "c": 14},
    "banana": {"cal": 89, "p": 1.1, "f": 0.3, "c": 22.8},
    "berries": {"cal": 57, "p": 0.7, "f": 0.3, "c": 14.5},
    "honey": {"cal": 304, "p": 0.3, "f": 0, "c": 82},
    "maple_syrup": {"cal": 260, "p": 0, "f": 0, "c": 67}
    }

recipes_db = [
    #breakfasts
    {"name": "Oatmeal & Berries", "time": "breakfast", "diets": ["vegan", "vegetarian", "standard"], "base": {"oats": 60, "almond_milk": 150, "berries": 100, "chia_seeds": 10}},
    {"name": "Protein Scramble", "time": "breakfast", "diets": ["vegetarian", "vegan", "standard"], "base": {"eggs": 100, "egg_whites": 100, "spinach": 50, "whole_wheat_bread": 70, "butter": 5}},
    {"name": "Tofu Scramble Hash", "time": "breakfast", "diets": ["vegan", "vegetarian", "standard"], "base": {"tofu_firm": 150, "potato": 100, "onion": 30, "olive_oil": 10}},
    {"name": "Greek Yogurt Parfait", "time": "breakfast", "diets": ["vegetarian", "standard"], "base": {"greek_yogurt": 200, "honey": 15, "almonds": 20, "berries": 50}},
    {"name": "Peanut Butter Banana Toast", "time": "breakfast", "diets": ["vegan", "vegetarian", "standard"], "base": {"whole_wheat_bread": 70, "peanut_butter": 30, "banana": 100}},
    {"name": "Smoked Samon Bagel Bowl", "time": "breakfast", "diets": ["standard"], "base": {"salmon": 80, "whole_wheat_bread": 70, "cottage_cheese": 50, "tomato": 40}},
    {"name": "Cottage Cheese & Apple", "time": "breakfast", "diets": ["vegetarian", "standard"], "base": {"cottage_cheese": 150, "apple": 120, "walnuts": 15}},
    {"name": "Steak & Eggs", "time": "breakfast", "diets": ["standard"], "base": {"lean_beef": 100, "eggs": 100, "potato": 100, "olive_oil": 5}},
    {"name": "Vegan Protein Shake", "time": "breakfast", "diets": ["vegan", "vegetarian", "standard"], "base": {"almond_milk": 250, "peanut_butter": 40, "banana": 100, "oats": 30}},
    {"name": "Avocado Toat with Egg", "time": "breakfast", "diets": ["vegetariain", "standard"], "base": {"whole_wheat_bread": 70, "avocado": 60, "egges": 50, "spinach": 30}},
#LUNCHES
    {"name": "Chicken Teriyaki Bowl", "time": "lunch", "diets": ["standard"], "base": {"chicken_breast": 150, "white_rice": 100, "broccoli": 80, "garlic": 5}},
    {"name": "Lentil Salad", "time": "lunch", "diets": ["vegan", "vegetarian", "standard"], "base": {"lentils": 150, "spinach": 50, "tomato": 50, "olive_oil": 10, "onion": 20}},
    {"name": "Tuna Salad Sandwich", "time": "lunch", "diets": ["standard"], "base": {"tuna_canned": 120, "greek_yogurt": 40, "whole_wheat_bread": 70, "carrot": 30}},
    {"name": "Tempeh Stir-fry", "time": "lunch", "diets": ["vegan", "vegetarian", "standard"], "base": {"tempeh": 120, "brown_rice": 100, "bell_pepper": 50, "zucchini": 50, "olive_oil": 10}},
    {"name": "Beef & Potato Hash", "time": "lunch", "diets": ["standard"], "base": {"lean_beef": 150, "sweet_potato": 150, "onion": 40, "olive_oil": 5}},
    {"name": "Chickpea Smash Wrap", "time": "lunch", "diets": ["vegan", "vegetarian", "standard"], "base": {"chickpeas": 130, "avocado": 40, "whole_wheat_bread": 70, "spinach": 30}},
    {"name": "Turkey & Cheese Roll-ups", "time": "lunch", "diets": ["standard"], "base": {"turkey_breast": 120, "cottage_cheese": 50, "whole_wheat_bread": 70, "tomato": 40}},
    {"name": "Quinoa & Black Bean Bowl", "time": "lunch", "diets": ["vegan", "vegetarian", "standard"], "base": {"quinoa": 100, "black_beans": 100, "avocado": 40, "bell_pepper": 40}},
    {"name": "Salmon & Veggie Pasta", "time": "lunch", "diets": ["standard"], "base": {"salmon": 120, "pasta": 80, "zucchini": 50, "olive_oil": 10}},
    {"name": "Seitan Power Bowl", "time": "lunch", "diets": ["vegan", "vegetarian", "standard"], "base": {"seitan": 100, "brown_rice": 100, "kale": 50, "olive_oil": 10}},
    #dinner
    {"name": "Lean Steak & Sweet Potato", "time": "dinner", "diets": ["standard"], "base": {"lean_beef": 180, "sweet_potato": 150, "broccoli": 100, "butter": 10}},
    {"name": "Tofu Curry", "time": "dinner", "diets": ["vegan", "vegetarian", "standard"], "base": {"tofu_firm": 150, "whole_milk": 50, "cauliflower": 100, "white_rice": 100}},
    {"name": "Baked Salmon & Asparagus", "time": "dinner", "diets": ["standard"], "base": {"salmon": 180, "quinoa": 80, "zucchini": 100, "olive_oil": 10}},
]
