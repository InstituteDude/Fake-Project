
import tkinter as tk

def usd_to_idr():
	angka = textbox.get()
	dollar = float(angka)* 14405.5
	text.set("Rp. "+str(dollar))
	label2.config(font=('Helvetica',15,"bold"),fg="green")


window = tk.Tk()
window.title("USD To IDR Converter :)")
window.geometry("400x150")

label1 = tk.Label(window, text= "USD '$' ",font=('Helvetica',12,"bold"))
label1.pack()

textbox = tk.Entry(window,font=('Helvetica', 15, "bold"),width=6,justify=tk.CENTER)
textbox.pack()

btn=tk.Button(window,text="TO", command= usd_to_idr,font=('Helvetica',12,'bold'))
btn.pack()

label4 = tk.Label(window, text= "IDR 'Rp' ",font=('Helvetica',12,"bold"))
label4.pack()

text =  tk.StringVar()
text.set("0")


label2 = tk.Label(window, font=('Helvetica', 12,"bold"),textvariable=text)
label2.pack()


window.mainloop()
