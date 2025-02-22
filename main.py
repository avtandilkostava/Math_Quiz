import random

f = open('questions.txt', 'r')
f1 = open('Users.txt', 'a')

name = input('Your Name -> ')
cnt = int(input('Number of questions -> '))

users = ['name']
e = ''
c = 0
s = []
for j in range(0, int(f.readline())):
    e = ''
    a = f.readline().split(';')
    for k in range(0, len(a[5]) - 1):
        e += a[5][k]
    a[5] = e
    s.append(a)


for i in range(0, cnt):
    print(''
          '*******************************************************'
          '')
    s1 = random.choice(s)

    print(f'{i+1}) {s1[0]}')
    print(f'A) {s1[1]}, B) {s1[2]}, C) {s1[3]}, D) {s1[4]}')

    ans = input('Your answer -> ')
    print()
    t = True
    for j in range(0, 4):
        if s1[ord(ans) - 64] == s1[5]:
            t = False
    if t:
        print('Ooops, wrong answer')
    else:
        print('Correct')
        c += 1

print(f'Result -> {c}/{cnt}')

f1.write(f'{name}, {c}/{cnt} ')
f1.write(""
         "")
f1.close()
f.close()
