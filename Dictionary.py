my_dict = {'key_1': 'val_1', 'key_2': 'val_2'}      # Use my_dict[key] to get or set the value.

keys_view = my_dict.keys()                          # Collection of keys that reflects changes.
values_view = my_dict.values()                      # Collection of values that reflects changes.
items_view = my_dict.items()                        # Collection of key-value tuples that reflects changes.

value = my_dict.get('key_1', default=None)          # Returns default if key is missing.
value = my_dict.setdefault('key_3', default='val_3')# Returns and writes default if key is missing.

import collections
default_dict = collections.defaultdict(str)         # Returns a dict with default value str().
default_dict_with_1 = collections.defaultdict(lambda: 1) # Returns a dict with default value 1.

dict_from_collection = dict([('a', 1), ('b', 2)])   # Creates a dict from collection of key-value pairs.
dict_from_zip = dict(zip(['a', 'b'], [1, 2]))       # Creates a dict from two collections.
dict_from_keys = dict.fromkeys(['a', 'b'], 0)       # Creates a dict from collection of keys.

my_dict.update({'key_4': 'val_4'})                  # Adds items. Replaces ones with matching keys.
removed_value = my_dict.pop('key_1', None)          # Removes item or returns None if missing.
keys_with_value = {k for k, v in my_dict.items() if v == 'val_2'}    # Returns set of keys that point to the value.
filtered_dict = {k: v for k, v in my_dict.items() if k in ['key_2', 'key_4']}  # Filters the dictionary by keys.






