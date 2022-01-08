def prime(n):
    if n == 1:
        print("This number is not prime")

    elif n % 2 == 0:
        print("This number is not prime")
    else:
        for i in range(3, int((n + 1) / 2)):
            if n % i == 0:
                print("This number is not prime")
                break
        print("This number is prime")


a = int(input())
prime(a)
