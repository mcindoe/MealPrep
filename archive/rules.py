"""
Provides the available rules on which to limit the meals which can be
selected for a given date

A meal dictionary is a dictionary name: meal_info as  found in the meals
JSON file. meal_info contains metadata on the meal.

A rule is a filtering of a meal dictionary, which accepts and returns a
meal dictionary. We also provide a suitable history and any current
recommendations which is expected to be of interest to all rules. An
example is so that we know what meal was suggested yesterday and don't
want to suggest that meal today.

We ensure that rules have a common interface. To accomplish this, we
provide all information which may be relevant to each rule. We require
rules to take the form:

rule(meals, date, combined_history)

where meals is the meals dictionary, date is the date on which a meal
choice is being made, and combined_history is a dictionary which
contains some suitably long recent history of meals, as well as any
recommendations for the current week which may in general be before or
after the current date. From the purpose of filtering, these histories
are indistinguishable. Rules must be implemented in a forward- and
backward-looking fashion. E.g. ensure that we don't suggest a meal today
which is suggested tomorrow already in the combined_history.
"""


import datetime as dt
from typing import Dict

from mealprep.src.utils.history import get_close_history_meal_names
from mealprep.src.utils.meals import Meal
from mealprep.src.utils.meals import get_protein
from mealprep.src.utils.meals import is_favourite
from mealprep.src.utils.meals import is_fish
from mealprep.src.utils.meals import is_pasta
from mealprep.src.utils.meals import is_roast
from mealprep.src.utils.meals import is_time_consuming


def not_consecutive_same_protein(
    meals: Dict[str, Dict],
    date: dt.date,
    combined_history: Dict[dt.date, Meal],
) -> Dict[str, Dict]:

    """
    Do not recommend the same protein two days in a row
    """

    relevant_meal_names = get_close_history_meal_names(
        combined_history, date, n_days=1
    )

    proteins_to_avoid = []
    for meal_name in relevant_meal_names:
        if get_protein(meal_name) is not None:
            proteins_to_avoid.append(get_protein(meal_name))

    return {
        name: meal_info
        for name, meal_info in meals.items()
        if get_protein(name) not in proteins_to_avoid
    }


def not_within_seven_days(
    meals: Dict[str, Dict],
    date: dt.date,
    combined_history: Dict[dt.date, Meal],
) -> Dict[str, Dict]:

    """
    Do not recommend the same meal within seven days of previous occurrence
    """

    relevant_meal_names = get_close_history_meal_names(
        combined_history, date, n_days=7
    )

    return {
        name: meal_info
        for name, meal_info in meals.items()
        if name not in relevant_meal_names
    }


def not_non_favourite_within_fourteen_days(
    meals: Dict[str, Dict],
    date: dt.date,
    combined_history: Dict[dt.date, Meal],
) -> Dict[str, Dict]:

    """
    Do not recommend any non-favourite meal within fourteen days of
    previous occurrence
    """

    relevant_meal_names = get_close_history_meal_names(
        combined_history, date, n_days=14
    )

    return {
        name: meal_info
        for name, meal_info in meals.items()
        if is_favourite(name) or name not in relevant_meal_names
    }


def not_pasta_within_five_days(
    meals: Dict[str, Dict],
    date: dt.date,
    combined_history: Dict[dt.date, Meal],
) -> Dict[str, Dict]:

    """
    Do not recommend pasta dishes within five days of previous occurrence
    """

    relevant_meal_names = get_close_history_meal_names(
        combined_history, date, n_days=5
    )

    if any([is_pasta(meal) for meal in relevant_meal_names]):
        return {
            name: meal_info
            for name, meal_info in meals.items()
            if not is_pasta(name)
        }

    return meals


def force_sunday_roast(
    meals: Dict[str, Dict],
    date: dt.date,
    combined_history: Dict[dt.date, Meal],
) -> Dict[str, Dict]:

    """
    Recommend only roasts on a Sunday
    """

    if date.weekday() != 6:
        return meals

    return {
        name: meal_info for name, meal_info in meals.items() if is_roast(name)
    }


def not_roast_on_non_sunday(
    meals: Dict[str, Dict],
    date: dt.date,
    combined_history: Dict[dt.date, Meal],
) -> Dict[str, Dict]:

    """
    If not on Sunday, do not recommend a roast
    """

    if date.weekday() == 6:
        return meals

    return {
        name: meal_info
        for name, meal_info in meals.items()
        if not is_roast(name)
    }


def not_fish_within_seven_days(
    meals: Dict[str, Dict],
    date: dt.date,
    combined_history: Dict[dt.date, Meal],
) -> Dict[str, Dict]:

    """
    Do not recommend fish dishes within seven days of previous occurrence
    """

    relevant_meal_names = get_close_history_meal_names(
        combined_history, date, n_days=7
    )

    if any([is_fish(meal) for meal in relevant_meal_names]):
        return {
            name: meal_info
            for name, meal_info in meals.items()
            if not is_fish(name)
        }

    return meals


def not_time_consuming_on_weekend(
    meals: Dict[str, Dict],
    date: dt.date,
    combined_history: Dict[dt.date, Meal],
) -> Dict[str, Dict]:

    """
    Do not recommend dishes which are marked as time-consuming on a weekend
    """

    if date.weekday() not in [5, 6]:
        return meals

    return {
        name: meal_info
        for name, meal_info in meals.items()
        if not is_time_consuming(name)
    }


def not_lasagne_and_moussaka_within_seven_days(
    meals: Dict[str, Dict],
    date: dt.date,
    combined_history: Dict[dt.date, Meal],
) -> Dict[str, Dict]:

    """
    Do not recommend moussaka within seven days of a lasagne
    """

    relevant_meal_names = get_close_history_meal_names(
        combined_history, date, n_days=7
    )

    if "Moussaka" in relevant_meal_names:
        meals = {
            name: meal_info
            for name, meal_info in meals.items()
            if name != "Lasagne"
        }

    if "Lasagne" in relevant_meal_names:
        meals = {
            name: meal_info
            for name, meal_info in meals.items()
            if name != "Moussaka"
        }

    return meals
