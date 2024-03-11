import os
import shutil
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
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

def listar_arquivos(pasta, listbox):
    listbox.delete(0, tk.END)
    try:
        arquivos = os.listdir(pasta)
        for arquivo in arquivos:
            listbox.insert(tk.END, arquivo)
    except Exception as e:
        listbox.insert(tk.END, f"Erro ao listar arquivos: {e}")

def listar_tipos_arquivos(destino):
    tipos_arquivos_listbox.delete(0, tk.END)
    tipos_arquivos = set()
    try:
        for pasta_atual, _, arquivos in os.walk(destino):
            for arquivo in arquivos:
                caminho_arquivo = os.path.join(pasta_atual, arquivo)
                tipo_arquivo = magic.Magic().from_file(caminho_arquivo)
                tipos_arquivos.add(tipo_arquivo)
    except Exception as e:
        tipos_arquivos_listbox.insert(tk.END, f"Erro ao listar tipos de arquivos: {e}")

    for tipo in tipos_arquivos:
        tipos_arquivos_listbox.insert(tk.END, tipo)

def selecionar_origem():
    if escolha_var.get() == 1:
        origem = filedialog.askopenfilename(title="Selecione o Arquivo")
    else:
        origem = filedialog.askdirectory(title="Selecione a Origem")
    origem_entry.delete(0, tk.END)
    origem_entry.insert(0, origem)
    listar_arquivos(origem, arquivos_listbox)

def selecionar_destino():
    destino = filedialog.askdirectory(title="Selecione o Destino")
    destino_entry.delete(0, tk.END)
    destino_entry.insert(0, destino)
    listar_tipos_arquivos(destino)

def selecionar_imagem_fundo():
    imagem_fundo_path = filedialog.askopenfilename(title="Selecione a Imagem de Fundo", filetypes=[("Imagens", "*.png;*.jpg;*.jpeg;*.gif")])
    if imagem_fundo_path:
        imagem_fundo = Image.open(imagem_fundo_path)
        imagem_fundo = imagem_fundo.resize((600, 500))
        imagem_fundo = ImageTk.PhotoImage(imagem_fundo)
        background_label.configure(image=imagem_fundo)
        background_label.image = imagem_fundo

        # Adicionando mensagem de sucesso
        status_label.config(text="Imagem de fundo selecionada com sucesso!")

def iniciar_backup():
    origem = origem_entry.get()
    destino = destino_entry.get()
    resultado = fazer_backup(origem, destino)

    # Exibindo mensagem de sucesso ou erro
    status_label.config(text=resultado)

# Criando a interface gráfica
root = tk.Tk()
root.title("Backup Supremo")
root.geometry("600x500")

# Configurando a imagem de fundo
imagem_fundo_path = "D:\\Imagens\\Space-Art-Wallpaper-Sci-Fi-space-8070476-1600-1200.jpg"
imagem_fundo = Image.open(imagem_fundo_path)
imagem_fundo = imagem_fundo.resize((600, 500))
imagem_fundo = ImageTk.PhotoImage(imagem_fundo)
background_label = tk.Label(root, image=imagem_fundo)
background_label.place(relwidth=1, relheight=1)

# Variável de controle para a escolha de arquivo ou pasta
escolha_var = tk.IntVar()
escolha_var.set(1)  # Inicialmente configurado para enviar um arquivo

# Botão de opção para escolher entre arquivo ou pasta
opcao_arquivo = tk.Radiobutton(root, text="Arquivo", variable=escolha_var, value=1, background="lightgray")
opcao_pasta = tk.Radiobutton(root, text="Pasta", variable=escolha_var, value=2, background="lightgray")

# Posicionando as opções de arquivo e pasta no canto superior direito
opcao_arquivo.place(relx=0.85, rely=0.05, anchor=tk.NE)
opcao_pasta.place(relx=0.85, rely=0.1, anchor=tk.NE)

# Espaçamento
tk.Label(root, text="", background="white").pack()

# Widgets
origem_label = tk.Label(root, text="Origem:", background="white")
origem_label.pack()

origem_entry = tk.Entry(root, width=40)
origem_entry.pack()

origem_selecionar_button = tk.Button(root, text="Selecionar Origem", command=selecionar_origem, background="lightblue")
origem_selecionar_button.pack()

destino_label = tk.Label(root, text="Destino:", background="white")
destino_label.pack()

destino_entry = tk.Entry(root, width=40)
destino_entry.pack()

destino_selecionar_button = tk.Button(root, text="Selecionar Destino", command=selecionar_destino, background="lightgreen")
destino_selecionar_button.pack()

arquivos_label = tk.Label(root, text="Arquivos na Origem:", background="white")
arquivos_label.pack()

arquivos_listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=5, width=40)
arquivos_listbox.pack()

tipos_arquivos_label = tk.Label(root, text="Tipos de Arquivos no Destino:", background="white")
tipos_arquivos_label.pack()

tipos_arquivos_listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=5, width=40)
tipos_arquivos_listbox.pack()

backup_button = tk.Button(root, text="Iniciar Backup", command=iniciar_backup, background="orange")
backup_button.pack()

status_label = tk.Label(root, text="", background="white")
status_label.pack()

# Rodapé
developer_label = tk.Label(root, text="Developer_Pedro_Lobato", background="white")
developer_label.place(relx=0.5, rely=1, anchor=tk.S)

# Rodar a interface gráfica
root.mainloop()
