import numpy as np
import scipy.io as io

name = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
pic_dict = {"bar": 0, "clock": 1, "pie": 2, "race": 3}
pic_dict_rev = {0: "bar", 1: "clock", 2: "pie", 3: "race"}
num_dict = {"3": 0, "30": 1, "76": 2, "97": 3}

size_a = 4
size_b = 4
size_c = len(name)
data = np.zeros((size_a, size_b, size_c), dtype=np.float16)
pic = np.zeros((size_a, size_b * size_c), dtype=np.float16)

def read_data(file, id_c):
    for lines in file:
        ele = lines.split(" ")
        id_a = pic_dict[ele[0]]
        id_b = num_dict[ele[1]]

        real = float(ele[1])
        pred = float(ele[2])

        # diff = abs(pred - real)
        diff = pred - real

        data[id_a][id_b][id_c] = diff

for i in range(size_c):
    path = name[i] + ".txt"
    file = open(path, "r")
    read_data(file, i)

for i in range(size_a):
    for j in range(size_b):
        for k in range(size_c):
            index = size_c * j + k
            pic[i][index] = data[i][j][k]

io.savemat("../matlab/data.mat", {'data': data})
io.savemat("../matlab/pic.mat", {'pic': pic})
for i in range(size_a):
    io.savemat("../matlab/{}.mat".format(pic_dict_rev[i]), {pic_dict_rev[i]: pic[i]})

print("Finish!")
