n = int(input("1부터 n까지의 숫자 중 짝수의 합을 구할 n을 입력하세요: "))

nums = [x for x in range(1, n+1) if x % 2 == 0]
print(sum(nums))