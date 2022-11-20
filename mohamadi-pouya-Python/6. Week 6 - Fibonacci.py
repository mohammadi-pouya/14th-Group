def fib(n):
    previous, current = 0, 0
    for i in range(n + 1):
        if i == 0:
            previous = i
            print(previous)
        elif i == 1:
            current = i
            print(current)
        else:
            previous, current = current, previous + current
            print(current)

# Solution2
def fibo(n):
    f0 = 0
    f1 = 1
    for i in range(n + 1):
        next_num = f0 + f1
        yield f0
        f0 = f1
        f1 = next_num
    

if __name__ == '__main__':
    fib(20)
    
    for item in fibo(20):
        print(item)
