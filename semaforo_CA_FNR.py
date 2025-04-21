import tkinter as tk
from PIL import Image, ImageTk
import threading

# Mapeamento dos comandos para imagens
comandos_para_imagens = {
    'frente': 'imagens/frente.png',
    'tras': 'imagens/tras.png',
    'esq': 'imagens/esquerda.png',
    'dir': 'imagens/direita.png',
    'stop': 'imagens/stop.png'
}

# Criação da interface
class ControladorDeImagem:
    def __init__(self, root):
        self.root = root
        self.root.title("Controle por Terminal")
        self.label = tk.Label(root)
        self.label.pack()
        self.imagem_atual = None

    def mostrar_imagem(self, caminho):
        imagem = Image.open(caminho)
        imagem = imagem.resize((400, 400))  # Tamanho ajustável
        self.imagem_atual = ImageTk.PhotoImage(imagem)
        self.label.config(image=self.imagem_atual)

    def run(self):
        self.root.mainloop()

# Função para ler comandos do terminal
def escutar_comandos(app):
    while True:
        comando = input("Comando (frente, tras, esq, dir, stop, fim): ").strip().lower()
        if comando == 'fim':
            print("Encerrando programa...")
            app.root.quit()
            break
        elif comando in comandos_para_imagens:
            caminho = comandos_para_imagens[comando]
            app.mostrar_imagem(caminho)
        else:
            print("Comando inválido.")

# Execução principal
if __name__ == "__main__":
    root = tk.Tk()
    app = ControladorDeImagem(root)

    # Thread separada para os inputs do terminal
    thread_comandos = threading.Thread(target=escutar_comandos, args=(app,))
    thread_comandos.daemon = True
    thread_comandos.start()

    app.run()
