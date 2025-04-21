import tkinter as tk
from PIL import Image, ImageTk
import threading
import os

# Mapeamento dos comandos para imagens
comandos_para_imagens = {
    'frente': 'imagens/frente.png',
    'esq': 'imagens/esquerda.png',
    'dir': 'imagens/direita.png',
    'stop': 'imagens/stop.png'
}

# Classe da aplicação
class ControladorDeImagem:
    def __init__(self, root):
        self.root = root
        self.root.title("Controle por Terminal")
        self.label = tk.Label(root)
        self.label.pack()
        self.imagem_atual = None

    def mostrar_imagem(self, caminho):
        if not os.path.exists(caminho):
            print(f"[imagem não encontrada] -> {caminho}")
            return  # ignora e continua
        try:
            imagem = Image.open(caminho)
            imagem = imagem.resize((400, 400))
            self.imagem_atual = ImageTk.PhotoImage(imagem)
            self.label.config(image=self.imagem_atual)
        except Exception as e:
            print(f"[erro ao mostrar imagem]: {e}")

    def run(self):
        self.root.mainloop()

# Função de input
def escutar_comandos(app):
    while True:
        comando = input("Comando (frente, esq, dir, stop, fim, sair): ").strip().lower()
        if comando in ['fim', 'sair']:
            print("A sair da aplicação...")
            app.root.quit()
            break
        elif comando in comandos_para_imagens:
            caminho = comandos_para_imagens[comando]
            app.mostrar_imagem(caminho)
        else:
            print("Comando inválido ou não suportado.")

# Execução principal
if __name__ == "__main__":
    root = tk.Tk()
    app = ControladorDeImagem(root)

    thread_comandos = threading.Thread(target=escutar_comandos, args=(app,))
    thread_comandos.daemon = True
    thread_comandos.start()

    app.run()
