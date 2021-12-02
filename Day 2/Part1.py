file1 = open("input.txt", "r")

data = []
for item in file1.readlines():
    data_temp = item.split(" ")
    data_temp[1] = int(data_temp[1])

    data.append(data_temp)

position = 0
depth = 0
for item in data:
    movement = item[0]
    nb = int(item[1])

    if movement == "forward":
        position += nb
    elif movement == "down":
        depth += nb
    elif movement == "up":
        depth -= nb

print(position, depth)
print(position * depth)
