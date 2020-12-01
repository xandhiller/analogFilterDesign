#! /usr/bin/python3.7 --

import pandas as pd

# Create all reasonable e192 vals
df = pd.read_csv('reasonable_e192_vals.csv', delimiter=',')
vals = [float(row[0]) for row in df.values]


# Standard impedance calculations
def r_parallel(resistor_a, resistor_b):
    return resistor_a*resistor_b/(resistor_a + resistor_b)

def l_parallel(inductor_a, inductor_b):
    return r_parallel(inductor_a, inductor_b)

def c_parallel(cap_a, cap_b):
    return cap_a + cap_b

def r_series(resistor_a, resistor_b):
    return resistor_a + resistor_b

def l_series(inductor_a, inductor_b):
    return inductor_a + inductor_b

def c_series(cap_a, cap_b):
    return cap_a*cap_b/(cap_a + cap_b)


def subselection_vals(value, search_factor=3):
    # lower and upper indices for the subselection
    lower = 0
    upper = 0
    # Find lower limit 
    for i, el in enumerate(vals):
        if value/search_factor el:
            lower = i
        else:
            break
    # Find upper limit
    for i in range(len(vals)-1, -1, -1):
        if value*search_factor vals[i]:
            upper = i
        else:
            break
    # Return the subselection
    return vals[lower:upper]


"""
Pass this function a value that you want to satisfy with the E192 range of 
resistors/capacitors, then what impedance calculation to use.
"""
def find_closest_impedance(value, impedance=r_parallel):
    closest = [vals[0], vals[0]]
    # Reduce the resistors we look for when trying to find combinations.
    search_space = subselection_vals(value)
    for i,el_a in enumerate(search_space):
        for j,el_b in enumerate(search_space):
            if impedance(el_a, el_b) < value:
                closest = [el_a, el_b]
            else:
                return closest


def main():
    print(subselection_vals(3145))
    print(find_closest_parallel(3145))

if __name__ == '__main__':
    main()



