a = [0]*100
t = 0
total = 0
count = 0


def part(x, n):
    global t, total, count
    for i in reversed(range(1, x+1)):
        if i+total <= n:
            a[t] = i
            t += 1
            total += i
            part(i, n)
    if total == n:
        count += 1
        print("{}=".format(n), end='')
        for j in range(0, t):
            print(a[j], end='')
            if j < t-1:
                print('+', end='')
            else:
                print()
    t -= 1
    total -= a[t]


k = int(input('please input k:'))
part(k, k)
