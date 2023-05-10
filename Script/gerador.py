import random
import csv
import os 

def gerar_csv(nome_arquivo, n):
    with open(nome_arquivo, 'w', newline='') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow([n])
        for i in range(n):
            valor = random.randint(1, 1000000)
            writer.writerow([valor])
            
os.system("cd E:\Backup\Codigos_gerais\8-semestre\Analise_algoritmos\RafaelNobrega_ws_AA_RR_2023\inputs && del *")
for randons in range(100, 600000 , 100000):
    gerar_csv(f'../inputs/{randons//1000}k_ran.csv', randons)
    


      
