import subprocess
import statistics
import matplotlib.pyplot as plt
import os

input_files = ["./inputs/1kran.csv","./inputs/10kran.csv","./inputs/500kran.csv","./inputs/1_5mran.csv"]
num_runs = 13

mean_execution_times = []

for input_file in input_files:
    execution_times = []
    for i in range(num_runs):
        process = subprocess.Popen(["./CodigoC/mergesort", input_file], stdout=subprocess.PIPE)
        output, error = process.communicate()
        execution_time = float(output.decode("utf-8"))
        execution_times.append(execution_time)
    
    mean_execution_time = statistics.mean(execution_times)
    mean_execution_times.append(mean_execution_time)

# Plotar o gráfico de linhas
input_files_names = [os.path.basename(file) for file in input_files]
plt.plot(input_files_names, mean_execution_times)
plt.xlabel("Arquivo de entrada")
plt.ylabel("Tempo de execução médio (ms)")
plt.title("Desempenho do Merge Sort para diferentes arquivos de entrada")
plt.show()
