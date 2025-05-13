# ✅ Como usar o script `semaforo_CA_FNR` no Raspberry Pi

## 📡 1. Descobrir o IP do Raspberry Pi na rede local

Num terminal no teu PC, corre:

```bash
arp -a
```
ou, em linux, 
```bash
sudo arp-scan --localnet
```

Procura uma entrada com o endereço MAC começa por b8-27-eb, que é prefixo oficial da Raspberry Pi Foundation.

---

## 🔐 2. Ligar ao Raspberry Pi via SSH

```bash
ssh pi@192.168.1.233
# Palavra-passe: aluno
```

(Substitui o IP se necessário pelo encontrado com `arp -a`)

---

## 🧰 3. Instalar dependências necessárias (só na primeira vez)

```bash
sudo apt update
sudo apt install -y git feh xdotool
```

---

## 📥 4. Clonar o repositório do projeto

```bash
git clone https://github.com/Duarte-Diamantino/semaforo_CA_FNR.git
```

---

## 📁 5. Navegar até à pasta do projeto

```bash
cd ~/Documents/semaforo_CA_FNR/
```

---

## 🖼️ 8. Preparar o ambiente gráfico (para abrir imagens e mover o rato)

```bash
export DISPLAY=:0
export XAUTHORITY=/home/pi/.Xauthority
```

---


## 🖱️ 7. Exemplos de comandos para mover o cursor do rato

```bash
xdotool mousemove 500 300
xdotool mousemove 1500 1300
```

---


## 🚦 8. Correr o script principal

```bash
python3 semaforo_CA_FNR.py
```

---

## 🔁 9. Passos para reutilizar no futuro

```bash
ssh pi@xxx.xxx.x.xxx
# Palavra-passe: aluno

bash run_semaforos.sh
```
