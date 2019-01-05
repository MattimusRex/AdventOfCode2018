import sys

recipes = [3, 7]
index_1 = 0
index_2 = 1

NUMBER_OF_RECIPES = '440231'
NUMBER_OF_RECIPES = [int(x) for x in NUMBER_OF_RECIPES]
recipe_count = 0
while True:
    new_recipe = recipes[index_1] + recipes[index_2]
    new_recipe = str(new_recipe)
    for char in new_recipe:
        recipes.append(int(char))
        if recipes[-6:] == NUMBER_OF_RECIPES:
            print (len(recipes) - 6)
            sys.exit()

    index_1 = (recipes[index_1] + 1 + index_1) % len(recipes)
    index_2 = (recipes[index_2] + 1 + index_2) % len(recipes)
