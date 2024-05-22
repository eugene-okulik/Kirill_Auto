my_dict = {
    "tuple": (1, "one", 2, "two", 5),
    "list": [1, 2, 3, 4, 5],
    "dict": {"one": "apple", "fruit": "cherкy", "animals": "bear"},
    "set": {2, None, 4.5, False, 8}
}

# last_element1 = my_dict.get('two', 5)
last_element2 = my_dict["tuple"][-1]

my_dict["list"].append(6)
del my_dict["list"][1]

my_dict["dict"][("i am a tuple",)] = 3
del my_dict["dict"]["one"]

my_dict["set"].add(True)
my_dict["set"].remove(8)

print(last_element2)
print(my_dict)
