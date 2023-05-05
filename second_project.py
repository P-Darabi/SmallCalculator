import tkinter as tk
from tkinter import E, W, N, S, ttk


list_of_safe_char=["1","2","3","4","5","6","7","8","9","+","-","*",".","0","="]

def show_calculator():
    win=tk.Tk()
    win.title(" Calculator ")
    lbl_screen=tk.Label(
        master=win,
        text="0",
        
    )
    lbl_screen.grid(row=0,column=0,columnspan=4,padx=7,pady=7,sticky="ew")

    def insert_number_on_label(btn_text):
        flag=False
        if lbl_screen["text"]=="0":
            lbl_screen["text"]=btn_text
        
        elif btn_text== "C":
            lbl_screen["text"]=lbl_screen["text"][:-1]

    
        elif btn_text=="=":
            if lbl_screen["text"][-1] not in ["-","+","*","."]:
                try:
                    if any(item in lbl_screen["text"] for item in list_of_safe_char):
                        lbl_screen["text"]=str(eval(lbl_screen["text"]))
                except Exception:
                    print (" Your application faced a illegal accessibility!!")  
                    return         

        elif btn_text in ["-","+","*"]:
            if lbl_screen["text"][-1] in ["-","+","*"]:
                    lbl_screen["text"]=lbl_screen["text"][:-1]+btn_text
            else:
                lbl_screen["text"]+=btn_text

        elif btn_text==".":
            for i in lbl_screen["text"]:   
               if i==".":
                   flag=True
               if i in ["-","+","*"]:
                   flag=False
            if flag==False:
                lbl_screen["text"]+=btn_text
            
        else:
            lbl_screen["text"]+=btn_text 
    
    calc_keys=[
        {"text" : "1",
        "command" : lambda: insert_number_on_label("1")}, 
        {"text" : "2",
        "command" : lambda: insert_number_on_label("2")},
        {"text" : "3",
        "command" : lambda: insert_number_on_label("3")},
        {"text" : "-",
        "command" : lambda: insert_number_on_label("-")},
        {"text" : "4",
        "command" : lambda: insert_number_on_label("4")},
        {"text" : "5",
        "command" : lambda: insert_number_on_label("5")},
        {"text" : "6",
        "command" : lambda: insert_number_on_label("6")},
        {"text" : "+",
        "command" : lambda: insert_number_on_label("+")},
        {"text" : "7",
        "command" : lambda: insert_number_on_label("7")},
        {"text" : "8",
        "command" : lambda: insert_number_on_label("8")},
        {"text" : "9",
        "command" : lambda: insert_number_on_label("9")},
        {"text" : "*",
        "command" : lambda: insert_number_on_label("*")},
        {"text" : ".",
        "command" : lambda: insert_number_on_label(".")},
        {"text" : "0",
        "command" : lambda: insert_number_on_label("0")},
        {"text" : "C",
        "command" : lambda: insert_number_on_label("C")},
        {"text" : "=",
        "command" : lambda: insert_number_on_label("=")},
    ]
    list_of_btn=[]

    for key_of_calc in calc_keys:
        btn=ttk.Button(
            master=win,
            text=key_of_calc["text"],
            width=5,
            command=key_of_calc["command"],
        )
        list_of_btn.append(btn)

    for index,name_btn in enumerate(list_of_btn):
        name_btn.grid(
            row=(index // 4) + 1,
            column=index % 4,
            sticky="ew",
            )
 
    win.mainloop()

show_calculator()


