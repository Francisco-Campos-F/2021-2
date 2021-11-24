#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>
#include "set.h"
#include "kruskal.h"

int main(int argc, char** argv){
    if(argc != 2)
    {
        printf("Modo de uso: %s input\nDonde:\n", argv[0]);
        printf("\t\"input\" es la ruta al archivo de input\n");
        return 1;
    }

    // Abrimos el archivo de input
    FILE* input_stream = fopen(argv[1], "r");

    // Si alguno de los dos archivos no se pudo abrir
    if(!input_stream)
    {
        printf("El archivo %s no existe o no se puede leer\n", argv[1]);
        return 2;
    }


    int N; // N° de puntos

    
    fscanf(input_stream, "%d", &N);

    int row;
    int col;

    Punto* puntos =  (Punto*)calloc(N, sizeof(Punto));

    // Obtenemos cada uno de los puntos
    for(int i = 0; i < N; i++)
    {
        fscanf(input_stream, "%d %d", &row, &col);
        puntos[i].id = i;
        puntos[i].x = col;
        puntos[i].y = row;
    }

    int edges_count = N*(N-1)/2;
    MST* mst = make_mst(N, edges_count);

    create_aristas(mst, puntos);

    int resultado = kruskal(mst);
    printf("%d\n", resultado);

    free(puntos);
    free(mst->aristas);
    free(mst);
    fclose(input_stream);
    return 0;
}