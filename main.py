import random

f = open('questions.txt', 'r')

d = {}
name = input('Your Name -> ')
cnt = int(input('Number of questions'))

c = 0
s = list(list(f.readlines().split(';')))
for i in range(0, cnt):
    print(''
          '*******************************************************')
    s1 = random.choise(s)
    print(f'{i+1}) {s1[0]}')
    print(f'A) {s1[1]}, B) {s1[2]}, C) {s1[3]}, D) {s1[4]}')
    ans = input('Your answer -> ')
    t = True
    for j in range(0, 4):
        if s1[ord(ans) - 64] == s1[5]:
            t = False
    if t:
        print('Ooops, wrong answer')
    else:
        print('Correct')
        c += 1
        
f.close()
