import sys
import pandas as pd
import numpy as np
import os

def main():
    if len(sys.argv) != 5:
        print("Usage: python topsis.py <InputFile> <Weights> <Impacts> <OutputFile>")
        sys.exit(1)

    input_file = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    output_file = sys.argv[4]

    if not os.path.exists(input_file):
        print("Error: Input file not found")
        sys.exit(1)

    try:
        if input_file.endswith('.xlsx'):
            data = pd.read_excel(input_file)
        else:
            data = pd.read_csv(input_file)
    except:
        print("Error: Unable to read input file")
        sys.exit(1)

    if data.shape[1] < 3:
        print("Error: Input file must contain at least 3 columns")
        sys.exit(1)

    try:
        weights = list(map(float, weights.split(',')))
        impacts = impacts.split(',')
    except:
        print("Error: Weights and impacts must be comma separated")
        sys.exit(1)

    if len(weights) != len(impacts) or len(weights) != data.shape[1] - 1:
        print("Error: Number of weights, impacts and columns must be same")
        sys.exit(1)

    for i in impacts:
        if i not in ['+', '-']:
            print("Error: Impacts must be + or -")
            sys.exit(1)

    try:
        matrix = data.iloc[:, 1:].astype(float)
    except:
        print("Error: Non-numeric values found")
        sys.exit(1)

    norm = np.sqrt((matrix ** 2).sum())
    normalized = matrix / norm
    weighted = normalized * weights

    ideal_best = []
    ideal_worst = []

    for i in range(len(impacts)):
        if impacts[i] == '+':
            ideal_best.append(weighted.iloc[:, i].max())
            ideal_worst.append(weighted.iloc[:, i].min())
        else:
            ideal_best.append(weighted.iloc[:, i].min())
            ideal_worst.append(weighted.iloc[:, i].max())

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    dist_best = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    score = dist_worst / (dist_best + dist_worst)

    data['Topsis Score'] = score
    data['Rank'] = data['Topsis Score'].rank(ascending=False).astype(int)

    data.to_csv(output_file, index=False)
    print("TOPSIS completed successfully!")

if __name__ == "__main__":
    main()
