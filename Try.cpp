#include <iostream>
#include <cstdlib>
using namespace std;
int main()
{
  int len;
  cin >> len;
 
  char * buffer = (char*) malloc(len + 1);

  if (buffer==NULL) exit (1);

  for (int ix = 0; ix < len; ix++)
    buffer[ix] = rand() % 26 + 'a';

  buffer[len]='\0';
  cout << "Случайная строка с длиной "<<len<< " : \n" << buffer;
  free(buffer);
 
  return 0;
}