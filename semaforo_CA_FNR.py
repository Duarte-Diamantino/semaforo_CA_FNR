import os
import subprocess
import threading

# Mapeamento dos comandos para imagens
comandos_para_imagens = {
    'frente': 'imagens/frente.png',
    'esq': 'imagens/esquerda.png',
    'dir': 'imagens/direita.png',
    'stop': 'imagens/stop.png',
    'fim': 'imagens/fim.png'
}

# Abrir imagem com programa padrão do sistema
def abrir_imagem(caminho):
    if not os.path.exists(caminho):
        print(f"[imagem não encontrada] -> {caminho}")
        return
    try:
        subprocess.Popen(["xdg-open", caminho])  # para sistemas Linux (como Raspberry Pi OS)
    except Exception as e:
        print(f"[erro ao abrir imagem]: {e}")

# Escutar comandos
def escutar_comandos():
    while True:
        comando = input("Comando (frente, esq, dir, stop, fim, sair): ").strip().lower()
        if comando == 'sair':
            print("A sair da aplicação...")
            os._exit(0)  # encerra imediatamente
        elif comando in comandos_para_imagens:
            caminho = comandos_para_imagens[comando]
            abrir_imagem(caminho)
        else:
            print("Comando inválido ou não suportado.")

# Main
if __name__ == "__main__":
    escutar_comandos()
