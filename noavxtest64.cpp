/*
 * Source code adapted from here: https://thinkingandcomputing.com/2014/02/28/using-avx-instructions-in-matrix-multiplication/
 * Done by wyldckat@github:
 *  - Adaptation made based on the names available in avxintrin.h and the matrix calculation being made, so that it would do double precision math, instead of only float.
 *  - Formatting changes.
 */
#include <iostream>
#include <iomanip>
#include <time.h>
#include <cstdlib>

using namespace std;

int main(){
  const int col = 128, row = 24, num_trails = 10000000;

  double w[row][col];
  double x[col];
  double y[row];
  double yb[row];
  double scratchpad[4];
  for (int i=0; i<row; i++) {
    for (int j=0; j<col; j++) {
      w[i][j]=(double)(rand()%1000)/800.0;
    }
  }
  for (int j=0; j<col; j++) {
    x[j]=(double)(rand()%1000)/800.0;
  }

  clock_t t1, t2;
  
  cout<<setprecision(18);

  t1 = clock();
  for (int r = 0; r < num_trails; r++)
    for(int j = 0; j < row; j++)
    {
      double sum = 0;
      double *wj = w[j];

      for(int i = 0; i < col; i++)
        sum += wj[i] * x[i];

      y[j] = sum;
    }
  t2 = clock();
  double diff = (((double)t2 - (double)t1) / CLOCKS_PER_SEC ) * 1000;
  cout<<"Time taken (ms): "<<diff<<endl;

  for (int i=0; i<row; i++) {
    cout<<y[i]<<", ";
  }
  cout<<endl<<endl;
  
  return 0;
}
