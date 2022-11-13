from pprint import pprint

list_of_dicts = [{'bin': bin(i), 'dec': i, 'oct': oct(i), 'hex': hex(i)} for i in range(0, 16)]
pprint(list_of_dicts)