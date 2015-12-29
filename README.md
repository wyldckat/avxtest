avxtest
=======
This simple repository is for testing AVX capabilities with GCC. The source code is based on the one provided here: https://thinkingandcomputing.com/2014/02/28/using-avx-instructions-in-matrix-multiplication/ - which seems to have been originally authored by (Yifei Teng)[https://github.com/tengyifei/], namely the code in the file `avxtest.cpp`.

The code in this repository was further changed to give formatted results with more precision and at the end is shown the differences in the results.

The file `avxtest64.cpp` was adapted from `avxtest.cpp` to do double precision operations, instead of doing single precision operations.

Author of these changes: Bruno Santos, namely wyldckat@github.


Compiling
=========
Simply run:

    g++ -O3 -mavx avxtest.cpp -o avxtest
    g++ -O3 -mavx avxtest64.cpp -o avxtest64


Example output
==============

These results were obtained with an AMD A10-7850K. Notice that since it's a 64-bit processor, it takes roughly the same time to do the operations with standard x86/x86_64 FPU, versus the results achieved with AVX, where it takes roughly twice as long to the operations with AVX and double precision.

avxtest
-------

    Time taken (ms): 44478.285156
    46.645702362, 54.693763733, 52.523517609, 46.882259369, 47.732662201, 53.505905151, 44.757362366, 53.78931427, 50.922969818, 47.973320007, 50.980171204, 51.735042572, 57.411094666, 50.251522064, 48.735942841, 50.678451538, 54.797599792, 52.394363403, 49.601345062, 48.174781799, 51.200325012, 43.908599854, 49.559474945, 48.012435913, 

    Time taken (ms): 6253.0961914
    46.645690918, 54.693771362, 52.523513794, 46.882263184, 47.732650757, 53.505893707, 44.757354736, 53.789325714, 50.922950745, 47.973320007, 50.980171204, 51.735046387, 57.41109848, 50.251529694, 48.735939026, 50.678451538, 54.797599792, 52.394359589, 49.601318359, 48.174793243, 51.200325012, 43.908607483, 49.55947876, 48.012435913, 

        Without AVX  |    With AVX      |   Difference
        46.645702362 |     46.645690918 | 1.1444091797e-05
        54.693763733 |     54.693771362 | -7.6293945312e-06
        52.523517609 |     52.523513794 | 3.8146972656e-06
        46.882259369 |     46.882263184 | -3.8146972656e-06
        47.732662201 |     47.732650757 | 1.1444091797e-05
        53.505905151 |     53.505893707 | 1.1444091797e-05
        44.757362366 |     44.757354736 | 7.6293945312e-06
        53.78931427  |     53.789325714 | -1.1444091797e-05
        50.922969818 |     50.922950745 | 1.9073486328e-05
        47.973320007 |     47.973320007 |                0
        50.980171204 |     50.980171204 |                0
        51.735042572 |     51.735046387 | -3.8146972656e-06
        57.411094666 |      57.41109848 | -3.8146972656e-06
        50.251522064 |     50.251529694 | -7.6293945312e-06
        48.735942841 |     48.735939026 | 3.8146972656e-06
        50.678451538 |     50.678451538 |                0
        54.797599792 |     54.797599792 |                0
        52.394363403 |     52.394359589 | 3.8146972656e-06
        49.601345062 |     49.601318359 | 2.6702880859e-05
        48.174781799 |     48.174793243 | -1.1444091797e-05
        51.200325012 |     51.200325012 |                0
        43.908599854 |     43.908607483 | -7.6293945312e-06
        49.559474945 |      49.55947876 | -3.8146972656e-06
        48.012435913 |     48.012435913 |                0


avxtest64
---------

    Time taken (ms): 44543.2169999999969
    46.6456921874999821, 54.6937718749999746, 52.5235124999999954, 46.8822578125000149, 47.7326531249999988, 53.5058921874999882, 44.7573531250000158, 53.7893234374999736, 50.9229515625000033, 47.9733187499999971, 50.9801671874999798, 51.735049999999994, 57.4110968749999913, 50.2515296874999891, 48.7359359374999883, 50.6784578124999712, 54.7975999999999956, 52.3943593750000289, 49.6013171875000296, 48.174790625, 51.2003234374999892, 43.9086031250000275, 49.5594781250000054, 48.012434374999998, 

    Time taken (ms): 13095.6270000000004
    46.6456921874999821, 54.6937718749999746, 52.5235124999999954, 46.8822578125000149, 47.7326531249999988, 53.5058921874999882, 44.7573531250000158, 53.7893234374999736, 50.9229515625000033, 47.9733187499999971, 50.9801671874999798, 51.735049999999994, 57.4110968749999913, 50.2515296874999891, 48.7359359374999883, 50.6784578124999712, 54.7975999999999956, 52.3943593750000289, 49.6013171875000296, 48.174790625, 51.2003234374999892, 43.9086031250000275, 49.5594781250000054, 48.012434374999998, 

          Without AVX     |       With AVX         |      Difference
      46.6456921874999821 |    46.6456921875000035 | -2.13162820728030056e-14
      54.6937718749999746 |     54.693771875000003 | -2.84217094304040074e-14
      52.5235124999999954 |    52.5235125000000025 | -7.10542735760100186e-15
      46.8822578125000149 |    46.8822578124999865 | 2.84217094304040074e-14
      47.7326531249999988 |    47.7326531250000059 | -7.10542735760100186e-15
      53.5058921874999882 |    53.5058921875000024 | -1.42108547152020037e-14
      44.7573531250000158 |    44.7573531250000016 | 1.42108547152020037e-14
      53.7893234374999736 |     53.789323437500002 | -2.84217094304040074e-14
      50.9229515625000033 |    50.9229515624999962 | 7.10542735760100186e-15
      47.9733187499999971 |    47.9733187499999971 |                      0
      50.9801671874999798 |    50.9801671875000011 | -2.13162820728030056e-14
       51.735049999999994 |    51.7350500000000011 | -7.10542735760100186e-15
      57.4110968749999913 |    57.4110968749999984 | -7.10542735760100186e-15
      50.2515296874999891 |    50.2515296874999962 | -7.10542735760100186e-15
      48.7359359374999883 |    48.7359359375000025 | -1.42108547152020037e-14
      50.6784578124999712 |    50.6784578124999925 | -2.13162820728030056e-14
      54.7975999999999956 |     54.797600000000017 | -2.13162820728030056e-14
      52.3943593750000289 |    52.3943593749999863 | 4.26325641456060112e-14
      49.6013171875000296 |    49.6013171875000012 | 2.84217094304040074e-14
             48.174790625 |    48.1747906250000071 | -7.10542735760100186e-15
      51.2003234374999892 |    51.2003234375000105 | -2.13162820728030056e-14
      43.9086031250000275 |    43.9086031249999991 | 2.84217094304040074e-14
      49.5594781250000054 |    49.5594781250000125 | -7.10542735760100186e-15
       48.012434374999998 |     48.012434374999998 |                      0
