"""
에라토스테네스의 체 알고리즘 활용
https://kimwooil.tistory.com/435 참고
"""

def get_primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False

    return [i for i in range(2, n+1) if is_prime[i]]

limit = int(input("소수를 찾을 범위를 입력하세요: "))
primes = get_primes(limit)
print(f"{limit} 이하의 소수: {primes}")