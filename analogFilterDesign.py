# Aiming to make a program that does the calculation for the low-pass prototype
import math
import logging

# Logging config:
logging.basicConfig(level=logging.CRITICAL, format= ' %(asctime)s - %(levelname)s - %(message)s')

# LPP = "Low Pass Prototype"
def LP(K0, Ks, Kp, OmegaP, OmegaS):
    logging.debug("Start of LPP:")

    # Calculate M
    M = math.sqrt( (math.pow(10, 0.1*Ks)-1) / (math.pow(10, 0.1*Kp)-1)  )  
    logging.debug("M is: " + str(M))
    logging.debug("ln(M) = " + str(math.log(M)))    
 
    # Calculate Ωs
    freqRatio = float(OmegaS)/float(OmegaP)
    logging.debug("freqRatio is: " + str(freqRatio))   
    logging.debug("ln(freqRatio) = " + str(math.log(freqRatio)))

    # Calculate n
    n = math.ceil( math.log(M) / math.log(freqRatio) )
    logging.debug("n is: " + str(n))

    # Calculate Omega0p
    Omega0p = float(OmegaP) / ( math.pow((math.pow(10, 0.1*Kp)-1), 1/(2*n)))
    logging.debug("Omega0p is: " + str(Omega0p))    

    # Calculate Omega0s
    Omega0s = float(OmegaS) / ( math.pow((math.pow(10, 0.1*Ks)-1), 1/(2*n)))
    logging.debug("Omega0s is: " + str(Omega0s))    

    # Calculate Omega0
    Omega0 = math.sqrt(Omega0p*Omega0s) 
    logging.debug("Omega0 is: " + str(Omega0))    

    return n, Omega0

def runLP():
    K0 = float(input("Enter K0: "))
    Ks = float(input("Enter Ks: "))
    Kp = float(input("Enter Kp: "))
    OmegaP = float(input("Enter OmegaP: "))
    OmegaS = float(input("Enter OmegaS: "))
    n, Omega0 = LP(K0, Ks, Kp, OmegaP, OmegaS)
    print("Omega0 is: " + str(Omega0))
    print("n is: " + str(n))



def HP(K0, Ks, Kp, ws, wp):
    # ws and wp = not transformed, OmegaP and OmegaS are the transformed versions used in the LPP.
    
    # Calculate Ωp, recall that the transform for a HP is Ω = wp/w, and Ωp is s.t. w = wp
    OmegaP = float(wp) / float(wp)

    # Calculate Ωs, the transform is Ω = wp/w, and Ωs is s.t. w = ws
    OmegaS = float(wp) / float(ws)

    # Chuck it all into the LPP
    n, Omega0 = LP(K0, Ks, Kp, OmegaP, OmegaS) 
    
    # Omega0 is the non-transformed version. Needs to be subbed back into the transform. 
    w0 = float(wp) / float(Omega0)

    # Warning about n, extra hand calculation required.
    print(
        "\nWARNING:"
        "\nExtra hand calulcation required. The n returned here is used s.t.:"
        "\nT(s) = (s^n) / (A polynomial of s of order n)" 
        "\nE.g. if n = 5, because S = 1/s then when transforming the transfer function from LPP to HP, we get:"
        "\n\n\t\ts^5\t\t"
        "\nT(s) = -------------------------"
        "\n\t(s^2+s+1)(s^2+s+1)(s+1)\n"
        "\nIf this is confusing, please refer to page 3.19 of the Anaolg Electronics Notes"
        "\n"
        )

    return n, w0


def runHP():
    print(
        "NOTE:"
        "\nRecall that with the Highpass filter that wp and ws are in different positions on the",
        "x-axis than the lowpass filter. ws comes first and then wp.\n"
        )

    K0 = float(input("Enter K0: "))
    Ks = float(input("Enter Ks: "))
    Kp = float(input("Enter Kp: "))
    wp = float(input("Enter wp: "))
    ws = float(input("Enter ws: "))
    n, w0 = HP(K0, Ks, Kp, wp, ws)
    logging.debug("w0 is: " + str(w0))
    logging.debug("n is: " + str(n))
    
    

def geffeAlgorithm(Omega0, q, QLP):
    # Algorithm is listed on page 3.31 of the Analog Electronics Notes

    D = Omega0 / (QLP*q)

    E = 4 + math.pow(Omega0/q, 2)

    G = math.sqrt( math.pow(E,2) - 4*math.pow(D,2)  )

    Q0 = (1/D)*math.sqrt((1/2)*(E+G))

    K = D*Q0/2

    W = K + math.sqrt(math.pow(K,2)-1)

    return W, Q0
    
def BP(K0, Ks, Kp, w1, w2, w3, w4):
    # Recall that for the bandpass LPP transformation, the transform is S = (1/bw)(1/s)(s^2 + w0^2) 

    # Check if conditions satisfied for use of the bandpass transformation
    if (math.ceil(math.sqrt(w1*w2)) != math.ceil(math.sqrt(w3*w4))):
        print(
        "The criteria for a bandpass transformation into the LPP is not satisfied.",
        "\nPlease reconsider your choices for w1, w2, w3 and w4 and make sure they satisfy the criterion:",
        "\n\tw0 = sqrt(w1*w2) \t& \tw0 = sqrt(w3*w4)"
        )
        exit
    # Hence if the conditions are met, then Ω = (w^2-w0^2)(1/w)(1/[w2-w1])
    
    # OmegaP = 1 because when w = w2, Ω = 1. If confused, please consult Analog Electronics Notes pg 3.26 
    OmegaP = 1
    
    # OmegaS is equal to this equation by the working shown on page 3.26 of the Analog Electronics Notes 
    OmegaS = ( float(w4) - float(w3) ) / ( float(w2) - float(w1) )

    # Calculate w0
    w0 = math.sqrt(w1*w2)

    # Calulcate bandwidth (bw), also sometimes written as ß
    bw = w2 - w1

    # Calculate q
    q = w0 / bw

    # Run the LPP calculation and save the outputs
    n, Omega0 = LP(K0, Ks, Kp, OmegaP, OmegaS)
 
    # Going to assume that QLP = 1 as per the calculations in pg 3.36, seems as though this is the standard output of the LPP, but I'm not sure.    
    QLP = 1 

    # Get the conversion factor so that we can have two different circuits with the same Q0 but different cutoff frequencies.
    W, Q0 = geffeAlgorithm(Omega0, q, QLP)

    # Can now have two cascaded circuits with different w0's but the same Q0's.

    # Centre frequency of the first circuit
    w01 = W*w0

    # Centre frequency of the second circuit
    w02 = (1/W)*w0

    return Q0, w01, w02, q, n


def runBP():
    K0 = float(input("Enter K0: "))
    Ks = float(input("Enter Ks: "))
    Kp = float(input("Enter Kp: "))
    w1 = float(input("Enter w1: "))
    w2 = float(input("Enter w2: "))
    w3 = float(input("Enter w3: "))
    w4 = float(input("Enter w4: "))
    Q0, w01, w02, q, n = BP(K0, Ks, Kp, w1, w2, w3, w4) #TODO: Outputs of this function may change
    logging.debug("Q0 is: " + str(Q0))
    logging.debug("w01: " + str(w01))
    logging.debug("w02 is: " + str(w02))
    logging.debug("q is: " + str(q))
    logging.debug("n is: " + str(n))

def printQ0():
    Q0 = {2: (0.707), 3: (1.00), 4: (0.541, 1.307), 5: (0.618, 1.618), 6: (0.518, 0.707, 1.932), 7: (0.555, 0.802, 2.247), 8: (0.510, 0.601, 0.900, 2.563), 9: (0.532, 0.653, 1.000, 2.879), 10: (0.506, 0.561, 0.707, 1.101, 3.196)}
    # Print out the values neatly
    print("n", end='\t')
    for i in range(0, len(Q0)-1):
        print(str(Q0[i]), end="\t")
        
    
 
def main():
    print()
    #TODO: Insert a switch statement between all possible functionalities, allowing users to select each function that they want.

if __name__ == "__main__":
    main()
