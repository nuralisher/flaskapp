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
  cout << "Random string with length "<<len<< " : \n" << buffer<<endl;
  cout << "Allocated memory size "<<len+1;
  free(buffer);
 
  return 0;
}