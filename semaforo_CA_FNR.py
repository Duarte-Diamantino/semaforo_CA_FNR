import os
import subprocess

# Mapeamento de comandos para imagens
comandos_para_imagens = {
    'frente': 'imagens/frente.png',
    'esq': 'imagens/esquerda.png',
    'dir': 'imagens/direita.png',
    'stop': 'imagens/stop.png',
    'fim': 'imagens/fim.png'
}

# Guarda o processo da imagem atual
processo_imagem = None

def abrir_imagem(caminho):
    global processo_imagem

    # Fecha a imagem anterior se existir
    if processo_imagem and processo_imagem.poll() is None:
        processo_imagem.terminate()

    if not os.path.exists(caminho):
        print(f"[imagem não encontrada] -> {caminho}")
        return

    try:
        # Abre a imagem em full screen com feh (sem output de erros)
        processo_imagem = subprocess.Popen(
            ["feh", "--fullscreen", caminho],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
    except Exception as e:
        print(f"[erro ao abrir imagem]: {e}")

def escutar_comandos():
    while True:
        comando = input("Comando (frente, esq, dir, stop, fim, sair): ").strip().lower()
        if comando == 'sair':
            print("A sair da aplicação...")
            # Fecha a imagem atual antes de sair
            if processo_imagem and processo_imagem.poll() is None:
                processo_imagem.terminate()
            os._exit(0)
        elif comando in comandos_para_imagens:
            caminho = comandos_para_imagens[comando]
            abrir_imagem(caminho)
        else:
            print("Comando inválido ou não suportado.")

if __name__ == "__main__":
    escutar_comandos()
