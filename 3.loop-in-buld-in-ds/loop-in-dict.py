# 1. Loop Through Keys (default behavior)
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key in my_dict:
    print(key, my_dict[key])




#2. Loop Through .keys() only
for key in my_dict.keys():
    print(key, my_dict[key])



#3. Loop Through .values() only
for value in my_dict.values():
    print(value)



# 4. get the key, value pair togather (Key + Value)
for key, value in my_dict.items():
    print(f"{key} -> {value}")


#5. get key, value pair and index with enumerate()
for index, (key, value) in enumerate(my_dict.items()):
    print(index, key, value)