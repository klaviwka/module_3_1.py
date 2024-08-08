calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    length = len(string)
    upper = string.upper()
    lower = string.lower()
    return (length, upper, lower)

def is_contains(string, list_to_search):
    count_calls()
    return string.lower() in (item.lower() for item in list_to_search)


print(string_info("Moneymaker"))
print(string_info("Nintendo"))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains("Becon", ["Milk", "Juice", "lemon"]))
print(calls)
