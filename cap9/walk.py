import os


for folderName, subFolders, filenames in os.walk('C:\\Users\\81135998191\\Documents\\PDFs'):
    print("Diretorio atual é: " + folderName)

    for subFolder in subFolders:
        print("O subdiretorio de " + folderName + " eh: " + subFolder)

        for filename in filenames:
            print("Arquivo dentro de " + subFolder + ": " + filename)

        print(" ")