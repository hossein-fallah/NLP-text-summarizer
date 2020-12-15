import tkinter as tk


root = tk.Tk()
root.geometry("810x460")
root.configure(background='#DCDCDC')
root.title('Hossein Fallah')
background_image=tk.PhotoImage('1.jpg')


def sumrizer():
    text=input_text.get("1.0", "end")
    return text

def getText():
    output_text.delete("1.0","end")
    result=input_text.get("1.0","end")
    output_text.insert(tk.END,result)

    return result
    
def textClear():
    output_text.delete("1.0","end")
    input_text.delete("1.0","end")


in_lable = tk.Label(root,relief='groove', text="لطفا متن خود را وارد نمایید")
in_lable.grid(row = 0, column = 0,  pady = 2)

input_text=tk.Text(root, height=10,width=100,bd=5)
input_text.grid(row = 1, column = 0,  pady = 2)


btnRead=tk.Button(root, height=1, width=20, text="ثبت",relief='flat',overrelief='groove',
                    command=getText)
btnRead.grid(row = 2, column = 0,  pady = 2)


btnClear=tk.Button(root, height=1, width=20, text="پاک کردن",relief='flat',overrelief='groove',
                    command=textClear)
btnClear.grid(row = 3, column = 0,  pady = 0)

out_lable = tk.Label(root,relief='groove', text="نتیجه شما در کادر زیر خواهد بود ")
out_lable.grid(row = 4, column = 0,  pady = 2)

output_text=tk.Text(root, height=10,width=100,bd=5)
output_text.grid(row = 5, column = 0,  pady = 2)
output_text.insert(tk.END,getText())


root.mainloop()
