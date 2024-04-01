from allpairspy import AllPairs

data = [
    ["DELL", "ACER", "ASUS", "HP"],
    ["WIN7", "XP", "WIN10", "Linux"],
    ["AMD", "INTEL", "ARM"],
]


def is_valid_combination(row):
    if len(row) > 1:
        if row[0] == "DELL" and row[1] == "XP":
            return False
    return True


pairwised_result = list(AllPairs(data))

for item in pairwised_result:
    print(item)
