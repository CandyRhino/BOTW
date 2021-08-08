import cs50
import sys

def get_ingredient_number():
    number = 0
    print("How many ingredients would you like to input? Enter an integer 1-5.")
    while (number < 1) or (number > 5):
        number = cs50.get_int("Number of Ingredients: ")
    return number

def get_ingredients(properties, number):
    text = 0
    selected_ingredients = []
    n = 1
    special_characters = [',', '.', ':', ';', "'", '"', '!', '-']
    while n <= number:
        text = input(f"Ingredient {n}: ")
        for m in special_characters:
            text = text.replace(m, '')
        text = text.lower()
        while properties.get(text) == None:
            print("Error: ingredient does not exist.")
            text = input(f"Ingredient {n}: ")
        selected_ingredients.insert(n - 1, text)
        n += 1
    return selected_ingredients

def get_elixir_food_status(selected_ingredients, properties):
    n = 0
    status_list = []
    while n < len(selected_ingredients):
        status_list.append(properties[selected_ingredients[n]]['status'])
        n += 1
    status_list = list(set(status_list))
    if (status_list.count('bug') > 0) and (status_list.count('monster') > 0):
        elixir_food_status = 'elixir'
    elif status_list.count('rock-hard') > 0:
        elixir_food_status = 'rock-hard'
    elif (status_list.count('bug') == 0) and (status_list.count('monster') > 0):
        elixir_food_status = 'dubious'
    elif (status_list.count('bug') > 0) and (status_list.count('monster') == 0):
        elixir_food_status = 'dubious'
    else:
        elixir_food_status = 'dish'
    return elixir_food_status

def get_effect(selected_ingredients, properties, number):
    n = 0
    effects_list = []
    while n < len(selected_ingredients):
        effects_list.append(properties[selected_ingredients[n]]['quality'])
        n += 1
    if effects_list.count('nothing') == number:
        effect = 'nothing'
    else:
        while effects_list.count('nothing') > 0:
            effects_list.remove('nothing')
        effects_list = list(set(effects_list))
        if len(effects_list) == 1:
            effect = effects_list[0]
        else:
            effect = 'nothing'
    return effect

def get_hearts(selected_ingredients, properties):
    hearts = 0
    n = 0
    if len(selected_ingredients) == 1 and selected_ingredients[0] == 'fresh milk':
        hearts += properties[selected_ingredients[n]]['health']
        hearts = hearts * 3
    elif len(selected_ingredients) == 1 and (selected_ingredients[0] == 'acorn' or selected_ingredients[0] == 'chickaloo tree nut'):
        hearts += properties[selected_ingredients[n]]['health']
    else:
        while n < len(selected_ingredients):
            hearts += properties[selected_ingredients[n]]['health']
            n += 1
        hearts = 2 * hearts
    if hearts >= 4.5:
        hearts = round(hearts) + 1
    return hearts

def get_potency(selected_ingredients, properties, potency_index, effect):
    n = 0
    level_value = 0
    while n < len(selected_ingredients):
        level_value += properties[selected_ingredients[n]]['potency']
        n += 1
    if level_value >= potency_index[effect]['min'] and level_value < potency_index[effect]['med']:
        tier = 1
    elif level_value >= potency_index[effect]['med'] and level_value < potency_index[effect]['max']:
        tier = 2
    elif level_value >= potency_index[effect]['max']:
        tier = 3
    return tier

def get_duration(selected_ingredients, properties, number):
    n = 0
    time = 0
    while n < len(selected_ingredients):
        if properties[selected_ingredients[n]]['quality'] == 'nothing':
            while selected_ingredients.count(selected_ingredients[n]) > 1:
                selected_ingredients.remove(selected_ingredients[n])
        n += 1
    n = 0
    while n < len(selected_ingredients):
        time += properties[selected_ingredients[n]]['duration']
        n += 1
    time = time + (number * 30)
    while time > 1800:
        time = 1800
    mins = round(((time - (time % 60)) / 60))
    secs = time % 60
    if mins > 0 and secs > 0:
        time = f'{mins} minute(s) and {secs} seconds'
    elif mins == 0 and secs > 0:
        time = f'{secs} seconds'
    elif mins > 0 and secs == 0:
        time = f'{mins} minute(s)'
    return time

def get_extrahearts(selected_ingredients, properties):
    extrahearts = 0
    n = 0
    while n < len(selected_ingredients):
        if properties[selected_ingredients[n]]['quality'] == 'hearty':
            extrahearts += properties[selected_ingredients[n]]['extrahearts']
            n += 1
        else:
            n += 1
    return extrahearts

def get_stamval(selected_ingredients, properties, effect):
    n = 0
    stamval = 0
    stampoints = 0
    while n < len(selected_ingredients):
        if (properties[selected_ingredients[n]]['quality'] == 'stamina') or (properties[selected_ingredients[n]]['quality'] == 'endura'):
            stampoints += properties[selected_ingredients[n]]['stampoints']
            n += 1
        else:
            n += 1
    if effect == 'stamina':
        if stampoints == 1:
            stamval = 'about 1/5'
        elif stampoints == 2:
            stamval = 'about 1/3'
        elif stampoints == 3:
            stamval = 'about 4/5'
        elif stampoints == 4:
            stamval = '1'
        elif stampoints == 5:
            stamval = 'about 1 and 1/3'
        elif stampoints == 6:
            stamval = 'about 1 and 2/3'
        elif stampoints == 7:
            stamval = 'about 1 and 4/5'
        elif stampoints == 8:
            stamval = 'about 2 and 1/5'
        elif stampoints == 9:
            stamval = 'about 2 and 1/3'
        elif stampoints == 10:
            stamval = 'about 2 and 4/5'
        elif stampoints >= 11:
            stamval = '3'
    elif effect == 'endura':
        if stampoints >= 1 and stampoints < 4:
            stamval = 'about 1/5'
        elif stampoints >= 4 and stampoints < 6:
            stamval = 'about 1/3'
        elif stampoints >= 6 and stampoints < 8:
            stamval = 'about 2/3'
        elif stampoints >= 8 and stampoints < 10:
            stamval = '4/5'
        elif stampoints >= 10 and stampoints < 12:
            stamval = '1'
        elif stampoints >= 12 and stampoints < 14:
            stamval = 'about 1 and 1/5'
        elif stampoints >= 14 and stampoints < 16:
            stamval = 'about 1 and 1/3'
        elif stampoints >= 16 and stampoints < 18:
            stamval = 'about 1 and 2/3'
        elif stampoints >= 18 and stampoints < 20:
            stamval = 'about 1 and 4/5'
        elif stampoints >= 20:
            stamval = '2'
    return stamval
