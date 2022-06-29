import sys, os
sys.path.append(os.path.dirname(os.path.abspath((os.path.dirname(__file__)))))
from etc.keys import get_aladin_keys

keys = get_aladin_keys()
print(keys)

