/*
 * Source code adapted from here: https://thinkingandcomputing.com/2014/02/28/using-avx-instructions-in-matrix-multiplication/
 * Adaptation made based on the names available in avxintrin.h and the matrix calculation being made.
 */
#include <iostream>
#include <time.h>
extern "C"
{
#include <immintrin.h>
}

using namespace std;

int main(){
  const int col = 128, row = 24, num_trails = 10000000;

  double w[row][col];
  double x[col];
  double y[row];
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
  cout<<"Time taken: "<<diff<<endl;

  for (int i=0; i<row; i++) {
    cout<<y[i]<<", ";
  }
  cout<<endl;

  __m256d ymm0, ymm1, ymm2, ymm3,
    ymm8, ymm9, ymm10, ymm11;

  t1 = clock();
  const int col_reduced = col - col%32;
  const int col_reduced_32 = col - col%16;
  for (int r = 0; r < num_trails; r++)
    for (int i=0; i<row; i++) {
      double res = 0;
      for (int j=0; j<col_reduced; j+=32) {
        ymm8 = _mm256_loadu_pd(&x[j]);
        ymm9 = _mm256_loadu_pd(&x[j+8]);
        ymm10 = _mm256_loadu_pd(&x[j+16]);
        ymm11 = _mm256_loadu_pd(&x[j+24]);

        ymm0 = _mm256_loadu_pd(&w[i][j]);
        ymm1 = _mm256_loadu_pd(&w[i][j+8]);
        ymm2 = _mm256_loadu_pd(&w[i][j+16]);
        ymm3 = _mm256_loadu_pd(&w[i][j+24]);

        ymm0 = _mm256_mul_pd(ymm0, ymm8 );
        ymm1 = _mm256_mul_pd(ymm1, ymm9 );
        ymm2 = _mm256_mul_pd(ymm2, ymm10);
        ymm3 = _mm256_mul_pd(ymm3, ymm11);

        ymm0 = _mm256_add_pd(ymm0, ymm1);
        ymm2 = _mm256_add_pd(ymm2, ymm3);
        ymm0 = _mm256_add_pd(ymm0, ymm2);

        _mm256_storeu_pd(scratchpad, ymm0);
        for (int k=0; k<4; k++)
          res += scratchpad[k];
      }
      for (int j=col_reduced; j<col_reduced_32; j+=16) {
        ymm8 = _mm256_loadu_pd(&x[j]);
        ymm9 = _mm256_loadu_pd(&x[j+8]);

        ymm0 = _mm256_loadu_pd(&w[i][j]);
        ymm1 = _mm256_loadu_pd(&w[i][j+8]);

        ymm0 = _mm256_mul_pd(ymm0, ymm8 );
        ymm1 = _mm256_mul_pd(ymm1, ymm9 );

        ymm0 = _mm256_add_pd(ymm0, ymm1);

        _mm256_storeu_pd(scratchpad, ymm0);
        for (int k=0; k<4; k++)
          res += scratchpad[k];
      }
      for (int l=col_reduced_32; l<col; l++) {
        res += w[i][l] * x[l];
      }
      y[i] = res;
    }
  t2 = clock();
  diff = (((double)t2 - (double)t1) / CLOCKS_PER_SEC ) * 1000;
  cout<<"Time taken: "<<diff<<endl;

  for (int i=0; i<row; i++) {
    cout<<y[i]<<", ";
  }
  cout<<endl;

  return 0;
}
