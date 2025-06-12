import os
import subprocess
import signal
import sys

# Mapeamento dos comandos para imagens
comandos_para_imagens = {
    'frente': 'imagens/frente.png',
    'esq': 'imagens/esquerda.png',
    'dir': 'imagens/direita.png',
    'stop': 'imagens/stop.png',
    'parque': 'imagens/parque.png',
    'fim': 'imagens/fim.png'
}

# Caminho para a imagem preta
imagem_preta = 'imagens/ecran_preto.png'  # Asegura que está no local correto

# Guarda o processo da imagem atual
processo_imagem = None
processo_preto = None

# Função para colocar o ecrã todo preto
def abrir_preto():
    global processo_preto
    try:
        # Abre a imagem preta no ecrã
        processo_preto = subprocess.Popen(
            ["setsid", "feh", "--fullscreen", imagem_preta],
            stdin=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
    except Exception as e:
        print(f"[erro ao abrir ecrã preto]: {e}")

# Função para abrir uma nova imagem
def abrir_imagem(caminho):
    global processo_imagem

    # Fecha a imagem anterior se ainda estiver aberta
    if processo_imagem and processo_imagem.poll() is None:
        processo_imagem.terminate()
        processo_imagem.wait()  # Espera até a imagem fechar completamente

    if not os.path.exists(caminho):
        print(f"[imagem não encontrada] -> {caminho}")
        return

    try:
        # Abre a nova imagem em full screen com feh isolado da sessão SSH
        processo_imagem = subprocess.Popen(
            ["setsid", "feh", "--fullscreen", caminho],
            stdin=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
    except Exception as e:
        print(f"[erro ao abrir imagem]: {e}")

# Função para fechar a imagem e o fundo preto
def fechar_aplicacao():
    global processo_imagem, processo_preto
    if processo_imagem and processo_imagem.poll() is None:
        processo_imagem.terminate()
        processo_imagem.wait()  # Espera a imagem fechar antes de sair

    if processo_preto and processo_preto.poll() is None:
        processo_preto.terminate()
        processo_preto.wait()  # Espera o fundo preto fechar

# Função para escutar os comandos do terminal
def escutar_comandos():
    abrir_preto()  # Coloca o ecrã preto logo no início

    while True:
        try:
            comando = input("Comando (frente, esq, dir, stop, parque, fim, sair): ").strip().lower()
        except EOFError:
            break  # sai do loop se terminal for fechado

        if comando == 'sair':
            print("A sair da aplicação...")
            fechar_aplicacao()
            os._exit(0)
        elif comando in comandos_para_imagens:
            caminho = comandos_para_imagens[comando]
            abrir_imagem(caminho)
        else:
            print("Comando inválido ou não suportado.")

# Função para capturar o Ctrl+C e garantir o fecho correto
def signal_handler(sig, frame):
    print('Ctrl+C detectado. Fechando aplicação...')
    fechar_aplicacao()
    sys.exit(0)

# Registra o sinal de interrupção (Ctrl+C)
signal.signal(signal.SIGINT, signal_handler)

if __name__ == "__main__":
    escutar_comandos()
