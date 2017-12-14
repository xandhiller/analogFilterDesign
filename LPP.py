# Aiming to make a program that does the calculation for the low-pass prototype
import math
import logging

# Logging config:
logging.basicConfig(level=logging.DEBUG, format= ' %(asctime)s - %(levelname)s - %(message)s')

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
    n, Omega0 = LPP(K0, Ks, Kp, OmegaP, OmegaS)
    print("Omega0 is: " + str(Omega0))
    print("n is: " + str(n))



## w0 = Specified cutoff freq, bw = bandwidth = w02-w01
#def bandpassLPP(w0, bw, w1, w2, w3, w4):

#    return ?

def HP(K0, Ks, Kp, OmegaS, OmegaP, w0):
    # Recall that for the bandpass LPP transformation, the transform is S = OmegaP / s = OmegaP / Omega. If you need to refresh your memort it's on pg3.14-3.16 of the Analog Electronics notes

    # Check if conditions satisfied for use of the bandpass transformation
    if (math.ceil(math.sqrt(w1*w2)) != math.ceil(math.sqrt(w3*w4))):
        print(
        "The criteria for a bandpass transformation into the LPP is not satisfied.",
        "\nPlease reconsider your choices for w1, w2, w3 and w4 and make sure they satisfy the criterion:",
        "\nw0 = sqrt(w1*w2) & w0 = sqrt(w3*w4)"
        )

    # Calculate Ωp
    OmegaP = 
    
    return  

def runHP():
     


def main():
    print()

if __name__ == "__main__":
    main()
