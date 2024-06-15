def get_key_value(my_dict, key):
    return my_dict.get(key, None)

print(get_key_value({"a": 1}, "b"))

# 'b' isn't in the dictionary, .get() is an alternative to check without throwing error
# it can be further simplified by provided the argument to return if key is not found
