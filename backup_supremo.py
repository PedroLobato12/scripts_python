import os
import shutil

# Solicitação manual dos caminhos de origem e destino
origem = input("Digite o caminho de origem: ")
destino = input("Digite o caminho de destino: ")

try:
    # Cria o diretório de destino se ainda não existir
    os.makedirs(destino, exist_ok=True)

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

    input("Pressione qualquer tecla para sair...")