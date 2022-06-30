'''
基本上使用tkinter來開發GUI應用需要以下5個步驟：

1.導入tkinter模塊中我們需要的東西。
2.創建一個頂層視窗對象並用它來承載整個GUI應用。
3.在頂層視窗對像上添加GUI組件。
4.通過代碼將這些GUI組件的功能組織起來。
5.進入主事件循環(main loop)。

'''


#GUI應用
import tkinter
import tkinter.messagebox


def main():
    flag = True

    # 修改標籤上的文字
    def change_label_text():
        nonlocal flag
        flag = not flag
        color, msg = ('red', 'Hello, world!')\
            if flag else ('blue', 'Goodbye, world!')
        label.config(text=msg, fg=color)

    # 確認退出
    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('溫馨提示', '確定要退出嗎?'):
            top.quit()

    # 創建頂層視窗
    top = tkinter.Tk()
    # 設置視窗大小
    top.geometry('240x160')
    # 設置視窗標題
    top.title('小遊戲')
    # 創建標籤對象並添加到頂層視窗
    label = tkinter.Label(top, text='Hello, world!', font='Arial -32', fg='red')
    label.pack(expand=1)
    # 創建一個裝按鈕的容器
    panel = tkinter.Frame(top)
    # 創建按鈕對象 指定添加到哪個容器中 通過command參數綁定事件回調函數
    button1 = tkinter.Button(panel, text='修改', command=change_label_text)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='退出', command=confirm_to_quit)
    button2.pack(side='right')
    panel.pack(side='bottom')
    # 開啟主事件循環
    tkinter.mainloop()


if __name__ == '__main__':
    main()