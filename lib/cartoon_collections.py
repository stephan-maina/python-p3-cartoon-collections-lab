def roll_call_dwarves(dwarf_names):
    for dwarf in dwarf_names:
        print(f"{dwarf} is here!")

def summon_captain_planet(elements):
    phrase = "By the power of "
    phrase += " and ".join(elements[:-1])
    phrase += f", and {elements[-1]}!"
    return phrase

def long_planeteer_calls(calls, length):
    for call in calls:
        if len(call) > length:
            return True
    return False

def find_the_cheese(foods):
    cheese_types = ["cheddar", "swiss", "mozzarella"]
    for food in foods:
        if food.lower() in cheese_types:
            return food
    return None

# Example usages:

dwarves = ["Doc", "Grumpy", "Happy", "Sleepy", "Bashful", "Sneezy", "Dopey"]
roll_call_dwarves(dwarves)

elements = ["Earth", "Fire", "Wind", "Water", "Heart"]
captain_planet_phrase = summon_captain_planet(elements)
print(captain_planet_phrase)

calls = ["Help!", "Save the planet!", "Go Planet!"]
result = long_planeteer_calls(calls, 15)
print(result)  # This will print False

foods = ["apple", "cheddar", "banana", "mozzarella"]
cheese = find_the_cheese(foods)
if cheese:
    print(f"Found cheese: {cheese}")
else:
    print("No cheese found.")
