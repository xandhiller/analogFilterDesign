#! /usr/bin/python3.7 --

import pandas as pd

# Read in all reasonable e192 vals
df = pd.read_csv('reasonable_e192_vals.csv', delimiter=',')
e192_vals = [float(row[0]) for row in df.values]


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


def subselection_vals(value, possible_vals=e192_vals, search_factor=3):
    # lower and upper indices for the subselection
    lower = 0
    upper = 0
    # Find lower limit
    for i, el in enumerate(possible_vals):
        if value/search_factor > el:
            lower = i
        else:
            break
    # Find upper limit
    for i in range(len(possible_vals)-1, -1, -1):
        if value*search_factor < possible_vals[i]:
            upper = i
        else:
            break
    # Return the subselection
    return possible_vals[lower:upper]


"""
Pass this function a value that you want to satisfy with the E192 range of 
resistors/capacitors, then what impedance calculation to use.
"""
def find_closest_impedance(value, impedance=r_parallel, series='e192'):
    closest_pair = []
    # Create all reasonable e192 vals
    df = pd.read_csv('reasonable_' + series + '_vals.csv', delimiter=',')
    available_vals = [float(row[0]) for row in df.values]

    # Reduce the resistors we look for when trying to find combinations.
    search_space = subselection_vals(value, available_vals)
    for i,el_a in enumerate(search_space):
        for j,el_b in enumerate(search_space):
            if impedance(el_a, el_b) < value:
                closest_pair = [el_a, el_b]
            else:
                resulting_impedance = impedance(closest_pair[0], closest_pair[1])
                impedance_error = 1-abs(resulting_impedance/value)
                return [closest_pair, resulting_impedance, impedance_error] 


def main():
    print(find_closest_impedance(3145, series='e24'))

if __name__ == '__main__':
    main()



