# 导入webbrowser和tkinter模块
import webbrowser as w
import tkinter as tk

# 定义一个函数，用于打开pdf文件
def open_pdf():
    # 获取用户输入的网址
    url = entry.get()

    # 从网址中提取md5值
    md5 = url.split('&')[1].split('=')[1]

    # 拼接pdf文件的链接
    pdf_url = f'https://r2-ndr.ykt.cbern.com.cn/edu_product/esp/assets_document/{md5}.pkg/pdf.pdf'

    # 用浏览器打开pdf文件
    w.open(pdf_url)

# 定义一个函数，用于清空输入框
def clear_entry():
    # 删除输入框中的所有内容
    entry.delete(0, tk.END)

# 定义一个函数，用于打开教材网址
def open_material():
    # 定义教材网址的链接
    material_url = 'https://basic.smartedu.cn/tchMaterial'

    # 用浏览器打开教材网址
    w.open(material_url)

# 定义一个函数，用于打开作者的GitHub主页
def open_author():
    # 定义作者的GitHub主页的链接
    author_url = 'https://github.com/Mystic-stars'

    # 用浏览器打开作者的GitHub主页
    w.open(author_url)

window = tk.Tk()

# 设置窗口的标题和大小
window.title('智慧中小学教材解析工具')
window.geometry('300x200')

# 创建一个标签对象，显示提示信息
label = tk.Label(window, text='请输入教材网址')
label.pack(pady=10)

# 创建一个输入框对象，接收用户输入的网址
entry = tk.Entry(window)
entry.pack()

# 创建一个按钮对象，绑定open_pdf函数
button1 = tk.Button(window, text='解析PDF文件', command=open_pdf)
button1.pack(pady=10)

# 创建一个框架对象，放置其他三个按钮
frame = tk.Frame(window)
frame.pack(pady=10)

# 创建一个按钮对象，绑定clear_entry函数，放在框架左边
button2 = tk.Button(frame, text='清空PDF链接', command=clear_entry)
button2.pack(side=tk.LEFT, padx=10)

# 创建一个按钮对象，绑定open_author函数，居中放在框架中间
button3 = tk.Button(frame, text='联系作者', command=open_author)
button3.pack(side=tk.LEFT, padx=10)

# 创建一个按钮对象，绑定open_material函数，放在框架右边
button4 = tk.Button(frame, text='教材搜寻网址', command=open_material)
button4.pack(side=tk.LEFT, padx=10)

# 创建一个标签对象，显示制作信息
label = tk.Label(window, text='作者：Mystic_Stars  非盈利软件，仅供学习交流使用')
label.pack(pady=10)

window.mainloop()
