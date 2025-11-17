import yaml

yaml_file = open("test.yaml", "r")

parsed_yaml = yaml.safe_load(yaml_file)

print(parsed_yaml)
# {'a': 1, 'b': {'c': 3, 'd': 4}, 'liste': ['valeur', 'autre valeur']}

print(parsed_yaml["a"])
# 1

for key in parsed_yaml["b"]:
    print("key:", key, ", value:", parsed_yaml["b"][key])
# key: c, value: 3
# key: d, value: 4

print(parsed_yaml["b"]["c"])
# 3

for value in parsed_yaml["liste"]:
    print(value)
# valeur
# autre valeur
