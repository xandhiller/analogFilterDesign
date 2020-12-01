#! /usr/bin/python3.7 --

import pandas as pd


def generate():
    nbs = ['192', '96', '48', '24', '12', '6', '3']
    for nb in nbs:
        print(nb)
        # Create all reasonable e192 e192_vals
        source_filename = 'e' + nb + '_vals_per_decade.csv'
        df = pd.read_csv(source_filename, delimiter=',')
        e192_vals = [float(row[0]) for row in df.values]
        output_filename = 'reasonable_e' + nb + '_vals.csv'
        f = open(output_filename, 'w')
        f.write('vals,\n')
        for i in range(-12, 10, 1):
            for val in e192_vals:
                f.write(str(val*10**i) + ',\n')
        f.close()


def main():
    generate()

if __name__ == '__main__':
    main()
