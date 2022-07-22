#Importe o repósitorio request e tkinter
#no linux tive problemas para executalo, se vc também estiver use (sudo apt-get install python3-tk)
import requests
from tkinter import *
from tkinter import ttk

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto_resposta['text'] = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

janela = Tk()
janela.title("Cotação de Hoje")
texto = Label(janela, text="Clique no botão para ver as cotações de moedas")
texto.grid(column=0, row=0, padx=10, pady=10)

botao = Button(janela, text="Buscar cotações", command=pegar_cotacoes)
botao.grid(column=0, row=1, padx=10, pady=10)

texto_resposta = Label(janela, text="")
texto_resposta.grid(column=0, row=2, padx=10, pady=10)

#Precisa colocar o mainloop na Janela para não fecha o código
janela.mainloop()
#tabela rápida para progamadores iniciantes
#espero quem gostem
#by Mateusnasciment
#repósitorio para estudos gratuito >> https://dcc.ufrj.br/~fabiom/mab225/14gui.pdf