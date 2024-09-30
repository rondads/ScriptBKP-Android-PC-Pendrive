import os # Utilizado para operações de sistema como listar arquivos, remover arquivos e diretórios, etc.
import shutil # Usado para operações de alto nível com arquivos e pastas, como copiar e deletar diretórios.
import subprocess # Para executar comandos externos no script, no caso o ADB.


# Diretório no PC para onde as fotos do celular serão copiadas. / variável utilizada na função1 e função2.
pastas_fotos_pc = "D:\Backupcompleto\Bkp_fotos_cel"


# Diretório no celular onde as fotos estão armazenadas (caminho pelo adb). / variável utilizada na função2.
pastas_fotos_celular = "/sdcard/Fotos/Galeria"


# Diretório do backup completo no PC. / variável utilizada na função3.
bkpfull_pc = "D:\Backupcompleto"


# Diretório para onde o backup completo será copiado no pendrive. / variável utilizada na função3.
bkpfull_pendrive = "E:\Novapasta"





# função1 = Esta função prepara a pasta que vai receber o backup de fotos do celular, deletando o backup anterior de fotos no PC.
def limpar_pasta(pastas_fotos_pc):
    for arquivos in os.listdir(pastas_fotos_pc): # Lista todos os arquivos e pastas no diretório.
        caminho_dos_arquivos_pastas_fotos_pc = os.path.join(pastas_fotos_pc, arquivos)
        try:
            if os.path.isfile(caminho_dos_arquivos_pastas_fotos_pc): # Se for arquivo, usa os.unlink() para deletá-lo.
                os.unlink(caminho_dos_arquivos_pastas_fotos_pc)
            elif os.path.isdir(caminho_dos_arquivos_pastas_fotos_pc): # Se for diretório, usa shutil.rmtree() para removê-lo completamente.
                shutil.rmtree(caminho_dos_arquivos_pastas_fotos_pc)
            print(f"As pastas de fotos do BKP anterior foram excluídas com sucesso")
        except Exception as Naofileoudir:
            print(f"Houve algum erro ao deletar a pasta de fotos do BKP anterior {caminho_dos_arquivos_pastas_fotos_pc}: {Naofileoudir}")





# função2 = Esta função copia as fotos do celular para o PC utilizando o comando ADB (adb pull).
def copiar_arquivos_cel(pastas_fotos_celular, pastas_fotos_pc):
    try:
        # Comando ADB para puxar arquivos, que copia o conteúdo de pastas_fotos_celular (diretório no celular) para pastas_fotos_pc (diretório no PC).
        comando = ["adb", "pull", pastas_fotos_celular, pastas_fotos_pc]
        subprocess.run(comando, check=True)
        print("Pastas de fotos do celular copiadas com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"Houve algum erro ao copiar as fotos do celular: {e}")





# função3 = Esta função copia o backup completo do PC para o pendrive.
def copiar_para_pendrive(bkpfull_pc, bkpfull_pendrive):
    try:
          # Verifica se o diretório de destino já existe, se sim, deleta o diretório antigo usando shutil.rmtree(), resolvendo o bug "[WinError 5] Access is denied".
        if os.path.exists(bkpfull_pendrive):
            shutil.rmtree(bkpfull_pendrive)
            print("O diretório de destino já existia. Foi excluído com sucesso.")
        
        # Em seguida, copia o diretório bkpfull_pc (backup completo no PC) para bkpfull_pendrive (pendrive) utilizando shutil.copytree().
        shutil.copytree(bkpfull_pc, bkpfull_pendrive)
        print("Backup no Pendrive concluído com sucesso!")
    except Exception as e:
        print(f"Houve algum erro ao efetuar o BKP para o pendrive: {e}")





# ATENÇÃO!!1 Antes de rodar o código, é necessário que o celular esteja conectado ao PC via USB, com a depuração USB ativada (geralmente nas opções de desenvolvedor), e 
# que o pendrive esteja plugado e formatado, com uma "Novapasta" criada para receber o backup do PC.
def realizar_backup():
    
    # função1: Limpar o backup anterior das fotos no PC.
    limpar_pasta(pastas_fotos_pc)
    

    # função2: Copiar as fotos do celular para o PC.
    copiar_arquivos_cel(pastas_fotos_celular, pastas_fotos_pc)
    
    
    # função3: Copiar o backup do PC para o pendrive.
    copiar_para_pendrive(bkpfull_pc, bkpfull_pendrive)
    
# Esta é a função principal, ela unifica o processo de backup, executando as três funções mencionadas anteriormente.
realizar_backup()
