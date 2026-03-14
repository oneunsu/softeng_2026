"""
Codex 활용 코드
prompt:
[sum_even_gui.py](hw03/sum_even_gui.py) 코드의 입력, 출력을 rich 라이브러리, gui 라이브러리(tkinter) 활용하여 최소 수정으로 꾸며줘.
"""

from tkinter import Tk, messagebox, simpledialog

from rich.console import Console
from rich.panel import Panel


console = Console()
root = Tk()
root.withdraw()

n = simpledialog.askinteger(
    "짝수 합 계산기",
    "1부터 n까지의 숫자 중 짝수의 합을 구할 n을 입력하세요:",
    parent=root,
)

if n is None:
    console.print("[yellow]입력이 취소되었습니다.[/yellow]")
elif n < 1:
    console.print("[red]1 이상의 정수를 입력하세요.[/red]")
    messagebox.showerror("짝수 합 계산기", "1 이상의 정수를 입력하세요.")
else:
    nums = [x for x in range(1, n + 1) if x % 2 == 0]
    result = f"1부터 {n}까지 짝수의 합은 {sum(nums)}입니다."
    console.print(
        Panel(result, title="계산 결과", border_style="bright_blue")
    )
    messagebox.showinfo("짝수 합 계산기", result)

root.destroy()
