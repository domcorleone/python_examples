"""
    Author: Eder Machado
    Description: Append info to a file in python 3.x
    Create Date: 19.10.2022 11:41 AM
"""

appendMe = "Di"

appendFile = open("sons.txt", "a")
print("Ficheiro aberto com sucesso...")
appendFile.write('\n')
appendFile.write(appendMe)
print("Ficheiro escrito com sucesso...")
appendFile.close()
print("Ficheiro fechado com sucesso...")
