from tkinter import *
from tkinter import ttk

# Importando tkcalendar depois de ter instalado no venv
from tkcalendar import Calendar, DateEntry

# Importando dateutil depois de ter intalado no venv
from dateutil.relativedelta import relativedelta

# Importando o datetime
from datetime import date

cor1 = "#3b3b3b"
cor2 = "#4a4a48"
cor3 = "#ffffff"
cor4 = "#f79b07"
cor5 = "#fcc058"  # Amarelo

janela = Tk()
janela.title("Calculadora de Idade")
janela.geometry("310x400")

# Frame da parte de cima
frame_cima = Frame(janela, width=310, height=150, padx=0, pady=0, relief='flat', bg=cor1)
frame_cima.grid(column=0, row=0)

# Frame do corpo
frame_corpo = Frame(janela, width=310, height=300, padx=0, pady=0, relief='flat', bg=cor2)
frame_corpo.grid(column=0, row=1)

# Label do frame de cima
label_calculadora = Label(frame_cima, text="CALCULADORA", width=25, height=1, padx=3, relief='flat', anchor='center', font=('Ivi 15 bold'), bg=cor1, fg=cor3)
label_calculadora.place(x=0, y=30)

label_idade = Label(frame_cima, text="DE IDADE", width=11, height=1, padx=0, relief='flat', anchor='center', font=('Arial 35 bold'), bg=cor1, fg=cor5)
label_idade.place(x=0, y=70)


# ---- Criando a funcao calcular idade
def calcular():
    inicial = cal_inicial.get()
    nascimento = cal_nascimento.get()

    # separando os valores
    dia_inic, mes_inic, ano_inic = [int(x) for x in inicial.split('/')]

    # convertendo os valores em formato date/datetime
    data_inicial = date(ano_inic, mes_inic, dia_inic)

    dia_nasci, mes_nasci, ano_nasci = [int(x) for x in nascimento.split('/')]

    # convertendo os valores em formato date/datetime
    data_nascimento = date(ano_nasci, mes_nasci, dia_nasci)

    anos = relativedelta(data_inicial, data_nascimento).years
    meses = relativedelta(data_inicial, data_nascimento).months
    dias = relativedelta(data_inicial, data_nascimento).days

    l_app_anos['text'] = anos
    l_app_meses['text'] = meses
    l_app_dias['text'] = dias


# --Label do frame de baixo
l_data_inical = Label(frame_corpo, text="Data inicial", height=1, padx=0, pady=0, relief='flat', anchor=NW, font='Ivi 11', bg=cor2, fg=cor3)
l_data_inical.place(x=40, y=30)

cal_inicial = DateEntry(frame_corpo, width=13, bg='darkblue', fg=cor3, borderwidth=2, date_pattern='d/m/y', y=2022, locale='pt_BR')
cal_inicial.place(x=190, y=30)


l_data_nascimento = Label(frame_corpo, text="Data de nascimento", height=1, padx=0, pady=0, relief='flat', anchor=NW, font='Ivi 11', bg=cor2, fg=cor3)
l_data_nascimento.place(x=40, y=70)

cal_nascimento = DateEntry(frame_corpo, width=13, bg='darkblue', fg=cor3, borderwidth=2, date_pattern='d/m/y', y=2022, locale='pt_BR')
cal_nascimento.place(x=190, y=70)

# ----- Label dos resultados
l_app_anos = Label(frame_corpo, text="--", height=1, padx=0, pady=0, relief='flat', anchor='center', font='Ivi 25 bold', bg=cor2, fg=cor3)
l_app_anos.place(x=60, y=135)
l_app_anos_nome = Label(frame_corpo, text="Anos", height=1, padx=0, pady=0, relief='flat', anchor='center', font='Ivi 11 bold', bg=cor2, fg=cor3)
l_app_anos_nome.place(x=60, y=175)

l_app_meses = Label(frame_corpo, text="--", height=1, padx=0, pady=0, relief='flat', anchor='center', font='Ivi 25 bold', bg=cor2, fg=cor3)
l_app_meses.place(x=140, y=135)
l_app_meses_nome = Label(frame_corpo, text="Meses", height=1, padx=0, pady=0, relief='flat', anchor='center', font='Ivi 11 bold', bg=cor2, fg=cor3)
l_app_meses_nome.place(x=130, y=175)

l_app_dias = Label(frame_corpo, text="--", height=1, padx=0, pady=0, relief='flat', anchor='center', font='Ivi 25 bold', bg=cor2, fg=cor3)
l_app_dias.place(x=220, y=135)
l_app_dias_nome = Label(frame_corpo, text="Dias", height=1, padx=0, pady=0, relief='flat', anchor='center', font='Ivi 11 bold', bg=cor2, fg=cor3)
l_app_dias_nome.place(x=220, y=175)

# ---Criando o botao calcular
bt_calcular = Button(frame_corpo, command=calcular, text="Calcular", width=20, height=1, relief='raised', overrelief='ridge', font='Ivi 10 bold', bg=cor2, fg=cor3)
bt_calcular.place(x=70, y=215)


janela.mainloop()
