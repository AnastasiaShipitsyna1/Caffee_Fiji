#list of ingridients
ingredients = [
    "eggs",
    "sugar brown",
    "sugar white",
    "milk",
    "whipping cream",
    "cacao",
    "almonds",
    "peanuts",
    "dark chocolate",
    "white chocolate",
    "milck chocolate",
    "mango puree",
    "passionfruit puree",
    "coconut milk",
    "matcha",
    "coffe",
    "chia seeds",
    "canola oil",
    "butter",
    "Oranges",
    "pineapple fresh",
    "pineapple puree",
    "coconut grated",
    "lemon",
    "lime",
    "mixed berries",
    "raspeberries",
    "blueberries",
    "mint",
    "Oreo cookies",
    "peanut butter",
    "pearl",
    "jam",
    "flour",
    "food colour",
    "soda",
    "sugar icing"
    "delivery"
]




#prices
price_eggs = 17/30
price_sugar = 6/1000
price_milk = 3/900
price_gelatin = 15/125
price_whipping_cream = 25/850
price_cacao = 7/100
price_decoration = 10
price_delivery = 25

#sizes of cakes
sizes = [
    "6 inches",
    "7 inches",
    "8 inches",
    "9 inches",
    "10 inches",
    "11 inches",
    "12 inches",
    "4 inches"
]

#Triple Chocolate
cake_1 = "Triple Chocolate Mousse Cake"
#recipe_Triple_Chocolate = [eggs + sugar + milk + gelatin + whipping_cream + cacao + decoration + delivery]

#size_6 ="6 inches"
eggs = 6
sugar = (eggs * 50)
milk = (eggs * 50)
gelatin = (eggs * 5)
whipping_cream = (eggs * 50)
cacao = (eggs * 5)

total_Triple_Choccolate_size_6 = (price_eggs * eggs + price_sugar *sugar + price_milk * milk + price_gelatin * gelatin 
                                 + price_whipping_cream * whipping_cream + price_decoration + price_delivery)

print(cake_1, ":",  "$", total_Triple_Choccolate_size_6 *2)
