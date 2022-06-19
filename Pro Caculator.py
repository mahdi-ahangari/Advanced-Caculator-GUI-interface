from tkinter import *


small_font = ("arial", 20)
big_font = ("arial", 46)


class Caculator:
    def __init__(self):
        # --------------------/ Main window / --------------------
        self.root = Tk()
        self.root.geometry("400x600+500+100")
        self.root.resizable(0, 0)
        self.root.iconbitmap(bitmap="gray75")
        self.root.title("Caculator Mahdi Edition")
        self.root.attributes("-alpha", 0.98)
        # --------------------/ Main window / --------------------
        self.all_nums = ""
        self.current_num = ""
        self.oFrame = self.Creat_output_frame()
        self.bFrame = self.Creat_button_frame()
        self.output = self.creat_output()

        self.numbers_list = {   # button text and grid system in ()
            1:(3, 0),2:(3, 1),3:(3, 2),
            4:(2, 0),5:(2, 1),6:(2, 2),
            7:(1, 0),8:(1, 1),9:(1, 2),
            0:(4, 0),"00":(4, 1),".":(4, 2)
        }
        self.num_buttons = self.creat_num_buttons()

        self.specialKey_list = {             # alt 0178 = ² /  alt 251 = √ / alt 0247 = ÷ / 
            "C":(0, 0),"x²":(0, 1),"√x":(0, 2),
            "x":(0, 3),"÷":(1, 3),"+":(2, 3),
            "-":(3, 3),"=":(4, 3),
        }
        self.special_buttons = self.creat_special_buttons()

        for i in range(4):
            self.bFrame.rowconfigure(i, weight=1)
            self.bFrame.columnconfigure(i, weight=1)
        

# --------------------/ Frames / --------------------
    def Creat_output_frame(self):
        oFrame = Frame(self.root, bg= "#2b2c33", height=200)
        oFrame.pack(expand= True,fill=BOTH)
        return oFrame
 

    def Creat_button_frame(self):
        bFrame = Frame(self.root, bg= "#2b2c33", height=400)
        bFrame.pack(expand= True,fill=BOTH)
        return bFrame


    def creat_output(self):
        self.all_nums_label = Label(self.oFrame, text=self.all_nums, font=small_font, bg= "gray", fg="white", padx=8, pady=20, anchor=E)
        self.all_nums_label.pack(expand= True,fill=BOTH)

        self.current_num_label = Label(self.oFrame, text=self.current_num, font=big_font, bg= "gray", fg="white", padx=10, anchor=E) # #2b2c33
        self.current_num_label.pack(expand= True,fill=BOTH)

        return self.all_nums_label, self.current_num_label

# --------------------/ Frames / --------------------

# --------------------/ Buttons / --------------------
    def clear_all_nums(self):
        self.current_num = ""
        self.all_nums = ""
        self.all_nums_label.config(text="")


    def clear_current_nums(self):
        self.current_num = ""
        self.current_num_label.config(text="")


    def update_current_num(self, value):
        self.current_num += str(value)
        self.current_num_label.config(text=self.current_num)



    def update_all_nums(self, value):
        if value in ['x', '÷', '+', '-']:
            self.all_nums += self.current_num
            self.all_nums += str(value)
            self.clear_current_nums()
            self.all_nums_label.config(text=self.all_nums)



    def creat_num_buttons(self):
        for num, grid in self.numbers_list.items():
            button = Button(self.bFrame, text=str(num))
            button.config(activeforeground="orange", activebackground="#2b2c29",
             bg="#2b2c29", fg="white", borderwidth=0, font=("arial", 26), command=lambda x = num: self.update_current_num(x))
            button.grid(row=grid[0], column=grid[1], sticky=NSEW)


    def creat_special_buttons(self):
        for key, grid in self.specialKey_list.items():
            button = Button(self.bFrame, text=str(key))
            button.config(activeforeground="gold", activebackground="#2b2c30",
             bg="#2b2c30", fg="white", borderwidth=0, font=("arial", 26), command=lambda x = key: self.update_all_nums(x))

            button.grid(row=grid[0], column=grid[1], sticky=NSEW)
            if key == "=" :
                button.config(activeforeground="lightgray", fg="gold")


# --------------------/ Buttons / --------------------










    def Run(self):
        self.root.mainloop()


if __name__ == "__main__":
    a = Caculator()
    a.Run()
