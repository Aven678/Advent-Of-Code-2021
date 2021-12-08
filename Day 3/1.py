data = [x for x in open("input.txt", "r").readlines()]
data_dict = {}

for i in data:
    for j in range(0, len(i)-1):
        if j in data_dict:
            _data = data_dict[j]
            if i[j] == "1":
                _data = (_data[0], _data[1]+1)
            else:
                _data = (_data[0]+1, _data[1])

            data_dict[j] = _data

        else:
            if i[j] == "1":
                data_dict[j] = (0,1)
            else:
                data_dict[j] = (1,0)

gamma = ""
epsilon = ""

for k in data_dict:
    _data = data_dict[k]
    if _data[0] > _data[1]:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1" 
        epsilon += "0"      

print(int(gamma, 2) * int(epsilon, 2))