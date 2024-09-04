import importlib

hyphen_module = importlib.import_module('task8_data-helper')

print(hyphen_module.get_random_date())
print(hyphen_module.get_random_string())
print(hyphen_module.get_random_integer())
print(hyphen_module.get_random_double())
