from tkinter import *


small_font = ("arial", 16)
big_font = ("arial", 36)


class Caculator:
    def __init__(self):
        # --------------------/ Main window / --------------------
        self.root = Tk()
        self.root.geometry("400x600+500+100")
        self.root.resizable(0, 0)
        self.root.iconbitmap(bitmap="gray75")
        self.root.title("Caculator Mahdi Edition")
        # self.root.attributes("-alpha", 0.95)
        # --------------------/ Main window / --------------------
        self.all_nums = 0
        self.current_num = 0
        self.oFrame = self.Creat_output_frame()
        self.bFrame = self.Creat_button_frame()
        self.output = self.creat_output()


    def Creat_output_frame(self):
        oFrame = Frame(self.root, bg= "#2b2c33", height=200)
        oFrame.pack(expand= True,fill=BOTH)
        return oFrame
 

    def Creat_button_frame(self):
        bFrame = Frame(self.root, bg= "#2b2c33", height=400)
        bFrame.pack(expand= True,fill=BOTH)
        return bFrame


    def creat_output(self):
        # 2 label bsazim ke az frame oFrame ers bari mikne va put mikne yki bala rast yki paiin rast bozorg tar
        all_nums = Label(self.oFrame, text=self.all_nums, font=small_font, bg= "#2b2c33", fg="white",padx=10, anchor=NE)
        all_nums.pack(expand= True,fill=BOTH)

        current_num = Label(self.oFrame, text=self.current_num, font=big_font, bg= "#2b2c33", fg="white",padx=10, anchor=E)
        current_num.pack(expand= True,fill=BOTH)

        return all_nums, current_num












    def Run(self):
        self.root.mainloop()


if __name__ == "__main__":
    a = Caculator()
    a.Run()
