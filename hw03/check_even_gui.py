"""
Codex 활용 코드
prompt: 
[check_even_gui.py](hw03/check_even_gui.py) 코드의 입력, 출력을 rich 라이브러리, gui 라이브러리(tkinter) 활용하여 최소 수정으로 꾸며줘.
"""

from tkinter import Tk, messagebox, simpledialog

from rich.console import Console
from rich.panel import Panel


def is_even(number):
    if number % 2 == 0:
        return "짝수"
    else:
        return "홀수"

console = Console()
root = Tk()
root.withdraw()

num = simpledialog.askinteger("짝수 판별기", "숫자를 입력하세요:", parent=root)

if num is None:
    console.print("[yellow]입력이 취소되었습니다.[/yellow]")
else:
    result = f"{num}은(는) {is_even(num)}입니다."
    console.print(
        Panel(result, title="확인 결과", border_style="bright_blue")
    )
    messagebox.showinfo("짝수 판별기", result)

root.destroy()
