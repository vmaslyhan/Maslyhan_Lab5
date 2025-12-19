import re

items = [
    "English",
    "інформація",
    "android",
    "Windows",
    "Добрий день",
    "матриця",
    "актова зала",
    "біоресурси",
    "єдиний",
    "кава"
]

UA_ALPHABET = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
UA_ALPHABET += UA_ALPHABET.upper()

UA_ORDER = {char: idx for idx, char in enumerate(UA_ALPHABET)}

CYRILLIC_RE = re.compile(r'^[\u0400-\u04FF]')

def starts_with_cyrillic(s: str) -> bool:
    return bool(CYRILLIC_RE.match(s.strip()))

def ua_sort_key(s: str):
    s = s.strip()
    group = 0 if starts_with_cyrillic(s) else 1
    if group == 0:
        key = tuple(UA_ORDER.get(c.lower(), ord(c)) for c in s)
    else:
        key = s.casefold()
    return (group, key)

sorted_items = sorted(items, key=ua_sort_key)

print("Заданий список:")
print(items)
print("\nВідсортований список:")
print(sorted_items)