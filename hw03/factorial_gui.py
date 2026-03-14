"""
Codex 활용 코드
음수, 0 예외 처리 추가
prompt:
[factorial_gui.py](hw03/factorial_gui.py) 코드의 입력, 출력을 rich 라이브러리, gui 라이브러리(tkinter) 활용하여 최소 수정으로 꾸며줘.
"""

from tkinter import Tk, messagebox, simpledialog

from rich.console import Console
from rich.panel import Panel


def fact(n):
        if n <= 1:
            return 1
        return n * fact(n - 1)

console = Console()
root = Tk()
root.withdraw()

num = simpledialog.askinteger("팩토리얼 계산기", "숫자를 입력하세요:", parent=root)

if num is None:
    console.print("[yellow]입력이 취소되었습니다.[/yellow]")
elif num < 0:
    console.print("[red]0 이상의 정수를 입력하세요.[/red]")
    messagebox.showerror("팩토리얼 계산기", "0 이상의 정수를 입력하세요.")
else:
    result = f"{num}! = {fact(num)}"
    console.print(
        Panel(result, title="계산 결과", border_style="bright_green")
    )
    messagebox.showinfo("팩토리얼 계산기", result)

root.destroy()
