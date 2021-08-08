import cookbook
import sys

# This program takes input as 1-5 ingredients acquirable in the popular video game The Legend of Zelda: Breath of the Wild and calculates the effects that would result in a dish combining those ingredients.
# Critical effects are not taken into account in this calculator.

def main():

    # Store all ingredients in nested dictionary with effects (quality, health, potency/extrahearts/stampoints, duration, status)
    properties = {'mighty banana': {'quality': 'attack up', 'health': 0.5, 'potency': 2, 'duration': 20, 'status': 'food'}, 'hearty truffle': {'quality': 'hearty', 'extrahearts': 1, 'health': 2, 'status': 'food'},
    'staminoka bass': {'quality': 'stamina', 'health': 1, 'stampoints': 4, 'status': 'food'}, 'endura shroom': {'quality': 'endura', 'health': 1, 'stampoints': 1, 'status': 'food'}, 'spicy pepper': {'quality': 'cold resistance', 'health': 0.5, 'potency': 1, 'duration': 120, 'status': 'food'},
    'ironshroom': {'quality': 'defense up', 'health': 0.5, 'potency': 2, 'duration': 20, 'status': 'food'}, 'chillfin trout': {'quality': 'heat resistance', 'health': 1, 'potency': 2, 'duration': 120, 'status': 'food'},
    'voltfruit': {'quality': 'shock resistance', 'health': 0.5, 'potency': 1, 'duration': 120, 'status': 'food'}, 'rushroom': {'quality': 'speed up', 'health': 0.5, 'potency': 1, 'duration': 30, 'status': 'food'},
    'silent shroom': {'quality': 'stealth up', 'health': 0.5, 'potency': 2, 'duration': 90, 'status': 'food'}, 'mighty carp': {'quality': 'attack up', 'health': 1, 'potency': 2, 'duration': 20, 'status': 'food'},
    'mighty porgy': {'quality': 'attack up', 'health': 1, 'potency': 3, 'duration': 20, 'status': 'food'}, 'mighty thistle': {'quality': 'attack up', 'health': 0, 'potency': 1, 'duration': 20, 'status': 'food'},
    'razorclaw crab': {'quality': 'attack up', 'health': 1, 'potency': 2, 'duration': 20, 'status': 'food'}, 'razorshroom': {'quality': 'attack up', 'health': 0.5, 'potency': 2, 'duration': 20, 'status': 'food'},
    'sizzlefin trout': {'quality': 'cold resistance', 'health': 1, 'potency': 2, 'duration': 120, 'status': 'food'}, 'sunshroom': {'quality': 'cold resistance', 'health': 0.5, 'potency': 2, 'duration': 120, 'status': 'food'},
    'warm saffina': {'quality': 'cold resistance', 'health': 0, 'potency': 1, 'duration': 120, 'status': 'food'}, 'armoranth': {'quality': 'defense up', 'health': 0, 'potency': 1, 'duration': 20, 'status': 'food'},
    'armored carp': {'quality': 'defense up', 'health': 1, 'potency': 2, 'duration': 20, 'status': 'food'}, 'armored porgy': {'quality': 'defense up', 'health': 1, 'potency': 3, 'duration': 20, 'status': 'food'},
    'fortified pumpkin': {'quality': 'defense up', 'health': 0.5, 'potency': 2, 'duration': 20, 'status': 'food'}, 'ironshell crab': {'quality': 'defense up', 'health': 1, 'potency': 2, 'duration': 20, 'status': 'food'},
    'chillshroom': {'quality': 'heat resistance', 'health': 0.5, 'potency': 2, 'duration': 120, 'status': 'food'}, 'cool saffina': {'quality': 'heat resistance', 'health': 0, 'potency': 1, 'duration': 120, 'status': 'food'},
    'hydromelon': {'quality': 'heat resistance', 'health': 0.5, 'potency': 1, 'duration': 120, 'status': 'food'}, 'electric saffina': {'quality': 'shock resistance', 'health': 0, 'potency': 1, 'duration': 120, 'status': 'food'},
    'voltfin trout': {'quality': 'shock resistance', 'health': 1, 'potency': 3, 'duration': 120, 'status': 'food'}, 'zapshroom': {'quality': 'shock resistance', 'health': 0.5, 'potency': 2, 'duration': 120, 'status': 'food'},
    'swift carrot': {'quality': 'speed up', 'health': 0.5, 'potency': 1, 'duration': 30, 'status': 'food'}, 'swift violet': {'quality': 'speed up', 'health': 0, 'potency': 2, 'duration': 30, 'status': 'food'},
    'fleet lotus seeds': {'quality': 'speed up', 'health': 0.5, 'potency': 2, 'duration': 30, 'status': 'food'}, 'blue nightshade': {'quality': 'stealth up', 'health': 0, 'potency': 1, 'duration': 90, 'status': 'food'},
    'silent princess': {'quality': 'stealth up', 'health': 1, 'potency': 3, 'duration': 90, 'status': 'food'}, 'shard of naydras horn': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 1800, 'status': 'food'},
    'sneaky river snail': {'quality': 'stealth up', 'health': 1, 'potency': 1, 'duration': 90, 'status': 'food'}, 'stealthfin trout': {'quality': 'stealth up', 'health': 1, 'potency': 2, 'duration': 90, 'status': 'food'},
    'hearty bass': {'quality': 'hearty', 'health': 2, 'extrahearts': 2, 'status': 'food'}, 'hearty blueshell snail': {'quality': 'hearty', 'health': 3, 'extrahearts': 3, 'status': 'food'}, 'hearty radish': {'quality': 'hearty', 'health': 2.5, 'extrahearts': 3, 'status': 'food'},
    'big hearty truffle': {'quality': 'hearty', 'health': 3, 'extrahearts': 4, 'status': 'food'}, 'hearty durian': {'quality': 'hearty', 'health': 3, 'extrahearts': 4, 'status': 'food'}, 'hearty lizard': {'quality': 'hearty', 'health': 0, 'extrahearts': 4, 'status': 'bug'},
    'hearty salmon': {'quality': 'hearty', 'health': 4, 'extrahearts': 4, 'status': 'food'}, 'big hearty radish': {'quality': 'hearty', 'health': 4, 'extrahearts': 5, 'status': 'food'}, 'energetic rhino beetle': {'quality': 'stamina', 'health': 0, 'stampoints': 6, 'status': 'bug'},
    'bright-eyed crab': {'quality': 'stamina', 'health': 1, 'stampoints': 2, 'status': 'food'}, 'courser bee honey': {'quality': 'stamina', 'health': 2, 'stampoints': 2, 'status': 'food'}, 'restless cricket': {'quality': 'stamina', 'health': 0, 'stampoints': 1, 'status': 'bug'},
    'stamella shroom': {'quality': 'stamina', 'health': 0.5, 'stampoints': 1, 'status': 'food'}, 'endura carrot': {'quality': 'endura', 'health': 2, 'stampoints': 4, 'status': 'food'}, 'tireless frog': {'quality': 'endura', 'health': 2, 'stampoints': 2, 'status': 'bug'},
    'acorn': {'quality': 'nothing', 'potency': 0, 'health': 0.5, 'duration': 20, 'status': 'food'}, 'chickaloo tree nut': {'quality': 'nothing', 'health': 0.5, 'potency': 0, 'duration': 10, 'status': 'food'}, 'hylian rice': {'quality': 'nothing', 'health': 1, 'potency': 0, 'duration': 30, 'status': 'food'},
    'rock salt': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 30, 'status': 'food'}, 'tabantha wheat': {'quality': 'nothing', 'health': 1, 'potency': 0, 'duration': 30, 'status': 'food'}, 'cane sugar': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 50, 'status': 'food'},
    'fresh milk': {'quality': 'nothing', 'health': 0.5, 'potency': 0, 'duration': 50, 'status': 'food'}, 'goat butter': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 50, 'status': 'food'}, 'bird egg': {'quality': 'nothing', 'health': 1, 'potency': 0, 'duration': 60, 'status': 'food'},
    'naydras scale': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 60, 'status': 'food'}, 'goron spice': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 60, 'status': 'food'}, 'star fragment': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 60, 'status': 'food'},
    'naydras claw': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 180, 'status': 'food'}, 'shard of naydras fang': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 600, 'status': 'food'},
    'bladed rhino beetle': {'quality': 'attack up', 'health': 0, 'potency': 1, 'duration': 20, 'status': 'bug'}, 'warm darner': {'quality': 'cold resistance', 'health': 0, 'potency': 2, 'duration': 120, 'status': 'bug'},
    'summerwing butterfly': {'quality': 'cold resistance', 'health': 0, 'potency': 1, 'duration': 120, 'status': 'bug'}, 'rugged rhino beetle': {'quality': 'defense up', 'health': 0, 'potency': 1, 'duration': 20, 'status': 'bug'},
    'fireproof lizard': {'quality': 'fireproof', 'health': 0, 'potency': 1, 'duration': 120, 'status': 'bug'}, 'smotherwing butterfly': {'quality': 'fireproof', 'health': 0, 'potency': 2, 'duration': 120, 'status': 'bug'},
    'cool darner': {'quality': 'heat resistance', 'health': 0, 'potency': 2, 'duration': 120, 'status': 'bug'}, 'winterwing butterfly': {'quality': 'heat resistance', 'health': 0, 'potency': 1, 'duration': 120, 'status': 'bug'},
    'electric darner': {'quality': 'shock resistance', 'health': 0, 'potency': 2, 'duration': 120, 'status': 'bug'}, 'thunderwing butterfly': {'quality': 'shock resistance', 'health': 0, 'potency': 1, 'duration': 120, 'status': 'bug'},
    'hightail lizard': {'quality': 'speed up', 'health': 0, 'potency': 1, 'duration': 30, 'status': 'bug'}, 'hot-footed frog': {'quality': 'speed up', 'health': 0, 'potency': 2, 'duration': 30, 'status': 'bug'},
    'sunset firefly': {'quality': 'stealth up', 'health': 0, 'potency': 1, 'duration': 90, 'status': 'bug'}, 'bokoblin horn': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 40, 'status': 'monster'},
    'bokoblin fang': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 80, 'status': 'monster'}, 'bokoblin guts': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 160, 'status': 'monster'},
    'moblin horn': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 40, 'status': 'monster'}, 'moblin fang': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 80, 'status': 'monster'},
    'moblin guts': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 160, 'status': 'monster'}, 'lizalfos horn': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 40, 'status': 'monster'},
    'lizalfos talon': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 80, 'status': 'monster'}, 'icy lizalfos tail': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 160, 'status': 'monster'},
    'lynel horn': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 40, 'status': 'monster'}, 'lynel hoof': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 80, 'status': 'monster'},
    'lynel guts': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 160, 'status': 'monster'}, 'chuchu jelly': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 40, 'status': 'monster'},
    'white chuchu jelly': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 80, 'status': 'monster'}, 'keese wing': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 40, 'status': 'monster'},
    'ice keese wing': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 80, 'status': 'monster'}, 'keese eyeball': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 160, 'status': 'monster'},
    'octorok tentacle': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 40, 'status': 'monster'}, 'octorok balloon': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 40, 'status': 'monster'},
    'octorok eyeball': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 80, 'status': 'monster'}, 'molduga fin': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 80, 'status': 'monster'},
    'molduga guts': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 160, 'status': 'monster'}, 'hinox toenail': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 40, 'status': 'monster'},
    'hinox tooth': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 80, 'status': 'monster'}, 'hinox guts': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 160, 'status': 'monster'},
    'ancient screw': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 40, 'status': 'monster'}, 'ancient spring': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 40, 'status': 'monster'},
    'ancient gear': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 80, 'status': 'monster'}, 'ancient shaft': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 80, 'status': 'monster'},
    'ancient core': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 160, 'status': 'monster'}, 'giant ancient core': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 160, 'status': 'monster'},
    'fairy': {'quality': 'nothing', 'health': 5, 'potency': 0, 'duration': 0, 'status': 'food'}, 'raw gourmet meat': {'quality': 'nothing', 'health': 3, 'potency': 0, 'duration': 0, 'status': 'food'},
    'raw whole bird': {'quality': 'nothing', 'health': 3, 'potency': 0, 'duration': 0, 'status': 'food'}, 'raw prime meat': {'quality': 'nothing', 'health': 1.5, 'potency': 0, 'duration': 0, 'status': 'food'},
    'raw bird thigh': {'quality': 'nothing', 'health': 1.5, 'potency': 0, 'duration': 0, 'status': 'food'}, 'palm fruit': {'quality': 'nothing', 'health': 1, 'potency': 0, 'duration': 0, 'status': 'food'},
    'hyrule herb': {'quality': 'nothing', 'health': 1, 'potency': 0, 'duration': 0, 'status': 'food'}, 'raw meat': {'quality': 'nothing', 'health': 1, 'potency': 0, 'duration': 0, 'status': 'food'},
    'raw bird drumstick': {'quality': 'nothing', 'health': 1, 'potency': 0, 'duration': 0, 'status': 'food'}, 'hyrule bass': {'quality': 'nothing', 'health': 1, 'potency': 0, 'duration': 0, 'status': 'food'},
    'sanke carp': {'quality': 'nothing', 'health': 1, 'potency': 0, 'duration': 0, 'status': 'food'}, 'apple': {'quality': 'nothing', 'health': 0.5, 'potency': 0, 'duration': 0, 'status': 'food'},
    'wildberry': {'quality': 'nothing', 'health': 0.5, 'potency': 0, 'duration': 0, 'status': 'food'}, 'hylian shroom': {'quality': 'nothing', 'health': 0.5, 'potency': 0, 'duration': 0, 'status': 'food'},
    'faroshs scale': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 60, 'status': 'food'}, 'faroshs claw': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 180, 'status': 'food'},
    'shard of faroshs fang': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 600, 'status': 'food'}, 'shard of faroshs horn': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 1800, 'status': 'food'},
    'dinraals scale': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 60, 'status': 'food'}, 'dinraals claw': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 180, 'status': 'food'},
    'shard of dinraals fang': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 600, 'status': 'food'}, 'shard of dinraals horn': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 1800, 'status': 'food'},
    'wood': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 0, 'status': 'rock-hard'}, 'diamond': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 0, 'status': 'rock-hard'},
    'flint': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 0, 'status': 'rock-hard'}, 'ruby': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 0, 'status': 'rock-hard'},
    'topaz': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 0, 'status': 'rock-hard'}, 'amber': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 0, 'status': 'rock-hard'},
    'opal': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 0, 'status': 'rock-hard'}, 'fire keese wing': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 80, 'status': 'monster'},
    'electric keese wing': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 80, 'status': 'monster'}, 'red lizalfos tail': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 160, 'status': 'monster'},
    'yellow lizalfos tail': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 160, 'status': 'monster'}, 'yellow chuchu jelly': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 80, 'status': 'monster'},
    'red chuchu jelly': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 80, 'status': 'monster'}, 'lizalfos tail': {'quality': 'nothing', 'health': 0, 'potency': 0, 'duration': 160, 'status': 'monster'}}

    # Dictionary for potency thresholds for each effect
    potency_index = {'attack up': {'min': 1, 'med': 5, 'max': 7}, 'cold resistance': {'min': 1, 'med': 6, 'max': 999}, 'defense up': {'min': 1, 'med': 5, 'max': 7},
    'fireproof': {'min': 1, 'med': 7, 'max': 999}, 'heat resistance': {'min': 1, 'med': 6, 'max': 999}, 'shock resistance': {'min': 1, 'med': 4, 'max': 6},
    'speed up': {'min': 1, 'med': 5, 'max': 7}, 'stealth up': {'min': 1, 'med': 6, 'max': 9}}

    # Input for number of ingredients
    number = cookbook.get_ingredient_number()

    # Input for each of the 1-5 ingredients
    selected_ingredients = cookbook.get_ingredients(properties, number)

    # Check for dishes vs elixirs vs dubious/rock-hard food
    elixir_food_status = cookbook.get_elixir_food_status(selected_ingredients, properties)

    # If the dish status is dubious or rock-hard, the program ends here
    if elixir_food_status == 'dubious':
        print(f"Your ingredient selection would produce a dubious food that restores up to 4 hearts and provides no additional effect. Whoops.")
    elif elixir_food_status == 'rock-hard':
        print(f"Your ingredient selection would produce a rock-hard food that restores up to 4 hearts and provides no additional effect. Whoops.")

    # If the dish status is food or elixir, there are extra steps to calculate effect and number of hearts recovered
    elif elixir_food_status == 'dish' or elixir_food_status == 'elixir':

        # Using ingredient input, calculates dish effect and hearts
        effect = cookbook.get_effect(selected_ingredients, properties, number)
        hearts = cookbook.get_hearts(selected_ingredients, properties)

        # Based on effect, may calculate extrahearts, stamval, or duration and potency
        if effect == "hearty":
            extrahearts = cookbook.get_extrahearts(selected_ingredients, properties)
            print(f"Your ingredient selection would produce a(n) {elixir_food_status} that restores all heart(s) and adds {extrahearts} extra hearts, up to a maximum of 20 total hearts.")
        elif effect == "stamina":
            stamval = cookbook.get_stamval(selected_ingredients, properties, effect)
            print(f"Your ingredient selection would produce a(n) {elixir_food_status} that restores {hearts} heart(s) and {stamval} stamina wheel(s).")
        elif effect == "endura":
            stamval = cookbook.get_stamval(selected_ingredients, properties, effect)
            print(f"Your ingredient selection would produce a(n) {elixir_food_status} that restores {hearts} heart(s), fully restores base stamina, and adds {stamval} extra stamina wheel(s).")
        else:
            if effect != 'nothing':
                tier = cookbook.get_potency(selected_ingredients, properties, potency_index, effect)
                duration = cookbook.get_duration(selected_ingredients, properties, number)
                print(f"Your ingredient selection would produce a(n) {elixir_food_status} that restores {hearts} heart(s) and provides a tier {tier} {effect} effect for {duration}.")
            else:
                print(f"Your ingredient selection would produce a(n) {elixir_food_status} that restores {hearts} heart(s).")

if __name__ == "__main__":
    main()
