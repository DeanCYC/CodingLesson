import time
import tkinter
import tkinter.messagebox
from threading import Thread


def main():

    class DownloadTaskHandler(Thread):

        def run(self):
            time.sleep(10)
            tkinter.messagebox.showinfo('提示', '下載完成!')
            # 啟用下載按鈕
            button1.config(state=tkinter.NORMAL)

    def download():
        # 禁用下載按鈕
        button1.config(state=tkinter.DISABLED)
        # 通過daemon參數將執行緒設置為守護執行緒(主程序退出就不再保留執行)
        # 在執行緒中處理耗時間的下載任務
        DownloadTaskHandler(daemon=True).start()

    def show_about():
        tkinter.messagebox.showinfo('關於', '作者: 陳叮(v1.0)')

    top = tkinter.Tk()
    top.title('單執行緒')
    top.geometry('200x150')
    top.wm_attributes('-topmost', 1)

    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='下載', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='關於', command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()


if __name__ == '__main__':
    main()