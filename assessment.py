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
    Evaluate provided town name.  Return true if it is my hometown.
    """
    if town_name == "Baton Rouge":
        return True
    else:
        return False

# Checking the function.
print is_hometown("Baton Rouge")
print is_hometown("Walnut Creek")


#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.

def full_name(first_name, last_name):
    """
    Return concatenation of two input strings.
    """
    return first_name + " " + last_name

# Checking the function.
print full_name("Charley", "McLean")
print full_name("Alex", "McLean")

#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you
#        from?" depending on what `is_hometown()` evaluates to.

def hometown_greeting(town_name, first_name, last_name):
    """
    Print a greeting.  Call is_hometown function and full_name function.
    """
    if is_hometown(town_name):
        print "Hi, " + full_name(first_name, last_name) + ", we're from the same place!"
    else:
        print "Hi " + full_name(first_name, last_name) + ", where are you from?"

# Checking the function.
hometown_greeting("Sarnia", "Alex", "McLean")
hometown_greeting("Baton Rouge", "Lynn", "Lalka") 

#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()``
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.

def increment(x = 1):
    """
    A function that takes a parameter, x, which defaults to 0 if no value
    is provided.  This is passed to an inner function which takes a 
    parameter, y.  The sum of x and y is returned.
    """
    def add(y):
        return x + y
    return add

# Checking the function.
add_ten = increment()
print add_ten(10)

add_twenty = increment(2)
print add_twenty(20)


# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call 
#    addfive with y = 5. Call again with y = 20.

addfive = increment(5)
print addfive(5)
print addfive(20)

# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.

def append_number(number, list_of_numbers):
    """
    Append a number to a list.
    """
    list_of_numbers.append(number)
    return list_of_numbers

# Checking the function.
print append_number(5, [1, 2, 3, 4])

#####################################################################