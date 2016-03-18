ile = 0
while ile not in range (1,10):
    ile = int(raw_input())

for i in range(ile):
    a = raw_input()
    a = a.split()
    while (int(a[0]) not in range(1,1000000)) |\
            (int(a[1]) not in range(1,1000000)):
        a = raw_input()
        a = a.split()

    ostatnia = str(int(a[0])**int(a[1]))
    print(ostatnia[-1])
    a = []