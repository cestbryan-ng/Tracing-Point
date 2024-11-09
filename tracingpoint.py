"""Script tracingpoint.py

Usage
=====
    App Tracing Point
"""

__author__ = "Jean-Roland Bryan Ngoupeyou"
__date__ = "09/11/2024"
__credits__ = "ngoupeyoubryan9@gmail.com"
__version__ = "1.0"

#importation modules.
from numpy import *
import matplotlib.pyplot as plt
import tkinter.messagebox
import customtkinter

#Evenements

def click() :
#Evenement pour tracer la fonction.
    try :
        entrée = entry1.get()
        X = linspace(-200, 200, 10000)
        Y = list()
        for _ in X :
            x = _
            Y.append(eval(entrée)) 
        Y = array(Y)
        plt.plot(X, Y, label = entrée)
        plt.xlim(-100, 100)
        plt.ylim(-100, 100)
        plt.xlabel("Axe des x"); plt.ylabel("Axe des y")
        plt.legend()
        plt.grid()
        plt.title("Tracing Point")
        plt.show()
    except :                    #I dont Know the exception, reason why i catch all the exceptions.
        tkinter.messagebox.showinfo("Error", "Ca ne s'est pas passé comme prévu\nEntrer une fonction valide, la variable est uniquement 'x'.")

def quitter() :
#Evenement pour fermer l'app.
    fenetre.destroy()
#---------
    
#UI/UX.

#Chargement de la fenetre.
fenetre = customtkinter.CTk()
fenetre.geometry("650x350")
fenetre.title("Tracing Point")

#fonts.
font1 = customtkinter.CTkFont(family = "Helvetica", size = 44, underline = True, weight = "bold")
font2 = customtkinter.CTkFont(family = "Cambria", weight = "bold")
font3 = customtkinter.CTkFont(family = "Cambria", weight = "bold", size = 16)

#Page(Interface).
frame = customtkinter.CTkFrame(fenetre, width = 500, height = 300, border_width = 5, corner_radius = 50, border_color = "white")
text1 = customtkinter.CTkLabel(frame, text = "TRACING POINT", font = font1, text_color = "yellow")
text1.place(x = 80, y = 5)
text2 = customtkinter.CTkLabel(frame, font = font3, text = "Grâce à cette application, réaliser le tracé de vos fonctions.\nExemples de fonction : 2x+2, log(x), cos(x)**2+1.")
text2.place(x = 40, y = 80)
entry1 = customtkinter.CTkEntry(frame, width = 300, fg_color = "lightblue",font = font2 , border_color = "white", text_color = "black" ,placeholder_text = "Entrer votre fonction ici.                   ", placeholder_text_color = "black", corner_radius = 30, justify = "right")
entry1.place(x = 100, y = 150)
button1 = customtkinter.CTkButton(frame,command = click, font = font2, width = 100, text = "Tracer",border_width = 3 ,border_color= "white", hover_color = "yellow")
button1.place(x = 200, y = 200)
button2 = customtkinter.CTkButton(frame,command = quitter, font = font2, width = 100, fg_color = "red" ,text = "Quitter",border_width = 3 ,border_color= "white", hover_color = "red")
button2.place(x = 200, y = 235)
frame.pack(side = customtkinter.TOP, pady = 20)

fenetre.mainloop()
#------
