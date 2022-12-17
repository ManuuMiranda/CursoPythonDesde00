# Loading data


def max_cal_txt(path):
    with open(path) as txt:
        data = [cal for cal in txt.read().strip().split("\n")]
    maxi = 0
    cont = 0
    for item in data:
        if item == '':
            cont = 0
        else:
            num = int(item)
            cont += num

        if cont > maxi:
            maxi = cont

    return f'The Answer Is: {maxi}'


print(max_cal_txt('Advent Of Code 2022/DAY 01/calorie_counting.txt'))
print(max_cal_txt('calorie_counting.txt'))
# La parte 2 se haría creando más variables max y razonando en este caso, haciendo lo mismo 2 veces más. INEFICIENTE

###################################################################################


def sorted_answer(path):
    with open(path) as txtx:
        datax = [cal for cal in txtx.read().strip().split("\n")]
    listx = []
    for elem in datax:
        if elem == '':
            sum(listx)
        else:
            listx.append(int(elem))
    return sorted(listx, reverse=True)


max(sorted_answer('Advent Of Code 2022/DAY 01/input.txt'))
sorted_answer('Advent Of Code 2022/DAY 01/input.txt')[:3]
sum(sorted_answer('Advent Of Code 2022/DAY 01/input.txt')[:3])

max(sorted_answer('Advent Of Code 2022/DAY 01/calorie_counting.txt'))
sorted_answer('Advent Of Code 2022/DAY 01/input.txt')[:3]
sum(sorted_answer('Advent Of Code 2022/DAY 01/calorie_counting.txt')[:3])


###################################################################################


with open("Advent Of Code 2022/DAY 01/calorie_counting.txt", "r") as txt:
    data = txt.read()

contmax = 0
conti = 0
for n in data.split("\n"):
    if len(n) == 0:
        conti = 0
    else:
        conti += int(n)
    # imrpriem esto si no lo entiendes: print(conti)
    contmax = max(contmax, conti)

print(contmax)


def sum_three_max(path):
    with open(path, "r") as f:
        data = f.read()

    sums = []
    s = 0
    for l in data.split("\n"):
        if len(l) == 0:
            sums.append(s)
            s = 0
        else:
            s += int(l)

    sums.append(s)
    sums.sort()
    return sum(sums[-1] + sums[-2] + sums[-3])


sum_three_max('Advent Of Code 2022/DAY 01/calorie_counting.txt')