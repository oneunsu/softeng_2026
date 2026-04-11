def fact(n):
        if n ==1:
            return 1
        return n * fact(n - 1)

num = int(input("숫자를 입력하세요: "))
print(fact(num))