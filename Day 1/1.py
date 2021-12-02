file1 = open("input.txt", "r")

data = []

for item in file1.readlines():
    _data = item
    data.append(int(_data))

ind_min = 0
measurements = 0
for i in range(1,len(data)):
    if data[ind_min] < data[i]:
        measurements += 1

    ind_min += 1

print(measurements)

measurements2 = 0

for i in range(0, len(data)-3):
    a = data[i] + data[i+1] + data[i+2]
    b = data[i+1] + data[i+2] + data[i+3]
    if b > a:
        measurements2 += 1

print(measurements2)