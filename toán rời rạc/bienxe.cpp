#include <iostream>
using namespace std;
int main()
{
    for (char letter = 'A'; letter <= 'Z'; letter++)
     for (int j = 0; j < 10; j++) 
      for (int a = 0; a < 10; a++) 
       for (int b = 0; b < 10; b++) 
        for (int c = 0; c < 10; c++) 
          for (int d = 0; d < 10; d++)
             cout<<"29"<<letter<<j<<"-"<<a<<b<<c<<d<<endl;
    return 0;
}


