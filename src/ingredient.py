from typing import Any
from typing import Iterable

from mealprep.src.constants import BaseEnum
from mealprep.src.constants import Category
from mealprep.src.constants import Unit


class Ingredient:
    def __init__(self, name: str, category: Category):
        if not isinstance(name, str):
            raise TypeError("'name' argument must be a string in Ingredient init")
        if not isinstance(category, Category):
            raise TypeError("'category' argument must be a Category in Ingredient init")

        self.name = name
        self.category = category


class IngredientQuantity:
    def __init__(self, ingredient: Ingredient, unit: Unit, quantity: Any):
        if not isinstance(ingredient, Ingredients):
            raise TypeError(
                "'ingredient' argument must be in the Ingredients enum in IngredientQuantity init"
            )
        if not isinstance(unit, Unit):
            raise TypeError(
                "'unit' argument must be a Unit in IngredientQuantity init"
            )

        self.ingredient = ingredient
        self.unit = unit
        self.quantity = quantity


class IngredientQuantityCollection:
    def __init__(self, ingredient_quantities: Iterable[IngredientQuantity]):
        self.ingredient_quantities = tuple(x for x in ingredient_quantities)

        for x in self.ingredient_quantities:
            if not isinstance(x, IngredientQuantity):
                raise TypeError(f"{x} is not an IngredientQuantity in IngredientQuantityCollection init")


class Ingredients(BaseEnum):
    BABY_SPINACH = Ingredient("Baby Spinach", Category.VEGETABLE)
    BAY_LEAVES = Ingredient("Bay Leaves", Category.HERB)
    BEEF_MINCE = Ingredient("Beef Mince", Category.MEAT)
    BROWN_SUGAR = Ingredient("Brown Sugar", Category.CONDIMENT)
    CARROT = Ingredient("Carrot", Category.VEGETABLE)
    CASTER_SUGAR = Ingredient("Caster Sugar", Category.CONDIMENT)
    CAYENNE_PEPPER = Ingredient("Cayenne Pepper", Category.SPICE)
    CELERY = Ingredient("Celery", Category.VEGETABLE)
    CHERRY_TOMATO = Ingredient("Cherry Tomato", Category.VEGETABLE)
    CHICKEN_BREAST = Ingredient("Chicken Breast", Category.MEAT)
    CHICKEN_STOCK = Ingredient("Chicken Stock", Category.CONDIMENT)
    CHICKEN_THIGH = Ingredient("Chicken Thigh", Category.MEAT)
    CHOPPED_TOMATO = Ingredient("Chopped Tomato", Category.CAN)
    CORIANDER = Ingredient("Coriander", Category.HERB)
    CREAM = Ingredient("Cream", Category.DAIRY)
    DARK_SOY_SAUCE = Ingredient("Dark Soy Sauce", Category.SAUCE)
    FRESH_CHILLI = Ingredient("Fresh Chilli", Category.VEGETABLE)
    FLOUR = Ingredient("Flour", Category.CONDIMENT)
    GARLIC_CLOVE = Ingredient("Garlic Clove", Category.VEGETABLE)
    GINGER = Ingredient("Ginger", Category.VEGETABLE)
    GUINNESS = Ingredient("Guinness", Category.SAUCE)
    HONEY = Ingredient("Honey", Category.CONDIMENT)
    KIDNEY_BEAN = Ingredient("Kidney Bean", Category.CAN)
    LEMONGRASS_PASTE = Ingredient("Lemongrass Paste", Category.CONDIMENT)
    MIXED_HERBS = Ingredient("Mixed Herbs", Category.HERB)
    MOZARELLA_CHEESE = Ingredient("Mozarella Cheese", Category.DAIRY)
    OLIVE_OIL = Ingredient("Olive Oil", Category.CONDIMENT)
    ONION = Ingredient("Onion", Category.VEGETABLE)
    OREGANO = Ingredient("Oregano", Category.HERB)
    PAPRIKA = Ingredient("Paprika", Category.SPICE)
    PARMESAN_CHEESE = Ingredient("Parmesan Cheese", Category.DAIRY)
    PEAR = Ingredient("Pear", Category.FRUIT)
    PENNE_PASTA = Ingredient("Penne Pasta", Category.CARBOHYDRATE)
    PORK_BELLY_SLICE = Ingredient("Pork Belly Slice", Category.MEAT)
    PORK_MINCE = Ingredient("Pork Mince", Category.MEAT)
    POTATO = Ingredient("Potato", Category.VEGETABLE)
    RED_CHILLI = Ingredient("Red Chilli", Category.VEGETABLE)
    RED_ONION = Ingredient("Red Onion", Category.VEGETABLE)
    RED_PEPPER = Ingredient("Red Pepper", Category.VEGETABLE)
    RICE = Ingredient("Rice", Category.CARBOHYDRATE)
    RICE_WINE = Ingredient("Rice Wine", Category.SAUCE)
    SPAGHETTI = Ingredient("Spaghetti", Category.CARBOHYDRATE)
    STEWING_BEEF = Ingredient("Stewing Beef", Category.MEAT)
    SUNDRIED_TOMATOES = Ingredient("Sundried Tomatoes", Category.CAN)
    TOMATO_PUREE = Ingredient("Tomato Puree", Category.CONDIMENT)
    TORTILLA_WRAP = Ingredient("Tortilla Wrap", Category.CARBOHYDRATE)
    VEGETABLE_OIL = Ingredient("Vegetable Oil", Category.CONDIMENT)
    YELLOW_PEPPER = Ingredient("Yellow Pepper", Category.VEGETABLE)
