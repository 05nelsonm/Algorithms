#!/usr/bin/python

import math


def compare(some_recipe, some_ingredients):
    batch_multiples_per_ingredient = []
    for key in some_recipe.keys():
        # Compare each to see
        if some_recipe[key] <= some_ingredients[key]:
            # Append to list the floor value
            batch_multiples_per_ingredient \
                .append(math.floor(some_ingredients[key] // some_recipe[key]))
        else:
            return 0

    return min(batch_multiples_per_ingredient)


def recipe_batches(recipe, ingredients):
    # If there are fewer key values in the
    # ingredients dictionary, there will automatically
    # not be enough.
    if len(recipe.keys()) > len(ingredients.keys()):
        return 0
    # Otherwise, run comparison
    else:
        return compare(recipe, ingredients)


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
    ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
