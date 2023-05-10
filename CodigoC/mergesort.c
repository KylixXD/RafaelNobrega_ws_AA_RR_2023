#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void mergeSort(long  int arr[], long  int l, long  int r);

// Função de mesclagem usada pela função mergeSort()
void merge(long  int arr[], long  int l, long  int m, long int r) {
    long  int i, j, k;
    long  int n1 = m - l + 1;
    long  int n2 = r - m;

    // Cria arrays temporários
    long int L[n1], R[n2];
    // Copia os dados para os arrays temporários L[] e R[]
    for (i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (j = 0; j < n2; j++)
        R[j] = arr[m + 1 + j];

    // Mescla os arrays temporários de volta em arr[l..r]
    i = 0; // Índice inicial do primeiro subarray
    j = 0; // Índice inicial do segundo subarray
    k = l; // Índice inicial do array mesclado
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        }
    else {
        arr[k] = R[j];
        j++;
    }
    k++;
}

// Copia os elementos restantes de L[], se houver algum
while (i < n1) {
    arr[k] = L[i];
    i++;
    k++;
}

// Copia os elementos restantes de R[], se houver algum
while (j < n2) {
    arr[k] = R[j];
    j++;
    k++;
}
}

void mergeSort(long  int arr[], long int l, long int r) {
    if (l < r) {
        long int m = l + (r - l) / 2; // Calcula o índice do elemento central
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);
        merge(arr, l, m, r);
    }
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Erro: use %s <arquivo_de_entrada>\n", argv[0]);
        return 1;
    }

    // Abre o arquivo de entrada
    FILE *input_file = fopen(argv[1], "r");
    if (input_file == NULL) {
        printf("Erro: não foi possível abrir o arquivo de entrada\n");
        return 1;
    }

    // Lê o número de elementos do arquivo de entrada
    int num_elements;
    fscanf(input_file, "%d", &num_elements);

    // Lê os elementos do arquivo de entrada e armazena em um vetor
    long  int *elements = malloc(num_elements * sizeof(long int));
    for (long  int i = 0; i < num_elements; i++) {
        fscanf(input_file, "%d", &elements[i]);
    }
    
    // Fecha o arquivo de entrada
    fclose(input_file);

    // Mede o tempo de execução do Merge Sort
    clock_t start_time = clock();
    mergeSort(elements, 0, num_elements - 1);
    clock_t end_time = clock();
    double elapsed_time_ms = (double)(end_time - start_time) / (CLOCKS_PER_SEC / 1000);

    // Imprime o tempo de execução do Merge Sort em milissegundos
    printf("%.4lf", elapsed_time_ms);

    // Libera a memória alocada
    free(elements);

    return 0;
}
