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


