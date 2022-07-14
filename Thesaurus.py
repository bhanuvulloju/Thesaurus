from tkinter.ttk import *
from tkinter import * 
from tkinter import messagebox
from turtle import width
import requests
from bs4 import BeautifulSoup



root = Tk()
root.title("UrsDictionary")
root.config(bg="#E5E7E9")
root.geometry("940x520")

title = Frame(root)
title.pack(side='top')
mytit = Label(title, text ="📖Thesaurus",font = ("broadway", 25, "bold")) 
mysubtit = Label(title, text ="- Know it ...🔍",font = ("arial", 15)) 
mytit.pack(ipadx=9,ipady=2,pady=10)
mysubtit.pack(ipadx=5,side='right')

searchword = StringVar()
searchtxt = Label(root, text ="Enter your word : ",font = ("arial", 10)).place(x=240,y=130)
myword = Entry(root,font = ("arial", 12,"bold"),textvariable=searchword)


myword.pack(padx=10,pady=30,ipady=10,ipadx=5)

# Get information about the word
def getinfo():
    my_search = searchword.get()
    res = 'https://api.dictionaryapi.dev/api/v2/entries/en/'
    res = res + my_search
    getting_req = requests.get(res)
    
    try:
        txt = getting_req.json()
        if(txt["title"]=="No Definitions Found"):
            messagebox.showwarning("ERROR❌", "cHECk tHe sPeLling")
    except:
        pass
    else:
        # print("success")
        return

    meaning = getting_req.json()[0]["meanings"][0]["definitions"][0]["definition"]
   
    pos = getting_req.json()[0]["meanings"][0]["partOfSpeech"]
    syn = getting_req.json()[0]["meanings"][0]["synonyms"]
    anto = getting_req.json()[0]["meanings"][0]["antonyms"]
    # print(anto)

    synlis=""
    cs=0
    for ele in syn:
        cs=cs+1
        synlis = synlis + ele + "\n"
        if(cs>4):
            break
    
    antolis=""
    ca=0
    for ele in anto:
        ca = ca + 1
        antolis = antolis + ele + "\n"
        if(ca>4):
            break

    meanT = Label(root, height = 2, width = 120,bg="light cyan",text=meaning).place(x=120,y=180)
    posT = Label(root, height = 1, width = 10,bg="light cyan",pady=10,text=pos).place(x=160,y=220)
    stnT = Label(root, height = 4, width = 15,bg="light cyan",pady=20,padx=10,text=synlis).place(x=140,y=280)
    antoT = Label(root, height = 4, width = 15,bg="light cyan",pady=20,padx=10,text=antolis).place(x=400,y=280)
    

enterb = Button(root,text="Enter",fg='black',bg='blue',font=('arial',12,'bold'),command=getinfo).place(x=580,y=130)

meantxt = Label(root, text ="Meaning : ",font = ("arial", 10)).place(x=40,y=180)
meanT = Text(root, height = 2, width = 100,bg="light cyan").place(x=120,y=180)

pospeech = Label(root, text ="Parts of speech : ",font = ("arial", 10),pady=10).place(x=40,y=220)
posT = Text(root, height = 1, width = 10,bg="light cyan",pady=10).place(x=160,y=220)

syn = Label(root, text ="Synonyms : ",font = ("arial", 10),pady=10).place(x=40,y=280)
stnT = Text(root, height = 4, width = 15,bg="light cyan",pady=20,padx=10).place(x=140,y=280)

Anto = Label(root, text ="Antonyms : ",font = ("arial", 10),pady=10).place(x=300,y=280)
antoT = Text(root, height = 4, width = 15,bg="light cyan",pady=20,padx=10).place(x=400,y=280)


# Get meaning in different languages...
def lang():
    myword = searchword.get()
    site = 'https://www.indifferentlanguages.com/words/'
    my_site = site + myword
    my_site = requests.get(my_site).text

    soup = BeautifulSoup(my_site, 'lxml')

    tel = soup.find('a', {'lang': 'te'}).text.strip()
    tel = Label(root, text =tel,font = ("arial", 10),pady=3,fg="#CAEA15").place(x=700,y=280)


    hin = soup.find('a', {'lang': 'hi'}).text.strip()
    hin = Label(root, text =hin,font = ("arial", 10),pady=3,fg="#1569EA").place(x=700,y=310)

    fr = soup.find('a', {'lang': 'fr'}).text.strip()
    fr = Label(root, text =fr,font = ("arial", 10),pady=3,fg="#8015EA").place(x=700,y=340)

    germ = soup.find('a', {'lang': 'de'}).text.strip()
    germ = Label(root, text =germ,font = ("arial", 10),pady=3,fg="#39EA15").place(x=700,y=370)




indiff_lang = Button(root,text="In Differnt Languages",command=lang,bd=5).place(x=620,y=240)

tel = Label(root, text ="Telugu : ",font = ("arial", 10),pady=3).place(x=640,y=280)
hin = Label(root, text ="Hindi : ",font = ("arial", 10),pady=3).place(x=640,y=310)
fr = Label(root, text ="French : ",font = ("arial", 10),pady=3).place(x=640,y=340)
ge = Label(root, text ="German : ",font = ("arial", 10),pady=3).place(x=640,y=370)

bend = Button(root,text="Close",font = ("arial", 14),bg="red",fg="white",command=root.destroy)
bend.pack(side='bottom')


root.mainloop()   