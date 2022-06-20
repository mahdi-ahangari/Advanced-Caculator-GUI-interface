from math import sqrt
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
        self.track_nums = ""
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
            ("C", "C"):(0, 0),("²", "**2"):(0, 1),("√", "sqrt("):(0, 2),
            ("×", "*"):(0, 3),("÷", "/"):(1, 3),("+", "+"):(2, 3),
            ("-", "-"):(3, 3),("=", "="):(4, 3),
        }
        self.special_buttons = self.creat_special_buttons()

        for i in range(4):
            self.bFrame.rowconfigure(i, weight=1)
            self.bFrame.columnconfigure(i, weight=1)
        
        self.operators = ["*", "/", "+", "-"]
        self.already_have_Operator = False    # operator spam nkne  
        self.pow_on = False     # bad as pow² dige adad nzne ke **2 adad bere jolosh dige pow 2 nmishe
        self.should_closeP = False  # i use sqrt() for root so i insert sqrt( first after numbers done i close it ')'

# --------------------/ Frames / --------------------
    def Creat_output_frame(self):
        oFrame = Frame(self.root, bg= "#2b2c33", height=200)
        oFrame.pack(expand= True, fill=BOTH)
        return oFrame


    def Creat_button_frame(self):
        bFrame = Frame(self.root, bg= "#2b2c33", height=400)
        bFrame.pack(expand= True,fill=BOTH)
        return bFrame


    def creat_output(self):
        self.track_nums_label = Label(self.oFrame, text=self.track_nums, font=small_font, bg= "gray", fg="white", padx=8, pady=20, anchor=E)
        self.track_nums_label.pack(expand= True,fill=BOTH)

        self.current_num_label = Label(self.oFrame, text=self.current_num, font=big_font, bg= "gray", fg="white", padx=10, anchor=E)
        self.current_num_label.pack(expand= True,fill=BOTH)

        return self.track_nums_label, self.current_num_label

# --------------------/ Frames / --------------------

# --------------------/ Buttons / --------------------
    def clear_track_nums(self):
        self.current_num = ""
        self.track_nums = ""
        self.track_nums_label.config(text="")


    def clear_current_nums(self):
        self.current_num = ""
        self.current_num_label.config(text="")


    def update_current_num(self, value):
        self.update_track_nums()
        if len(self.current_num) < 11 and not self.pow_on:
            self.already_have_Operator = False
            self.current_num += str(value)
            self.current_num_label.config(text=self.current_num)


    def update_track_nums(self):
        replace_method = self.track_nums           # back end avaz nashe chon avz miknim chizi ke be karbar nshon dade mishe 
        for operator, _ in self.specialKey_list.items():
            replace_method = replace_method.replace(operator[1], operator[0]) # jay sheklay pythoni ba riazi ii avz mikne Then update
            replace_method = replace_method.replace(")", "")
        self.track_nums_label.config(text=replace_method)

        # ----------------/Operations and update result / ---------------

    def caculate(self):
        try : #  inja baraye ineke alaki num va = nzne , gand bzne be caculator pro am
            is_only_number = self.track_nums + self.current_num
            if is_only_number == "":
                return 0
            int(is_only_number)
        except Exception as _:   # agar error bede yani operator dare va pass mishe vagarna tabe ejra nmishe
            pass
        else :
            return 0
        # stage 1 => add current num to over all and update it then clear current num
        self.track_nums += self.current_num   
        if self.should_closeP:    # agar root gerefte bashe sqrt( bayad baste beshe then update va edame
            self.track_nums +=")"   
            self.should_closeP = False  
        self.clear_current_nums()
        self.update_track_nums()      

        #stage 2 => caculate and update current num
        try :
            self.current_num = str(eval(self.track_nums))[:11]       
            self.current_num_label.config(text=self.current_num)
        except ZeroDivisionError :
            self.current_num_label.config(text="zero division:(")
            self.current_num = ""
            self.track_nums = ""       
        except Exception as e:
            self.current_num_label.config(text="Error !!!")   
            self.current_num = ""
            self.track_nums = ""     

        self.track_nums = self.current_num       # --> this is for next operation after pressing = 
        self.current_num = ""


    def operate(self, value):
        try : 
            if value in self.operators and not self.already_have_Operator:
                self.already_have_Operator = True
                self.track_nums += self.current_num
                if self.should_closeP:
                    self.track_nums +=") "
                    self.should_closeP = False
                self.track_nums += value           
                self.clear_current_nums()
                self.update_track_nums()
                self.pow_on = False

            elif value in self.operators and self.already_have_Operator:  # nmizare spam kone operator haro update mikneshon
                self.track_nums = self.track_nums[:-1] + value # pop last operator and put new one
                self.update_track_nums()

        except Exception as E :
            self.current_num_label.config(text="Error")

        #operates final result
        if value == "=":
            self.caculate()
            self.should_closeP = False
            self.pow_on = False

        if value == "C":
            self.already_have_Operator = False
            self.clear_current_nums()
            self.clear_track_nums()
            self.pow_on = False

        if value == "**2":
            if self.current_num != "" or self.track_nums != "":  # nmizare alaki khali tavan bzne
                self.track_nums += self.current_num + value
                self.clear_current_nums()
                self.track_nums_label.config(text=self.track_nums)
                self.update_track_nums()
                self.pow_on = True

        if value == "sqrt(":
            self.pow_on = False
            if self.track_nums != "" and not self.already_have_Operator\
                 or self.current_num != "":  # gabl radikal 1 zarb mizare default masalam 10 radikal 6 yani zrb
                self.track_nums += self.current_num
                self.track_nums += "*"
            self.should_closeP = True
            self.track_nums += value
            self.clear_current_nums()
            self.update_track_nums()

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
            if key[0] == "=" :
                button.config(activeforeground="lightgray", fg="gold")
            if key[0] == "²" :
                button.config(text="x²")
            if key[0] == "√" :
                button.config(text="√x")

# --------------------/ Buttons / --------------------
    def Run(self):
        self.root.mainloop()


if __name__ == "__main__":
    a = Caculator()
    a.Run()
