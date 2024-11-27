from tkinter import Label, Tk, Button
import tkinter

window = tkinter.Tk()
window.title('Jogo da Velha')
window.configure(bg="#333333")
window.geometry("485x634")

jogador_atual = "X"
tabuleiro = ["", "", "", "", "", "", "", "", ""]
jogo_ativo = True

label = Label(window, bg="#1f1f1f", width=66, height=8, fg="white", text="Jogador X  -                                                                             - Jogador O")
label.grid(row=0, column=0, padx=10, pady=10)

def alternar_jogador():
    global jogador_atual
    if jogador_atual == "X":
        jogador_atual = "O"
    else:
        jogador_atual = "X"
    label.config(text=f"Jogador X  -                                   {jogador_atual}                                     - Jogador O")


def marcar(i):
    global jogador_atual, tabuleiro, jogo_ativo

    if tabuleiro[i] == "" and jogo_ativo:  
        tabuleiro[i] = jogador_atual
        botoes[i].config(text=jogador_atual)  
        verificar_vitoria()  
        alternar_jogador()  

def verificar_vitoria():
    global jogo_ativo
    vitorias = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  
                (0, 3, 6), (1, 4, 7), (2, 5, 8), 
                (0, 4, 8), (2, 4, 6)]  

    for vitoria in vitorias:
        if tabuleiro[vitoria[0]] == tabuleiro[vitoria[1]] == tabuleiro[vitoria[2]] and tabuleiro[vitoria[0]] != "":
            jogo_ativo = False 
            labelvitoria = Label(window, bg="#1f1f1f", width=66, height=8, fg="white", text=f"Jogador   {tabuleiro[vitoria[0]]}   Venceu!") 
            labelvitoria.grid(row=0, column=0, padx=10, pady=10)

            break

botoes = []

botao1 = Button(window,width=20, height=8, bg="#cccccc", command=lambda i=0: marcar(i))
botao1.place(x=1, y=168)
botoes.append(botao1)
botao2 = Button(window, width=20, height=8, bg="#cccccc", command=lambda i=1: marcar(i))
botao2.place(x=168, y=168)
botoes.append(botao2)
botao3 = Button(window, width=20, height=8, bg="#cccccc", command=lambda i=2: marcar(i))
botao3.place(x=335, y=168)
botoes.append(botao3)
botao4 = Button(window, width=20, height=8, bg="#cccccc", command=lambda i=3: marcar(i))
botao4.place(x=1, y=335)
botoes.append(botao4)
botao5 = Button(window, width=20, height=8, bg="#cccccc", command=lambda i=4: marcar(i))
botao5.place(x=168, y=335)
botoes.append(botao5)
botao6 = Button(window, width=20, height=8, bg="#cccccc", command=lambda i=5: marcar(i))
botao6.place(x=335, y=335)
botoes.append(botao6)
botao7 = Button(window, width=20, height=8, bg="#cccccc", command=lambda i=6: marcar(i))
botao7.place(x=1, y=502) 
botoes.append(botao7)
botao8 = Button(window, width=20, height=8, bg="#cccccc", command=lambda i=7: marcar(i))
botao8.place(x=168, y=502)
botoes.append(botao8) 
botao9 = Button(window, width=20, height=8, bg="#cccccc", command=lambda i=8: marcar(i))
botao9.place(x=335, y=502)
botoes.append(botao9)

window.mainloop()