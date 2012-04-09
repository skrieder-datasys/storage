// Include the time.h library
#include<time.h>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(int argc, char* argv[])
{
  for(int i =0; i < 10; i++){
    char *buffer;
    long bSize = 1024;
    int blockSize = 1024;
    long iterations = bSize/blockSize;
  
    buffer = (char*)malloc(bSize);
    memset(buffer, 'x', bSize);
  
    FILE * pFile;
    
    char fName[5];
    char buf[5];
    
    char* first = itoa(i, buf, 10);
    char* second = "-1KB.txt";
    char* both = malloc(strlen(first) + strlen(second) + 2);

    sprintf("%s %s", first, second);

    fName = "1KB.txt";

    pFile = fopen (fName, "w" );
    fwrite(buffer, blockSize, iterations, pFile);
    fclose(pFile);
  }
}

