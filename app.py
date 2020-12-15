import tkinter as tk
from tkinter import filedialog
from nltk.tokenize import sent_tokenize,word_tokenize
from heapq import nlargest
from collections import defaultdict
from nltk.probability import FreqDist


root = tk.Tk()
root.geometry("815x488")
root.configure(background='#DCDCDC')
root.title('test')


# first text wiget
input_text=tk.Text(root, height=10,width=100,bd=5)
input_text.grid(row = 1, column = 0,  pady = 2, columnspan=3)

text=input_text.get("1.0","end")
stopwords = []
file = open('stopwords.txt', encoding = 'utf-8').read()
[stopwords.append(x) for x in file.split()]
_stopwords = set(stopwords)

#n=input
def summraizer():
    
    output_text.delete("1.0","end")
    re=input_text.get("1.0","end")
    sents = sent_tokenize(re)
    num=round(len(sents))
    n=round(num/2)
    word_sent=word_tokenize(re)
    word_sent=[word for word in word_sent if word not in _stopwords]
    freq = FreqDist(word_sent)
    ranking = defaultdict(int)
    for i,sent in enumerate(sents):
        for w in word_tokenize(sent):
            if w in freq:
                ranking[i] += freq[w]
        ranking[i] /= len(word_tokenize(sent))
    
    sents_idx = nlargest(n, ranking, key=ranking.get) 
    al=[sents[j] for j in sorted(sents_idx)]
    res=' '
    for sent in al:
        res+=''.join(sent)
    output_text.insert(tk.END,res)

def getText():
    output_text.delete("1.0","end")
    result=input_text.get("1.0","end")
    output_text.insert(tk.END,result)

    return result
    
def textClear():
    output_text.delete("1.0","end")
    input_text.delete("1.0","end")

def fileDialog():
 
    filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype =
    (("text files","*.txt"),("all files","*.*")) )
    print(filename)

    with open(filename,'r',encoding='utf-8') as f:
        text=f.read()
        input_text.insert(tk.END,text)
    f.close()
    




#our lables
in_lable = tk.Label(root,relief='groove', text="لطفا متن خود را وارد نمایید")
in_lable.grid(row = 0, column = 1,  pady = 2)



#BTNs
btnRead=tk.Button(root, height=1, width=20, text="ثبت",relief='flat',overrelief='groove',
                    command=summraizer)
btnRead.grid(row = 2, column = 0, pady = 2)

btnClear=tk.Button(root, height=1, width=20, text="پاک کردن",relief='flat',overrelief='groove',
                    command=textClear)
btnClear.grid(row = 2, column = 1, pady = 2)


btnFind =tk.Button(root, height=1, width=20,text = "پیدا کردن فایل",relief='flat',overrelief='groove',
                    command =fileDialog)
btnFind.grid(row = 2, column = 2, pady = 2)



#last lable
out_lable = tk.Label(root,relief='groove', text="نتیجه شما در کادر زیر خواهد بود ")
out_lable.grid(row = 5, column = 1,  pady = 2)



#out text
output_text=tk.Text(root, height=10,width=100,bd=5)
output_text.grid(row = 6, column = 0,  pady = 2, columnspan=3)



#copywrite
copywrite_lable = tk.Label(root,relief='sunken', text="2020")
copywrite_lable.grid(row = 8, column = 0,  pady = 2)


root.mainloop()
