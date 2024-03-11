import os
import shutil
import tkinter as tk
from tkinter import filedialog
import magic

def fazer_backup(origem, destino):
    try:
        # Cria o diretório de destino se ainda não existir
        os.makedirs(destino, exist_ok=True)

        # Verifica se a origem é um arquivo
        if os.path.isfile(origem):
            shutil.copy2(origem, destino)
            return "Transferência do arquivo concluída com sucesso!"
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

            return "Transferência de arquivos concluída com sucesso!"

    except Exception as e:
        return f"Erro durante a transferência: {e}"

def selecionar_origem():
    origem = filedialog.askdirectory(title="Selecione a Origem")
    origem_entry.delete(0, tk.END)
    origem_entry.insert(0, origem)
    listar_arquivos(origem)

def selecionar_destino():
    destino = filedialog.askdirectory(title="Selecione o Destino")
    destino_entry.delete(0, tk.END)
    destino_entry.insert(0, destino)
    listar_tipos_arquivos(destino)

def listar_arquivos(pasta):
    arquivos_listbox.delete(0, tk.END)
    arquivos = os.listdir(pasta)
    for arquivo in arquivos:
        arquivos_listbox.insert(tk.END, arquivo)

def listar_tipos_arquivos(destino):
    tipos_arquivos_listbox.delete(0, tk.END)
    tipos_arquivos = set()
    for pasta_atual, _, arquivos in os.walk(destino):
        for arquivo in arquivos:
            caminho_arquivo = os.path.join(pasta_atual, arquivo)
            tipo_arquivo = magic.Magic().from_file(caminho_arquivo)
            tipos_arquivos.add(tipo_arquivo)

    for tipo in tipos_arquivos:
        tipos_arquivos_listbox.insert(tk.END, tipo)

def iniciar_backup():
    origem = origem_entry.get()
    destino = destino_entry.get()
    resultado = fazer_backup(origem, destino)
    resultado_label.config(text=resultado)

# Criando a interface gráfica
root = tk.Tk()
root.title("Backup Supremo")

# Widgets
origem_label = tk.Label(root, text="Caminho de Origem:")
origem_label.pack()

origem_entry = tk.Entry(root, width=50)
origem_entry.pack()

origem_selecionar_button = tk.Button(root, text="Selecionar Origem", command=selecionar_origem)
origem_selecionar_button.pack()

destino_label = tk.Label(root, text="Caminho de Destino:")
destino_label.pack()

destino_entry = tk.Entry(root, width=50)
destino_entry.pack()

destino_selecionar_button = tk.Button(root, text="Selecionar Destino", command=selecionar_destino)
destino_selecionar_button.pack()

arquivos_label = tk.Label(root, text="Arquivos na Origem:")
arquivos_label.pack()

arquivos_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
arquivos_listbox.pack()

tipos_arquivos_label = tk.Label(root, text="Tipos de Arquivos no Destino:")
tipos_arquivos_label.pack()

tipos_arquivos_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
tipos_arquivos_listbox.pack()

backup_button = tk.Button(root, text="Iniciar Backup", command=iniciar_backup)
backup_button.pack()

resultado_label = tk.Label(root, text="")
resultado_label.pack()

# Rodar a interface gráfica
root.mainloop()




