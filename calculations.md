# Python interpreter output of Bandpass function.
>>> import analogFilterDesign as afd
>>> Q0, w01, w02, q, n = afd.BP(0, 10, 0.8, 1884.955592, 18849.555922, 628.318507, 56548.667765)
>>> Q0
0.7397708923012121
>>> w01
28658.66975281337
>>> w02
1239.7845450730542
>>> q
0.3513641844403705
>>> n
2

# Putting in the prototype values into the scaling function
>>> R1 = 1
>>> R2 = 4*pow(Q0,2)
>>> R2
2.189043892384526
>>> C1 = 0.5*Q0
>>> C2 = C1
>>> C1
0.36988544615060603

# Desigining using the prototype friend circuit.
# Using two friend circuits with the same Q0 but different w0's, as suggested.

# First filter: w01 = 28658.66975281337
>>> afd.flexibleScaling()
Enter number of resistors in the filter: 2
Enter number of capacitors in the filter: 2
Enter the value of R1: 1
Enter the value of R2: 2.189043892384526
Enter the value of C1: 0.36988544615060603
Enter the value of C2: 0.36988544615060603
Enter the current w0 of the filter: 1
Enter the desired w0 of the filter: 28658.66975281337
CONSTRAINTS:
C1: 	12.90658112679131039762650292	< Km <	2581316.225358262079525300584
C2: 	12.90658112679131039762650292	< Km <	2581316.225358262079525300584
R1: 	1E+3	                        < Km <	1E+5
R2: 	456.8204426959661265905265499	< Km <	45682.04426959661265905265499
NET CONSTRAINTS:
        1E+3	                        < Km <	45682.04426959661265905265499

# Second filter: w02 = 1239.7845450730542
>>> afd.flexibleScaling()
Enter number of resistors in the filter: 2
Enter number of capacitors in the filter: 2
Enter the value of R1: 1
Enter the value of R2: 2.189043892384526
Enter the value of C1: 0.36988544615060603
Enter the value of C2: 0.36988544615060603
Enter the current w0 of the filter: 1
Enter the desired w0 of the filter: 1239.7845450730542
CONSTRAINTS:
C1: 	298.3465535366958145204330779	< Km <	59669310.70733916290408661557
C2: 	298.3465535366958145204330779	< Km <	59669310.70733916290408661557
R1: 	1E+3	                        < Km <	1E+5
R2: 	456.8204426959661265905265499	< Km <	45682.04426959661265905265499
NET CONSTRAINTS:
        1E+3	                        < Km <	45682.04426959661265905265499
