"""
Codex 활용 코드
prompt:
[is_prime_gui.py](hw03/is_prime_gui.py) 코드의 입력, 출력을 rich 라이브러리, gui 라이브러리(tkinter) 활용하여 최소 수정으로 꾸며줘.
"""

from tkinter import Tk, messagebox, simpledialog

from rich.console import Console
from rich.panel import Panel


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

console = Console()
root = Tk()
root.withdraw()

number = simpledialog.askinteger("소수 판별기", "숫자를 입력하세요:", parent=root)

if number is None:
    console.print("[yellow]입력이 취소되었습니다.[/yellow]")
else:
    if is_prime(number):
        result = f"{number}은(는) 소수입니다."
    else:
        result = f"{number}은(는) 소수가 아닙니다."

    console.print(
        Panel(result, title="판별 결과", border_style="bright_yellow")
    )
    messagebox.showinfo("소수 판별기", result)

root.destroy()
