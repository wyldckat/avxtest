/*
 * Original source code from here: https://thinkingandcomputing.com/2014/02/28/using-avx-instructions-in-matrix-multiplication/
 * Formatting changes and removed AVX extensions by wyldckat@github.
 */
#include <iostream>
#include <iomanip>
#include <time.h>
#include <cstdlib>

using namespace std;

int main(){
  const int col = 128, row = 24, num_trails = 10000000;

  float w[row][col];
  float x[col];
  float y[row];
  float yb[row];
  float scratchpad[8];
  for (int i=0; i<row; i++) {
    for (int j=0; j<col; j++) {
      w[i][j]=(float)(rand()%1000)/800.0f;
    }
  }
  for (int j=0; j<col; j++) {
    x[j]=(float)(rand()%1000)/800.0f;
  }

  clock_t t1, t2;

  cout<<setprecision(11);

  t1 = clock();
  for (int r = 0; r < num_trails; r++)
    for(int j = 0; j < row; j++)
    {
      float sum = 0;
      float *wj = w[j];

      for(int i = 0; i < col; i++)
        sum += wj[i] * x[i];

      y[j] = sum;
    }
  t2 = clock();
  float diff = (((float)t2 - (float)t1) / CLOCKS_PER_SEC ) * 1000;
  cout<<"Time taken (ms): "<<diff<<endl;

  for (int i=0; i<row; i++) {
    cout<<y[i]<<", ";
  }
  cout<<endl<<endl;

  return 0;
}
