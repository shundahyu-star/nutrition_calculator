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
    {"name": "Protein Scramble", "time": "breakfast", "diets": ["vegetarian", "standard"], "base": {"eggs": 100, "egg_whites": 100, "spinach": 50, "whole_wheat_bread": 70, "butter": 5}},
    {"name": "Tofu Scramble Hash", "time": "breakfast", "diets": ["vegan", "vegetarian", "standard"], "base": {"tofu_firm": 150, "potato": 100, "onion": 30, "olive_oil": 10}},
    {"name": "Greek Yogurt Parfait", "time": "breakfast", "diets": ["vegetarian", "standard"], "base": {"greek_yogurt": 200, "honey": 15, "almonds": 20, "berries": 50}},
    {"name": "Peanut Butter Banana Toast", "time": "breakfast", "diets": ["vegan", "vegetarian", "standard"], "base": {"whole_wheat_bread": 70, "peanut_butter": 30, "banana": 100}},
    {"name": "Smoked Salmon Bagel Bowl", "time": "breakfast", "diets": ["standard"], "base": {"salmon": 80, "whole_wheat_bread": 70, "cottage_cheese": 50, "tomato": 40}},
    {"name": "Cottage Cheese & Apple", "time": "breakfast", "diets": ["vegetarian", "standard"], "base": {"cottage_cheese": 150, "apple": 120, "walnuts": 15}},
    {"name": "Steak & Eggs", "time": "breakfast", "diets": ["standard"], "base": {"lean_beef": 100, "eggs": 100, "potato": 100, "olive_oil": 5}},
    {"name": "Vegan Protein Shake", "time": "breakfast", "diets": ["vegan", "vegetarian", "standard"], "base": {"almond_milk": 250, "peanut_butter": 40, "banana": 100, "oats": 30}},
    {"name": "Avocado Toast with Egg", "time": "breakfast", "diets": ["vegetarian", "standard"], "base": {"whole_wheat_bread": 70, "avocado": 60, "eggs": 50, "spinach": 30}},
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
    {"name": "Pork Loin & Mash", "time": "dinner", "diets": ["standard"], "base": {"pork_loin": 160, "potato": 200, "whole_milk": 30, "kale": 80}},
    {"name": "Vegan Black Bean Burger", "time": "dinner", "diets": ["vegan", "vegetarian", "standard"], "base": {"black_beans": 120, "oats": 30, "whole_wheat_bread": 70, "avocado": 30, "tomato": 30}},
    {"name": "Shrimp Pasta Garlic Oil", "time": "dinner", "diets": ["standard"], "base": {"shrimp": 150, "pasta": 100, "olive_oil": 15, "garlic": 10, "spinach": 50}},
    {"name": "Lentil Shepherd's Pie", "time": "dinner", "diets": ["vegan", "vegetarian", "standard"], "base": {"lentils": 120, "potato": 150, "carrot": 50, "onion": 30, "olive_oil": 10}},
    {"name": "Chicken & Veggie Roast", "time": "dinner", "diets": ["standard"], "base": {"chicken_breast": 180, "carrot": 80, "potato": 100, "olive_oil": 10}},
    {"name": "Tempeh Bolognese", "time": "dinner", "diets": ["vegan", "vegetarian", "standard"], "base": {"tempeh": 120, "pasta": 100, "tomato": 100, "onion": 30, "garlic": 5}},
    {"name": "Turkey Meatball Zoodles", "time": "dinner", "diets": ["standard"], "base": {"turkey_breast": 150, "zucchini": 200, "tomato": 100, "olive_oil": 10}}
]

# logic and algorithms.
def calculate_needs(age, gender, weight, height, activity, goal):
    #bmr calculation
    if gender == 'm':
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
    #tdee calculation
    tdee = bmr * activity
    #goal rrequirements
    if goal == 'cut': target_cals = tdee * 0.80
    elif goal == 'bulk': target_cals = tdee * 1.20
    else: target_cals = tdee
    #macro split calc
    target_p = weight * 2.2
    target_f = (target_cals * 0.25)/ 9
    target_c = (target_cals - (target_p* 4) - (target_f * 9))/4
    return target_cals, target_p, target_f, target_c
def calculate_recipe_base_macros(recipe):
    base_cals = base_p = base_f = base_c = 0
    for ingr, amount in recipe["base"].items():
        ratio = amount / 100
        base_cals += ingr_db[ingr]["cal"] * ratio
        base_p += ingr_db[ingr]["p"] * ratio
        base_f += ingr_db[ingr]["f"] * ratio
        base_c += ingr_db[ingr]["c"] * ratio
    return base_cals, base_p, base_f, base_c
def generate_meal_plan(target_cals, diet_pref):
    # Filter
    valid_breakfasts = [r for r in recipes_db if r["time"] == "breakfast" and diet_pref in r["diets"]]
    valid_lunches = [r for r in recipes_db if r["time"] == "lunch" and diet_pref in r["diets"]]
    valid_dinners = [r for r in recipes_db if r["time"] == "dinner" and diet_pref in r["diets"]]
    meal_target_cals = target_cals / 3

    daily_plan = []
    for meal_pool in [valid_breakfasts, valid_lunches, valid_dinners]:
        selected_recipe = random.choice(meal_pool)
        base_cals, base_p, base_f, base_c = calculate_recipe_base_macros(selected_recipe)
        scale_factor = meal_target_cals / base_cals if base_cals > 0 else 1
        scaled_ingredients = {}
        for ingr, base_amount in selected_recipe["base"].items():
            scaled_ingredients[ingr] = round(base_amount * scale_factor)

        daily_plan.append({
            "name": selected_recipe["name"],
            "cals": round(base_cals * scale_factor),
            "p": round(base_p * scale_factor),
            "f": round(base_f * scale_factor),
            "c": round(base_c * scale_factor),
            "ingredients": scaled_ingredients
        })
    return daily_plan

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()
    print("=========================================")
    print("      MACRO & MEAL PLAN GENERATOR        ")
    print("=========================================\n")
    
    #user data
    age = int(input("Age: "))
    gender = input("Gender (m/f): ").lower()
    weight = float(input("Weight (kg): "))
    height = float(input("Height (cm): "))
    
    print("\nActivity Levels:")
    print("1: Sedentary (office job, little exercise)")
    print("2: Lightly Active (1-3 days/week)")
    print("3: Moderately Active (3-5 days/week)")
    print("4: Very Active (6-7 days/week)")
    act_choice = input("Select Activity Level (1-4): ")
    activity_map = {'1': 1.2, '2': 1.375, '3': 1.55, '4': 1.725}
    activity = activity_map.get(act_choice, 1.2)
    
    print("\nGoals:")
    print("1: Cut (Lose Fat)")
    print("2: Maintain")
    print("3: Bulk (Gain Muscle)")
    goal_choice = input("Select Goal (1-3): ")
    goal_map = {'1': 'cut', '2': 'maintain', '3': 'bulk'}
    goal = goal_map.get(goal_choice, 'maintain')
    
    print("\nDietary Restrictions:")
    print("1: Standard (No restrictions)")
    print("2: Vegetarian")
    print("3: Vegan")
    diet_choice = input("Select Diet (1-3): ")
    diet_map = {'1': 'standard', '2': 'vegetarian', '3': 'vegan'}
    diet = diet_map.get(diet_choice, 'standard')
    
    # Crunch the numbers once
    t_cals, t_p, t_f, t_c = calculate_needs(age, gender, weight, height, activity, goal)
    
    # Meal Generation Loop
    while True:
        clear_screen()
        print("=========================================")
        print("           YOUR DAILY TARGETS            ")
        print("=========================================")
        print(f"Goal: {goal.upper()} | Diet: {diet.upper()}")
        print(f"Calories: {t_cals:.0f} kcal")
        print(f"Macros: Protein {t_p:.0f}g | Fat {t_f:.0f}g | Carbs {t_c:.0f}g")
        print("=========================================\n")
        
        plan = generate_meal_plan(t_cals, diet)
        
        meal_labels = ["BREAKFAST", "LUNCH", "DINNER"]
        for i, meal in enumerate(plan):
            print(f"[{meal_labels[i]}] - {meal['name']}")
            print(f"Macros: {meal['cals']} kcal | P: {meal['p']}g | F: {meal['f']}g | C: {meal['c']}g")
            print("Ingredients needed:")
            for ingr, amount in meal['ingredients'].items():
                clean_name = ingr.replace("_", " ").title()
                print(f"  - {amount}g of {clean_name}")
            print("-" * 41)
            
        print("\nOptions:")
        choice = input("Press [Enter] to exit, or type 'R' to generate different meals: ").lower()
        
        if choice != 'r':
            print("\nEnjoy your meals! Exiting...")
            break

if __name__ == "__main__":
    main()