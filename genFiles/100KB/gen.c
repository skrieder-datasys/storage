// Include the time.h library
#include<time.h>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(int argc, char* argv[])
{
  for(int i = 1; i < 101; i++){
    char *buffer;
    long bSize = 102400;
    int blockSize = 102400;
    long iterations = bSize/blockSize;
  
    buffer = (char*)malloc(bSize);
    memset(buffer, 'x', bSize);
  
    FILE * pFile;
    
    char fName[5];
    //    char buf[5];
    //sprintf(buf, )
    //    char* first = itoa(i, buf, 10);
    //char* second = "-1KB.txt";
    //char* both = malloc(strlen(first) + strlen(second) + 2);

    //sprintf("%s %s", first, second);

    sprintf(fName,"%i" ,i);
    //printf("%s",fName);
    //fName = sprintf("%i", i);

    //fName = i;

    pFile = fopen (fName, "w" );
    fwrite(buffer, blockSize, iterations, pFile);
    fclose(pFile);
  }
}

