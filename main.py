import tkinter as tk
from tkinter import scrolledtext, ttk

# ==============================================
# 说明：
# 1. 本项目为演示版本，展示AI编程工具功能
# 2. 如需真实AI能力，可接入通义千问/豆包等API
# 3. 请勿上传真实API Key到GitHub
# ==============================================
API_KEY = "请在此处填写你的通义千问API Key"

# 演示模式（不联网、不依赖环境）
def demo_ai_response(prompt):
    return (
        "【演示模式：AI 生成结果】\n"
        "def example():\n"
        "    print('这是演示生成的代码')\n\n"
        "实际使用时可接入大模型API获取真实结果"
    )

# 功能函数
def generate_code():
    output.delete("1.0", tk.END)
    output.insert(tk.END, "生成中...")
    root.update()
    res = demo_ai_response(input_box.get("1.0", tk.END))
    output.delete("1.0", tk.END)
    output.insert(tk.END, res)

def fix_error():
    output.delete("1.0", tk.END)
    output.insert(tk.END, "【演示：报错修复】\n已自动分析并修复代码错误")

def add_comment():
    output.delete("1.0", tk.END)
    output.insert(tk.END, "【演示：注释生成】\n# 自动生成注释\n原代码")

def format_code():
    output.delete("1.0", tk.END)
    output.insert(tk.END, "【演示：格式化】\n代码已自动格式化")

def gen_doc():
    output.delete("1.0", tk.END)
    output.insert(tk.END, "【演示：文档生成】\n生成函数说明文档")

# 界面
root = tk.Tk()
root.title("AI 编程辅助工具")
root.geometry("800x600")

tk.Label(root, text="输入区域").pack()
input_box = scrolledtext.ScrolledText(root, height=12)
input_box.pack(fill="both", padx=10, pady=5)

frame = ttk.Frame(root)
frame.pack(pady=5)
ttk.Button(frame, text="生成代码", command=generate_code).grid(row=0, column=0, padx=5, pady=5)
ttk.Button(frame, text="修复报错", command=fix_error).grid(row=0, column=1, padx=5, pady=5)
ttk.Button(frame, text="添加注释", command=add_comment).grid(row=0, column=2, padx=5, pady=5)
ttk.Button(frame, text="代码格式化", command=format_code).grid(row=0, column=3, padx=5, pady=5)
ttk.Button(frame, text="生成文档", command=gen_doc).grid(row=0, column=4, padx=5, pady=5)

tk.Label(root, text="输出区域").pack()
output = scrolledtext.ScrolledText(root, height=15)
output.pack(fill="both", padx=10, pady=5)

root.mainloop()