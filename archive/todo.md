* In writemeals(), check that the meals conform to some standards before writing
    - I.e. check that all ingredients are supported for example
    - Could also have a method of Meal which checks for all these things
* Ability to move around suggestions easily in looprecomend
    - Could offer move to or swap
    - And then use indexes to easily do this
* Check that additionals / extras / sides are compliant in checkdatafiles script
    - And that there are no unexpected keys in any meals dictionary
* Need to sanity-check ingredients file: beans e.g. have sum = 202, some are measured in grams some in units
    - Wondering why some are measured in one and some in the other ...
    - Could use this ingredients measuredin to check meals.json is compliant
* Try changing meals, didn't work just now - seems to be too restrictive atm

* utils/display I think - there was a bug when running on Louisa's machine.
    - I imported Iterable from collections.abc, which was not subscriptable
    - Tried to use it as Iterable[float] e.g. in one of these scripts but supposedly that's not valid

* Add install instructions to repo README 
