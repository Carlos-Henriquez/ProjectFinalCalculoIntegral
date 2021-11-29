from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter.font import BOLD
from sympy import*

x=Symbol('x')

class AppIndefinida(Frame):
    def __init__(self, root=  None):
        super().__init__(root,width=650,height=500)
        self.root=root
        self.pack()
        self.createWidget()
        
    def setFuction(self,fuction):
        self.BoxText.focus_get()==self.BoxText
        self.BoxText.insert(END,fuction)
            
    def clearTextInputAll(self):
        if(self.BoxText.focus_get()==self.BoxText):
            self.BoxText.delete(0,END)
        elif(self.BoxText1.focus_get()==self.BoxText1):
            self.BoxText1.delete(0,END)

    def ClerarAll(self):
        self.BoxText.delete(0,END) 
        self.BoxText1.delete(0,END)
        self.BoxText.focus() 

    def clearTextInputOne(self):
        if(self.BoxText.focus_get()==self.BoxText):
            contador=self.BoxText.get()
            contador=len(contador)
            contador-=1
            self.BoxText.delete(contador,END)
        elif(self.BoxText1.focus_get()==self.BoxText1):   
            contador=self.BoxText1.get()
            contador=len(contador)
            contador-=1
            self.BoxText1.delete(contador,END)

    def integrar(self):
        try:
            if(self.BoxText.get()!=""):
                self.BoxText1.delete(0,END)
                print(self.BoxText.get())
                print(integrate(self.BoxText.get()))
                self.BoxText1.insert(END,integrate(self.BoxText.get()))
            else:
                self.BoxText1.delete(0,END)
                MessageBox.showerror("Alerta!", "Asegurese de completar todos los campos \n antes de integrar.") 
        except SympifyError:
            MessageBox.showerror("Alerta!", "Asegurese de escribir su expresión \ncorrectamente y vuelva a intentar.")

    def createWidget(self):
        self.bo7=Button(self,text="*",padx=19,pady=10,command=lambda:self.setFuction("*"))
        self.bo7.place(x=120,y=145)
        self.bo7=Button(self,text="÷",padx=19,pady=10,command=lambda:self.setFuction("/"))
        self.bo7.place(x=180,y=145)
        self.bo7=Button(self,text="+",padx=19,pady=10,command=lambda:self.setFuction("+"))
        self.bo7.place(x=240,y=145)
        self.bo7=Button(self,text="-",padx=19,pady=10,command=lambda:self.setFuction("-"))
        self.bo7.place(x=300,y=145)
        self.bo7=Button(self,text="1",padx=19,pady=10,command=lambda:self.setFuction("1"))
        self.bo7.place(x=120,y=195)
        self.bo7=Button(self,text="2",padx=19,pady=10,command=lambda:self.setFuction("2"))
        self.bo7.place(x=180,y=195)
        self.bo7=Button(self,text="3",padx=19,pady=10,command=lambda:self.setFuction("3"))
        self.bo7.place(x=240,y=195)
        self.bo8=Button(self,text="Log",padx=12,pady=10,command=lambda:self.setFuction("log"))
        self.bo8.place(x=300,y=195)
        self.bo8=Button(self,text="sin",padx=12,pady=10,command=lambda:self.setFuction("sin("))
        self.bo8.place(x=360,y=195)
        self.bo8=Button(self,text="cos",padx=12,pady=10,command=lambda:self.setFuction("cos("))
        self.bo8.place(x=420,y=195)
        self.bo8=Button(self,text="tan",padx=12,pady=10,command=lambda:self.setFuction("tan("))
        self.bo8.place(x=480,y=195)
        self.bo8=Button(self,text="4",padx=19,pady=10,command=lambda:self.setFuction("4"))
        self.bo8.place(x=120,y=245)
        self.bo8=Button(self,text="5",padx=19,pady=10,command=lambda:self.setFuction("5"))
        self.bo8.place(x=180,y=245)
        self.bo8=Button(self,text="6",padx=19,pady=10,command=lambda:self.setFuction("6"))
        self.bo8.place(x=240,y=245)
        self.bo8=Button(self,text="x",padx=17,pady=10,command=lambda:self.setFuction("x"))
        self.bo8.place(x=300,y=245)
        self.bo8=Button(self,text="csc",padx=12,pady=10,command=lambda:self.setFuction("csc("))
        self.bo8.place(x=360,y=245)
        self.bo8=Button(self,text="sec",padx=12,pady=10,command=lambda:self.setFuction("sec("))
        self.bo8.place(x=420,y=245)
        self.bo8=Button(self,text="cot",padx=12,pady=10,command=lambda:self.setFuction("cot("))
        self.bo8.place(x=480,y=245)
        self.bo7=Button(self,text="7",padx=19,pady=10,command=lambda:self.setFuction("7"))
        self.bo7.place(x=120,y=295)
        self.bo7=Button(self,text="8",padx=19,pady=10,command=lambda:self.setFuction("8"))
        self.bo7.place(x=180,y=295)
        self.bo7=Button(self,text="9",padx=19,pady=10,command=lambda:self.setFuction("9"))
        self.bo7.place(x=240,y=295)
        self.bo7=Button(self,text="x^",padx=15,pady=10,command=lambda:self.setFuction("x**"))
        self.bo7.place(x=300,y=295)
        self.bo7=Button(self,text="Limpirar\n todo",padx=57,pady=28,command=self.ClerarAll)
        self.bo7.place(x=360,y=295)
        self.bo7=Button(self,text="0",padx=19,pady=10,command=lambda:self.setFuction("0"))
        self.bo7.place(x=120,y=345)
        self.bo7=Button(self,text=".",padx=21,pady=10,command=lambda:self.setFuction("."))
        self.bo7.place(x=180,y=345)
        self.bo7=Button(self,text="AC",padx=14,pady=10,command=self.clearTextInputAll)
        self.bo7.place(x=240,y=345)
        self.bo7=Button(self,text="√",padx=18,pady=10,command=lambda:self.setFuction("sqrt"))
        self.bo7.place(x=300,y=345)
        self.bo7=Button(self,text="(",padx=19,pady=10,command=lambda:self.setFuction("("))
        self.bo7.place(x=120,y=395)
        self.bo7=Button(self,text=")",padx=19,pady=10,command=lambda:self.setFuction(")"))
        self.bo7.place(x=180,y=395)
        self.bo7=Button(self,text="π",padx=19,pady=10,command=lambda:self.setFuction("pi"))
        self.bo7.place(x=240,y=395)
        self.bo7=Button(self,text="e",padx=19,pady=10,command=lambda:self.setFuction("e"))
        self.bo7.place(x=300,y=395)
        self.bo7=Button(self,text="DEL",padx=19,pady=10,command=self.clearTextInputOne)
        self.bo7.place(x=360,y=395)
        self.bo7=Button(self,text="Integrar",padx=23,pady=10,command=self.integrar)
        self.bo7.place(x=435,y=395)
    
        Label(self,text="Función",font=("verdana",8,BOLD)).place(x=120,y=10)
        Label(self,text="Resultado",font=("verdana",8,BOLD)).place(x=120,y=75)
        Label(self,text="Fun. Trigonométricas",font=("verdana",9,BOLD)).place(x=376,y=158)
        
        self.BoxText=Entry(self,font="Arial 13")
        self.BoxText.place(x=120,y=40,width=360,height=30)
        
        self.BoxText1=Entry(self,font="Arial 13")
        self.BoxText1.place(x=120,y=100,width=360,height=30)
