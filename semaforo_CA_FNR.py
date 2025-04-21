import os
import subprocess

# Mapeamento dos comandos para imagens
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

    # Fecha a imagem anterior se ainda estiver aberta
    if processo_imagem and processo_imagem.poll() is None:
        processo_imagem.terminate()

    if not os.path.exists(caminho):
        print(f"[imagem não encontrada] -> {caminho}")
        return

    try:
        # Abre a imagem em full screen com feh isolado da sessão SSH
        processo_imagem = subprocess.Popen(
            ["setsid", "feh", "--fullscreen", caminho],
            stdin=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
    except Exception as e:
        print(f"[erro ao abrir imagem]: {e}")

def escutar_comandos():
    while True:
        try:
            comando = input("Comando (frente, esq, dir, stop, fim, sair): ").strip().lower()
        except EOFError:
            break  # sai do loop se terminal for fechado

        if comando == 'sair':
            print("A sair da aplicação...")
            if processo_imagem and processo_imagem.poll() is None:
                processo_imagem.terminate()
            os._exit(0)
        elif comando in comandos_para_imagens:
            caminho = comandos_para_imagens[comando
