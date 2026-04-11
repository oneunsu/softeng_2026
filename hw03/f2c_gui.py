"""
Codex 활용 코드
prompt:
[f2c_gui.py](hw03/f2c_gui.py) 코드의 입력, 출력을 rich 라이브러리, gui 라이브러리(tkinter) 활용하여 최소 수정으로 꾸며줘.
"""

from tkinter import Tk, messagebox, simpledialog

from rich.console import Console
from rich.panel import Panel


def f2c(temp_f):
    return (temp_f - 32) * 5.0/9.0

console = Console()
root = Tk()
root.withdraw()

temp_f = simpledialog.askfloat("온도 변환기", "화씨 온도를 입력하세요:", parent=root)

if temp_f is None:
    console.print("[yellow]입력이 취소되었습니다.[/yellow]")
else:
    temp_c = f2c(temp_f)
    result = f"화씨 {temp_f}도는 섭씨 {temp_c:.2f}도입니다."
    console.print(
        Panel(result, title="변환 결과", border_style="bright_red")
    )
    messagebox.showinfo("온도 변환기", result)

root.destroy()
