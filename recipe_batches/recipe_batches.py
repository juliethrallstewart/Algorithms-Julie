#!/usr/bin/python

import math


recipes = (
  { 'milk': 100, 'butter': 50, 'flour': 5 },
  { 'milk': 138, 'butter': 48, 'flour': 51 }
)

ingredients = {
  'eggs': 12,
  'butter': 100,
  'sugar': 200,
  'flour': 60,
  'cheese': 100,
  'milk': 250
}

def recipe_batches(recipe, ingredients):
#how much needed for all the batches:
  milk = 0
  butter = 0
  flour = 0
  cheese = 0
  eggs = 0
  result = 0

  for recipe in recipes:
#     print(recipe)
    for ingredient in recipe.keys():
          # print(ingredient)
          if ingredient == 'milk':
                milk+=recipe[ingredient]
               
                for stock_item in ingredients:
                  if stock_item == 'milk' and ingredients[stock_item] > milk:
                              # print(f"if stock item {stock_item} == 'milk' and recipe[ingredient] {recipe[ingredient]} > milk {milk}")
                              print(f"{stock_item}, {ingredients[stock_item]} > {milk}")
                              print("You have enough milk!")
                              result+=1
                              
                  elif stock_item == 'milk' and ingredients[stock_item] < milk: 
                              print(f"You need {milk} milk but you only have this much {ingredients[stock_item]}")
                              return 0
                
                    
                  
          elif ingredient == 'butter':
                butter+=recipe[ingredient]
          elif ingredient == 'flour':
                flour+=recipe[ingredient]
          elif ingredient == 'cheese':
                cheese+=recipe[ingredient]
          elif ingredient == 'eggs':
                eggs+=recipe[ingredient]
          elif ingredient == 'sugar':
                sugar+=recipe[ingredient]
    

                 

  return result
              
  #  print(recipe[0]['milk'], "recipe")
 

print(recipe_batches(recipes, ingredients))

# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test 
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))


  # def test_recipe_batches(self):
  #       self.assertEqual(recipe_batches({ 'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5 }, { 'milk': 1288, 'flour': 9, 'sugar': 95 }), 0)
  #   self.assertEqual(recipe_batches({ 'milk': 100, 'butter': 50, 'cheese': 10 }, { 'milk': 198, 'butter': 52, 'cheese': 10 }), 1)
  #   self.assertEqual(recipe_batches({ 'milk': 2, 'sugar': 40, 'butter': 20 }, { 'milk': 5, 'sugar': 120, 'butter': 500 }), 2)
  #   self.assertEqual(recipe_batches({ 'milk': 2 }, { 'milk': 200}), 100)