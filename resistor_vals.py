#! /usr/bin/python3.7 --

import pandas as pd

# Create all reasonable e192 vals
df = pd.read_csv('reasonable_e192_vals.csv', delimiter=',')
vals = [float(row[0]) for row in df.values]


def parallel(resistor_a, resistor_b):
    return resistor_a*resistor_b/(resistor_a + resistor_b)


def subselection_vals(value):
    # lower and upper indices for the subselection
    lower = 0
    upper = 0
    # Find lower limit 
    for i, el in enumerate(vals):
        if value/3 > el:
            lower = i
        else:
            break
    # Find upper limit
    for i in range(len(vals)-1, -1, -1):
        if value*3 < vals[i]:
            upper = i
        else:
            break
    # Return the subselection
    return vals[lower:upper]


def find_closest_parallel(value):
    closest = [vals[0], vals[0]]
    # Reduce the resistors we look for when trying to find combinations.
    search_space = subselection_vals(value)
    for i,el_a in enumerate(search_space):
        for j,el_b in enumerate(search_space):
            if parallel(el_a, el_b) < value:
                closest = [el_a, el_b]
            else:
                return closest


def main():
    print(subselection_vals(3145))
    print(find_closest_parallel(3145))

if __name__ == '__main__':
    main()



