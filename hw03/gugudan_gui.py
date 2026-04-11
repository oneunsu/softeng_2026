"""
Codex 활용 코드
prompt:
[gugudan_gui.py](hw03/gugudan_gui.py) 코드의 입력, 출력을 rich 라이브러리, gui 라이브러리(tkinter) 활용하여 최소 수정으로 꾸며줘.
"""

from tkinter import Tk, messagebox, simpledialog

from rich.console import Console
from rich.panel import Panel


console = Console()
root = Tk()
root.withdraw()

dan = simpledialog.askinteger("구구단 출력기", "몇 단을 출력할까요?", parent=root)

if dan is None:
    console.print("[yellow]입력이 취소되었습니다.[/yellow]")
else:
    lines = []
    for i in range(1, 10):
        lines.append(f"{dan} x {i} = {dan * i}")

    result = "\n".join(lines)
    console.print(
        Panel(result, title=f"{dan}단", border_style="bright_magenta")
    )
    messagebox.showinfo("구구단 출력기", result)

root.destroy()
