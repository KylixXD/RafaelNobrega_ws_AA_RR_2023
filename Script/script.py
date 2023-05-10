import subprocess
import statistics
import matplotlib.pyplot as plt
import os


input_files = []
num_runs = 13

for file in os.scandir("E:\Backup\Codigos_gerais\8-semestre\Analise_algoritmos\RafaelNobrega_ws_AA_RR_2023\inputs"):
    input_files += [file.path]


mean_execution_times = []

log = open("execution_time.txt", 'w')
for input_file in input_files:
    execution_times = []
    print("execuções do",input_file)
    for i in range(num_runs):
        process = subprocess.Popen(["E:\Backup\Codigos_gerais\8-semestre\Analise_algoritmos\RafaelNobrega_ws_AA_RR_2023\CodigoC\mergesort.exe", input_file], stdout=subprocess.PIPE)
        output, error = process.communicate()
        try:
            execution_time = float(output.decode("utf-8"))
            execution_times.append(execution_time)
            log.write(str(execution_time) + "\n")
            print(execution_time)
        except ValueError:
            execution_time = None

    
    mean_execution_time = statistics.mean(execution_times) if execution_times else 0
    mean_execution_times.append(mean_execution_time)

print(mean_execution_times)
# Plotar o gráfico de linhas
input_files_names = [os.path.splitext(os.path.basename(file))[0] for file in input_files]
plt.plot(input_files_names, mean_execution_times)
plt.xlabel("Arquivo de entrada")
plt.ylabel("Tempo de execução médio (ms)")
plt.title("Desempenho do Merge Sort para diferentes arquivos de entrada")
plt.savefig('grafico.png')
