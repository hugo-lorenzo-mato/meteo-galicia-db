#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include "existe.h"



int fileCheck(char *fileName){
    return (!access(fileName, F_OK ));
}





