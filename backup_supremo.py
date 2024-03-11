import os
import shutil
import getpass
import sys
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Backup Supremo")

# Convertendo a imagem para o formato suportado (PNG)
imagem_original = Image.open("D:\\Imagens\\Formatura\\IMG_8921.jpg")
imagem_original.save("D:\\Imagens\\Formatura\\IMG_8921.png")

# Configurando uma imagem de fundo
background_image = ImageTk.PhotoImage(file="D:\\Imagens\\Formatura\\IMG_8921.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Resto do código para a interface
label = ttk.Label(root, text="Bem-vindo ao Backup Supremo!", font=("Arial", 18))
label.pack(pady=20)

# Adicione seus outros widgets aqui...

root.mainloop()



senha_correta = "1515Pe@"

# Número máximo de tentativas
tentativas_maximas = 3

for tentativa in range(1, tentativas_maximas + 1):
    # Solicitação da senha
    senha_usuario = input(f"Tentativa {tentativa}/{tentativas_maximas}. Digite a senha: ")

    # Verifica se a senha está correta
    if senha_usuario == senha_correta:
        print("Senha correta! Continuando com o backup.")
        break  # Sai do loop se a senha estiver correta
    else:
        print("Senha incorreta.")

    # Se todas as tentativas falharem
    if tentativa == tentativas_maximas:
        print("Número máximo de tentativas atingido. Bloqueando o acesso.")
        sys.exit(1)  # Sai do script com código de erro 1

while True:
    # Mensagem inicial
    print("Bem-vindo ao Backup Supremo!")

    # Solicitação manual dos caminhos de origem e destino
    origem = input("Digite o caminho de origem: ").strip('\"')
    destino = input("Digite o caminho de destino: ").strip('\"')

    try:
        # Cria o diretório de destino se ainda não existir
        os.makedirs(destino, exist_ok=True)

        # Verifica se a origem é um arquivo
        if os.path.isfile(origem):
            shutil.copy2(origem, destino)
            print("Transferência do arquivo concluída com sucesso!")
        else:
            # Percorre todos os arquivos e subdiretórios na origem
            for pasta_atual, subpastas, arquivos in os.walk(origem):
                # Calcula o caminho de destino correspondente
                caminho_destino = os.path.join(destino, os.path.relpath(pasta_atual, origem))

                # Cria o diretório de destino se ainda não existir
                os.makedirs(caminho_destino, exist_ok=True)

                # Copia cada arquivo para o destino
                for arquivo in arquivos:
                    caminho_origem = os.path.join(pasta_atual, arquivo)
                    caminho_destino_arquivo = os.path.join(caminho_destino, arquivo)

                    # Copia o arquivo, substituindo se já existir
                    shutil.copy2(caminho_origem, caminho_destino_arquivo)

            print("Transferência de arquivos concluída com sucesso!")

    except Exception as e:
        print(f"Erro durante a transferência: {e}")

    # Pergunta ao usuário se deseja fazer um novo backup
    novo_backup = input("Deseja fazer um novo backup? (s/n): ")
    if novo_backup.lower() != 's':
        break  # Sai do loop se a resposta não for 's'