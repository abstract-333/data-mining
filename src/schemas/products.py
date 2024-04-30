from enum import Enum
from typing import Final


class Products(Enum):
    Instant_food_products = "Instant food products"
    UHT_milk = "UHT-milk"
    abrasive_cleaner = "abrasive cleaner"
    artif_sweetener = "artif. sweetener"
    baby_cosmetics = "baby cosmetics"
    baby_food = "baby food"
    bags = "bags"
    baking_powder = "baking powder"
    bathroom_cleaner = "bathroom cleaner"
    beef = "beef"
    berries = "berries"
    beverages = "beverages"
    bottled_beer = "bottled beer"
    bottled_water = "bottled water"
    brandy = "brandy"
    brown_bread = "brown bread"
    butter = "butter"
    butter_milk = "butter milk"
    cake_bar = "cake bar"
    candles = "candles"
    candy = "candy"
    canned_beer = "canned beer"
    canned_fish = "canned fish"
    canned_fruit = "canned fruit"
    canned_vegetables = "canned vegetables"
    cat_food = "cat food"
    cereals = "cereals"
    chewing_gum = "chewing gum"
    chicken = "chicken"
    chocolate = "chocolate"
    chocolate_marshmallow = "chocolate marshmallow"
    citrus_fruit = "citrus fruit"
    cleaner = "cleaner"
    cling_film_bags = "cling film/bags"
    cocoa_drinks = "cocoa drinks"
    coffee = "coffee"
    condensed_milk = "condensed milk"
    cooking_chocolate = "cooking chocolate"
    cookware = "cookware"
    cream = "cream"
    cream_cheese = "cream cheese"
    cream_cheese_ = "cream cheese "
    curd = "curd"
    curd_cheese = "curd cheese"
    decalcifier = "decalcifier"
    dental_care = "dental care"
    dessert = "dessert"
    detergent = "detergent"
    dish_cleaner = "dish cleaner"
    dishes = "dishes"
    dog_food = "dog food"
    domestic_eggs = "domestic eggs"
    female_sanitary_products = "female sanitary products"
    finished_products = "finished products"
    fish = "fish"
    flour = "flour"
    flower_seeds = "flower (seeds)"
    flower_soil_fertilizer = "flower soil/fertilizer"
    frankfurter = "frankfurter"
    frozen_chicken = "frozen chicken"
    frozen_dessert = "frozen dessert"
    frozen_fish = "frozen fish"
    frozen_fruits = "frozen fruits"
    frozen_meals = "frozen meals"
    frozen_potato_products = "frozen potato products"
    frozen_vegetables = "frozen vegetables"
    fruit_vegetable_juice = "fruit/vegetable juice"
    grapes = "grapes"
    hair_spray = "hair spray"
    ham = "ham"
    hamburger_meat = "hamburger meat"
    hard_cheese = "hard cheese"
    herbs = "herbs"
    honey = "honey"
    house_keeping_products = "house keeping products"
    hygiene_articles = "hygiene articles"
    ice_cream = "ice cream"
    instant_coffee = "instant coffee"
    jam = "jam"
    ketchup = "ketchup"
    kitchen_towels = "kitchen towels"
    kitchen_utensil = "kitchen utensil"
    light_bulbs = "light bulbs"
    liqueur = "liqueur"
    liquor = "liquor"
    liquor_appetizer = "liquor (appetizer)"
    liver_loaf = "liver loaf"
    long_life_bakery_product = "long life bakery product"
    make_up_remover = "make up remover"
    male_cosmetics = "male cosmetics"
    margarine = "margarine"
    mayonnaise = "mayonnaise"
    meat = "meat"
    meat_spreads = "meat spreads"
    misc_beverages = "misc. beverages"
    mustard = "mustard"
    napkins = "napkins"
    newspapers = "newspapers"
    nut_snack = "nut snack"
    nuts_prunes = "nuts/prunes"
    oil = "oil"
    onions = "onions"
    organic_products = "organic products"
    organic_sausage = "organic sausage"
    other_vegetables = "other vegetables"
    packaged_fruit_vegetables = "packaged fruit/vegetables"
    pasta = "pasta"
    pastry = "pastry"
    pet_care = "pet care"
    photo_film = "photo/film"
    pickled_vegetables = "pickled vegetables"
    pip_fruit = "pip fruit"
    popcorn = "popcorn"
    pork = "pork"
    pot_plants = "pot plants"
    potato_products = "potato products"
    preservation_products = "preservation products"
    processed_cheese = "processed cheese"
    prosecco = "prosecco"
    pudding_powder = "pudding powder"
    ready_soups = "ready soups"
    red_blush_wine = "red/blush wine"
    rice = "rice"
    roll_products = "roll products"
    roll_products_ = "roll products "
    rolls_buns = "rolls/buns"
    root_vegetables = "root vegetables"
    rubbing_alcohol = "rubbing alcohol"
    rum = "rum"
    salad_dressing = "salad dressing"
    salt = "salt"
    salty_snack = "salty snack"
    sauces = "sauces"
    sausage = "sausage"
    seasonal_products = "seasonal products"
    semi_finished_bread = "semi-finished bread"
    shopping_bags = "shopping bags"
    skin_care = "skin care"
    sliced_cheese = "sliced cheese"
    snack_products = "snack products"
    soap = "soap"
    soda = "soda"
    soft_cheese = "soft cheese"
    softener = "softener"
    sound_storage_medium = "sound storage medium"
    soups = "soups"
    sparkling_wine = "sparkling wine"
    specialty_bar = "specialty bar"
    specialty_cheese = "specialty cheese"
    specialty_chocolate = "specialty chocolate"
    specialty_fat = "specialty fat"
    specialty_vegetables = "specialty vegetables"
    spices = "spices"
    spread_cheese = "spread cheese"
    sugar = "sugar"
    sweet_spreads = "sweet spreads"
    syrup = "syrup"
    tea = "tea"
    tidbits = "tidbits"
    toilet_cleaner = "toilet cleaner"
    tropical_fruit = "tropical fruit"
    turkey = "turkey"
    vinegar = "vinegar"
    waffles = "waffles"
    whipped_sour_cream = "whipped/sour cream"
    whisky = "whisky"
    white_bread = "white bread"
    white_wine = "white wine"
    whole_milk = "whole milk"
    yogurt = "yogurt"
    zwieback = "zwieback"


PRODUCTS_LIST: Final[list[str]] = [
    "Instant food products",
    "UHT-milk",
    "abrasive cleaner",
    "artif. sweetener",
    "baby cosmetics",
    "baby food",
    "bags",
    "baking powder",
    "bathroom cleaner",
    "beef",
    "berries",
    "beverages",
    "bottled beer",
    "bottled water",
    "brandy",
    "brown bread",
    "butter",
    "butter milk",
    "cake bar",
    "candles",
    "candy",
    "canned beer",
    "canned fish",
    "canned fruit",
    "canned vegetables",
    "cat food",
    "cereals",
    "chewing gum",
    "chicken",
    "chocolate",
    "chocolate marshmallow",
    "citrus fruit",
    "cleaner",
    "cling film/bags",
    "cocoa drinks",
    "coffee",
    "condensed milk",
    "cooking chocolate",
    "cookware",
    "cream",
    "cream cheese",
    "cream cheese ",
    "curd",
    "curd cheese",
    "decalcifier",
    "dental care",
    "dessert",
    "detergent",
    "dish cleaner",
    "dishes",
    "dog food",
    "domestic eggs",
    "female sanitary products",
    "finished products",
    "fish",
    "flour",
    "flower (seeds)",
    "flower soil/fertilizer",
    "frankfurter",
    "frozen chicken",
    "frozen dessert",
    "frozen fish",
    "frozen fruits",
    "frozen meals",
    "frozen potato products",
    "frozen vegetables",
    "fruit/vegetable juice",
    "grapes",
    "hair spray",
    "ham",
    "hamburger meat",
    "hard cheese",
    "herbs",
    "honey",
    "house keeping products",
    "hygiene articles",
    "ice cream",
    "instant coffee",
    "jam",
    "ketchup",
    "kitchen towels",
    "kitchen utensil",
    "light bulbs",
    "liqueur",
    "liquor",
    "liquor (appetizer)",
    "liver loaf",
    "long life bakery product",
    "make up remover",
    "male cosmetics",
    "margarine",
    "mayonnaise",
    "meat",
    "meat spreads",
    "misc. beverages",
    "mustard",
    "napkins",
    "newspapers",
    "nut snack",
    "nuts/prunes",
    "oil",
    "onions",
    "organic products",
    "organic sausage",
    "other vegetables",
    "packaged fruit/vegetables",
    "pasta",
    "pastry",
    "pet care",
    "photo/film",
    "pickled vegetables",
    "pip fruit",
    "popcorn",
    "pork",
    "pot plants",
    "potato products",
    "preservation products",
    "processed cheese",
    "prosecco",
    "pudding powder",
    "ready soups",
    "red/blush wine",
    "rice",
    "roll products",
    "roll products ",
    "rolls/buns",
    "root vegetables",
    "rubbing alcohol",
    "rum",
    "salad dressing",
    "salt",
    "salty snack",
    "sauces",
    "sausage",
    "seasonal products",
    "semi-finished bread",
    "shopping bags",
    "skin care",
    "sliced cheese",
    "snack products",
    "soap",
    "soda",
    "soft cheese",
    "softener",
    "sound storage medium",
    "soups",
    "sparkling wine",
    "specialty bar",
    "specialty cheese",
    "specialty chocolate",
    "specialty fat",
    "specialty vegetables",
    "spices",
    "spread cheese",
    "sugar",
    "sweet spreads",
    "syrup",
    "tea",
    "tidbits",
    "toilet cleaner",
    "tropical fruit",
    "turkey",
    "vinegar",
    "waffles",
    "whipped/sour cream",
    "whisky",
    "white bread",
    "white wine",
    "whole milk",
    "yogurt",
    "zwieback",
]
