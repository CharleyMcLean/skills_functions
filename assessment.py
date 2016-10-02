# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5%

def calc_full_item_cost(item_cost, state_abbrev, tax = 0.05):
    """
    Calculate the full item cost based on the item cost and tax rate.
    The tax string default is 5%.  If the state is California, the tax
    rate is 7%
    """
    if state_abbrev == "CA":
        tax = 0.07
    return item_cost + item_cost * tax

# Checking the function.
print calc_full_item_cost(5.00, "CA")
print calc_full_item_cost(5.00, "TX")


#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or 
#        "blackberry".

def is_berry(fruit):
    """
    Check if the input fruit is a berry.  Return a boolean.
    """
    if fruit == "strawberry" or fruit == "cherry" or fruit == "blackberry":
        return True
    else:
        return False

# Checking the function.
print is_berry("strawberry")
print is_berry("cherry")
print is_berry("blackberry")
print is_berry("apple")

#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function 
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.


def shipping_cost(fruit):
    """
    Calculate shipping cost based on fruit type.  Call is_berry function
    to determine the fruit type.
    """
    if is_berry(fruit) == True:
        return 0
    else:
        return 5

# Checking the function.
print shipping_cost("strawberry")
print shipping_cost("cherry")
print shipping_cost("blackberry")
print shipping_cost("apple")

# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.

def is_hometown(town_name):
    """


#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.
#
#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you 
#        from?" depending on what `is_hometown()` evaluates to.

#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()`` 
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.

# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call 
#    addfive with y = 5. Call again with y = 20.

# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.

#####################################################################