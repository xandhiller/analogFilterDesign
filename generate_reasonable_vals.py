#! /usr/bin/python3.7 --
import pandas as pd

# Create all reasonable e192 e192_vals
df = pd.read_csv('e192_vals_per_decade.csv', delimiter=',')
e192_vals = [float(row[0]) for row in df.values]

def main():
    f = open('reasonable_e192_vals.csv', 'w')
    f.write('vals,\n')
    for i in range(-12, 10, 1):
        for val in e192_vals:
            f.write(str(val*10**i) + ',\n')
    f.close()



if __name__ == '__main__':
    main()
