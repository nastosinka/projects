yaml = []

file1 = open('lab3.yaml')
s = file1.readlines()

now = 0 

for i in range(1, len(s)): 

    j = 0
    while not s[i][j].isalpha(): 
        s[i] = s[i][j + 1:]
        j += 1

    s[i] = s[i][0:-1] 

    j = 0
    while j < len(s[i]): 
        if s[i][j] == ":":

            if "'" in s[i]:
                flag = False
                ind = "'".find(s[i])
                next_str = ""
                s[i] = s[i][1:j]

            else:
                flag = True
                next_str = s[i][j + 2:]
                s[i] = s[i][:j]
        j += 1
    current = "<" + s[i] + ">"

    if flag == True:
        current = "<" + s[i] + ">" + next_str + "</" + current[1:]
        yaml.insert(now, count * 3 * " " + current)

    else: 
        count = 1
        yaml.append(count * 3 * " " + current)
        now = len(yaml)
        current = "</" + current[1:]
        yaml.append(count * 3 * " " + current)
        count += 1


first = "<" + s[0][:-2] + ">"
yaml.insert(0, first)
first = "</" + first[1:]
yaml.append(first)

for i in range(len(yaml)):
    print(yaml[i])





























'''
yaml = []
file1 = open('C://Users/osink/Downloads/lab3.yaml')
s = file1.readlines()
count = 0 # счётчик количества опущенных пробелов
for i in range(len(s)):
    count = 0
    j = 0 # идея: счётчик, который будет считать колво опущенных пробелов в строке
    while s[i][j] == "	" or s[i][j] == "-":
        if s[i][j] == "-": # убираем чёрточки
            s[i] = s[i][j + 1:]
            j += 1
        if s[i][j] == "	": # убираем пробелы
            count += 1
            s[i] = s[i][j + 1:]
    ans = "	" * count + "<" # составляем заготовку для строки
    for z in range(len(s[i]) - j):
        ans += s[i][z + j] # прибавляем
    ans = ans[0:-1]
    s[i] = ans + ">"
    print(s[i])


'''
