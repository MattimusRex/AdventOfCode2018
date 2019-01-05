recipes = [3, 7]
index_1 = 0
index_2 = 1

NUMBER_OF_RECIPES = 440231
recipe_count = 0
while True:
    new_recipe = recipes[index_1] + recipes[index_2]
    new_recipe = str(new_recipe)
    for char in new_recipe:
        recipes.append(int(char))
        recipe_count += 1
    
    if recipe_count >= NUMBER_OF_RECIPES + 10:
        break

    index_1 = (recipes[index_1] + 1 + index_1) % len(recipes)
    index_2 = (recipes[index_2] + 1 + index_2) % len(recipes)

print(recipes[NUMBER_OF_RECIPES:NUMBER_OF_RECIPES + 10])

