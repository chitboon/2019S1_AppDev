def get_lowest(my_dict):

    part_name = ''
    lowest = 100

    for key in my_dict:
        if my_dict[key] < lowest:
            part_name = key
            lowest = my_dict[key]

    return part_name

result = {}
for i in range(5):
    name = input("Enter name: ")
    score = int(input("Enter score: "))
    result[name] = score
print(result)

print(get_lowest(result), "has the lowest score.")
