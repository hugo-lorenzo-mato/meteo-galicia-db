%module existe
%{
#define SWIG_FILE_WITH_INIT
#include "existe.h"
%}

int fileCheck(char *fileName);
