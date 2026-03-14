def is_even(number):
    if number % 2 == 0:
        return "짝수"
    else:
        return "홀수"

num = int(input("숫자를 입력하세요: "))
print(f"{num}은(는) {is_even(num)}입니다.")