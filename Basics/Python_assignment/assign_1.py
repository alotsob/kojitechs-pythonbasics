
import builtins
from pprint import pprint

items = [
    ("product1", 100),
    ("product2", 140),
    ("product3", 250),
    ("product4", 200)
]
# The for_loop expression
for item in items:
    if item[1] >= 200:
        print(item)
