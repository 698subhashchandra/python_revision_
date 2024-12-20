from operator import itemgetter

def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem

    raise RuntimeError(f"Could not find an element with {expected}.")

fridends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne pun", "age": 29},
]

print((search(fridends, "Rolf Smith", itemgetter("name"))))