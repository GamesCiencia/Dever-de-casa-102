import os
import shutil

from_dir = "C:/Users/thoma/OneDrive/Área de Trabalho/BYJUs/Deveres de casa/Arquivos_Documentos"
to_dir = "C:/Users/thoma/OneDrive/Área de Trabalho/BYJUs/Deveres de casa/Arquivos_Chegada"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)
    #print(name)
    #print(extension)

    if extension == '':
        continue
    if extension in ['.txt']:

path1 = from_dir + '/' + file_name
path2 = to_dir + '/' + "Arquivos_Documentos"
path3 = to_dir + '/' + "Arquivos_Documentos" + '/' + file_name
print("path1 ", path1)
print("path3 ", path3)

# Verifique se o caminho da pasta/diretório existe ante de mover
# Caso contrário, crie uma NOVA pasta/diretório, e então mova

if os.path.exists(path2):
    print("Movendo " + file_name + ".....")

    # Mover de path1 ---> path3
    shutil.move(path1, path3)

else:
    os.makedirs(path2)
    print("Movendo " + file_name + ".....")
    shutil.move(path1, path3)
