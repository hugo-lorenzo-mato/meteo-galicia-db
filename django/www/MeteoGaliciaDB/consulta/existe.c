#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include </home/hugo/PycharmProjects/pintgrupo16/django/www/MeteoGaliciaDB/consulta/existe.h>


/*
1 --> Existe

0 --> No existe

int fileCheck(const char *fileName);


int main (void) {

    char *fileName = "/home/hugo/PycharmProjects/pintgrupo16/django/www/MeteoGaliciaDB/consulta/static/consulta/imagenes/OOFA2YPORF.png";
    if (fileCheck(fileName))
        printf("The File %s\t was Found\n",fileName);
    else
        printf("The File %s\t not Found\n",fileName);
    return 0;
}

*/

int fileCheck(const char *fileName){
    return (!access(fileName, F_OK ));
}





