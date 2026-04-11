"""
Codex 활용 코드
2 미만 숫자 처리 기능 추가
prompt:
[get_primes_gui.py](hw03/get_primes_gui.py) 코드의 입력, 출력을 rich 라이브러리, gui 라이브러리(tkinter) 활용하여 최소 수정으로 꾸며줘.
"""

from tkinter import Tk, messagebox, simpledialog

from rich.console import Console
from rich.panel import Panel


def get_primes(n):
    if n < 2:
        return []

    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    return [i for i in range(2, n + 1) if is_prime[i]]


console = Console()
root = Tk()
root.withdraw()

limit = simpledialog.askinteger("소수 찾기", "소수를 찾을 범위를 입력하세요:", parent=root)

if limit is None:
    console.print("[yellow]입력이 취소되었습니다.[/yellow]")
elif limit < 0:
    console.print("[red]0 이상의 정수를 입력하세요.[/red]")
    messagebox.showerror("소수 찾기", "0 이상의 정수를 입력하세요.")
else:
    primes = get_primes(limit)
    result = f"{limit} 이하의 소수: {primes}"
    console.print(
        Panel(result, title="계산 결과", border_style="bright_cyan")
    )
    messagebox.showinfo("소수 찾기", result)

root.destroy()