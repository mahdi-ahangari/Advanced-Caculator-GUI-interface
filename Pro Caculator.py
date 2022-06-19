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
        self.root.title("Caculator Pro")
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

        self.specialKey_list = {             # alt 0178 = ² /  alt 251 = √ / alt 0247 = ÷ / alt 0215 × 
            ("C", "C"):(0, 0),("x²", "**"):(0, 1),("√x", "**0.5"):(0, 2),
            ("×", "*"):(0, 3),("÷", "/"):(1, 3),("+", "+"):(2, 3),
            ("-", "-"):(3, 3),("=", "="):(4, 3),
        }
        self.special_buttons = self.creat_special_buttons()

        for i in range(4):
            self.bFrame.rowconfigure(i, weight=1)
            self.bFrame.columnconfigure(i, weight=1)
        
        self.operators = ["*", "/", "+", "-"]

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

        self.current_num_label = Label(self.oFrame, text=self.current_num, font=big_font, bg= "gray", fg="white", padx=10, anchor=E)
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
        if len(self.current_num) < 11 :
            self.already_have_Operator = False
            self.current_num += str(value)
            self.current_num_label.config(text=self.current_num)
        

    def update_all_nums(self):
        replace_method = self.all_nums           # back end avaz nashe chon avz miknim chizi ke be karbar nshon dade mishe 
        for operator, _ in self.specialKey_list.items():
            replace_method = replace_method.replace(operator[1], operator[0]) # jay sheklay pythoni ba riazi ii avz mikne Then update
        self.all_nums_label.config(text=replace_method)


        # ----------------/Operations and update result / ---------------

    def caculate(self):
        # stage 1 => add current num to over all and update it then clear current num
        self.all_nums += self.current_num        
        self.clear_current_nums()
        self.update_all_nums()      

        #stage 2 => caculate and update current num
        try :
            self.current_num = str(eval(self.all_nums))[:11]         
            self.current_num_label.config(text=self.current_num)
        except ZeroDivisionError :
            self.current_num_label.config(text="zero division:(")
            self.current_num = ""
            self.all_nums = ""       
        except Exception as e:
            self.current_num_label.config(text="Error !!!")   
            self.current_num = ""
            self.all_nums = ""     

        self.all_nums = self.current_num       # --> this is for next operation after pressing = 
        self.current_num = ""
                
    def operate(self, value):
        try :
            if value in self.operators and not self.already_have_Operator:
                self.already_have_Operator = True
                self.all_nums += self.current_num       
                self.all_nums += value           
                self.clear_current_nums()
                self.update_all_nums()

            elif value in self.operators and self.already_have_Operator:  # nmizare spam kone operator haro update mikneshon
                self.all_nums = self.all_nums[:-1] + value # pop last operator and put new one
                self.update_all_nums()
        except Exception as E :
            self.current_num_label.config(text="put a number")

        #operates final result
        if value == "=":
            self.caculate()
        if value == "C":
            self.clear_current_nums()
            self.clear_all_nums()

        if value == "**":
            try :
                self.caculate()           
                self.all_nums_label.config(text=f"{self.all_nums}²")
                self.current_num = str(pow(float(self.all_nums), 2))[:11]
                self.current_num_label.config(text=self.current_num)
                self.all_nums = self.current_num
                self.current_num = ""
            except Exception as e:
                self.current_num_label.config(text="put a number")

        if value == "**0.5":
            try :
                self.caculate()           
                self.all_nums_label.config(text=f"√{self.all_nums}")
                self.current_num = str(pow(float(self.all_nums), 0.5))[:11]
                self.current_num_label.config(text=self.current_num)
                self.all_nums = self.current_num
                self.current_num = ""
            except Exception as e:
                self.current_num_label.config(text="put a number")


        # ----------------/Operations and update result / ---------------


    def creat_num_buttons(self):
        for num, grid in self.numbers_list.items():
            button = Button(self.bFrame, text=str(num))
            button.config(activeforeground="gold", activebackground="#2b2c29",
             bg="#2b2c29", fg="white", borderwidth=0, font=("arial", 26), command=lambda x = num: self.update_current_num(x))
            button.grid(row=grid[0], column=grid[1], sticky=NSEW)


    def creat_special_buttons(self):
        for key, grid in self.specialKey_list.items():   # back end symbol hay python use mide front shekl dige nshon mide
            button = Button(self.bFrame, text=str(key[0]))
            button.config(activeforeground="gold", activebackground="#2b2c30",
             bg="#2b2c30", fg="white", borderwidth=0, font=("arial", 26), command=lambda x = key[1]: self.operate(x))

            button.grid(row=grid[0], column=grid[1], sticky=NSEW)
            if key == "=" :
                button.config(activeforeground="lightgray", fg="gold")


# --------------------/ Buttons / --------------------

    def Run(self):
        self.root.mainloop()


if __name__ == "__main__":
    a = Caculator()
    a.Run()
