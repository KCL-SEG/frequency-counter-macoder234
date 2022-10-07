"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""


def frequencies(items):

    frequencies = {}

    newList = []
    for x in items:
        if isinstance(x, str):
            newList.append(x)
        else:
            newList.append(f"{x}")

    for x in newList:
        frequencies.update({x: newList.count(x)})

    print(frequencies)

    return frequencies


# while True:
#     try:
#         items = [input().split(",")]
#         frequencies(items)
#     except ValueError:
#         print("Some input could not be converted to a number!")
#     else:
#         break
