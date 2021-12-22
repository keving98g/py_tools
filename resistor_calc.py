import math

E12 = [1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2]
E24 = [1, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2.0, 2.2, 2.4, 2.7, 3.0, 3.3, 3.6, 3.9, 4.3, 4.7, 5.1, 5.6, 6.2, 6.8, 7.5, 8.2, 9.1]

def find_closest(res_list, res):
    index_min = 0
    index_max = len(res_list) + 1
    index = math.floor((index_min + index_max)/2)
    i = 0
    while (index_max - index_min) > 1 and i < 100:
        if res_list[index] == res:
            break
        elif (res_list[index] > res):
            index_max = index
        elif (res_list[index] < res):
            index_min = index
        index = math.floor( (index_min + index_max) / 2)
        i+=1
    if (index < len(res_list)):
        tol1 = abs(res_list[index] / res - 1.0)
        tol2 = abs(res_list[index + 1] / res - 1.0)
        if (tol1 < tol2):
            return index
        else:
            return (index + 1)
    else:
        return index

print(E12[find_closest(E12, 1.8)])
