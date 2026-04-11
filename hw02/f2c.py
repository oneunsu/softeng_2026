def f2c(temp_f):
    return (temp_f - 32) * 5.0/9.0

temp_f = float(input("화씨 온도를 입력하세요: "))
temp_c = f2c(temp_f)
print(f"화씨 {temp_f}도는 섭씨 {temp_c:.2f}도입니다.")