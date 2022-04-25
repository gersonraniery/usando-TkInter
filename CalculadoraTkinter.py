from tkinter import *
from tkinter import ttk


cor1 = "#0d0d0c"
cor3 = "#38576b"
cor4 = "#ECEFF1"
cor5 = "#FFAB40"

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x310")

# criando frames
frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(column=0, row=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(column=0, row=1)

# variavel todos valores
todos_valores = ''
# Criando label
valor_texto = StringVar()


def entra_valor(event):
    global todos_valores
    todos_valores += str(event)

    # passando o valor para tela
    valor_texto.set(todos_valores)


# funcao para calcular
def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))


# funcao de limpar a tela
def limpar_tela():
    global todos_valores
    todos_valores = ''
    valor_texto.set('')


app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=cor3, fg=cor4)
app_label.place(x=0, y=0)


# criando botoes

but_1 = Button(frame_corpo, command=limpar_tela, text="C", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
but_1.place(x=0, y=0)
but_2 = Button(frame_corpo, command=lambda: entra_valor("%"), text="%", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
but_2.place(x=118, y=0)
but_3 = Button(frame_corpo, command=lambda: entra_valor("/"), text="/", width=5, height=2, bg=cor5, fg=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
but_3.place(x=177, y=0)

but_4 = Button(frame_corpo, command=lambda: entra_valor("7"), text="7", width=6, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
but_4.place(x=0, y=52)
but_5 = Button(frame_corpo, command=lambda: entra_valor("8"), text="8", width=6, height=2, bg=cor5, fg=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
but_5.place(x=59, y=52)
but_6 = Button(frame_corpo, command=lambda: entra_valor("9"), text="9", width=6, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
but_6.place(x=118, y=52)
but_7 = Button(frame_corpo, command=lambda: entra_valor("*"), text="*", width=6, height=2, bg=cor5, fg=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
but_7.place(x=177, y=52)

but_8 = Button(frame_corpo, command=lambda: entra_valor("4"), text="4", width=6, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
but_8.place(x=0, y=104)
but_9 = Button(frame_corpo, command=lambda: entra_valor("5"), text="5", width=6, height=2, bg=cor5, fg=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
but_9.place(x=59, y=104)
but_10 = Button(frame_corpo, command=lambda: entra_valor("6"), text="6", width=6, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
but_10.place(x=118, y=104)
but_11 = Button(frame_corpo, command=lambda: entra_valor("-"), text="-", width=6, height=2, bg=cor5, fg=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
but_11.place(x=177, y=104)

but_8 = Button(frame_corpo, command=lambda: entra_valor("1"), text="1", width=6, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
but_8.place(x=0, y=156)
but_9 = Button(frame_corpo, command=lambda: entra_valor("2"), text="2", width=6, height=2, bg=cor5, fg=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
but_9.place(x=59, y=156)
but_10 = Button(frame_corpo, command=lambda: entra_valor("3"), text="3", width=6, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
but_10.place(x=118, y=156)
but_11 = Button(frame_corpo, command=lambda: entra_valor("+"), text="+", width=6, height=2, bg=cor5, fg=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
but_11.place(x=177, y=156)

but_1 = Button(frame_corpo, command=lambda: entra_valor("0"), text="0", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
but_1.place(x=0, y=208)
but_2 = Button(frame_corpo, command=lambda: entra_valor("."), text=".", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
but_2.place(x=118, y=208)
but_3 = Button(frame_corpo, command=calcular, text="=", width=5, height=2, bg=cor5, fg=cor1, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
but_3.place(x=177, y=208)


janela.mainloop()
