# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import csv
import math

import pandas
import numpy as np

def print_hi(name):
    with open('dataset_final.csv', 'w') as f:
        with open('dataset_test.csv') as csvfile:
            i = 0
            spamreader = csv.reader(csvfile, delimiter=';')
            writer = csv.writer(f)
            df = pandas.DataFrame()
            row_count = sum(1 for row in spamreader)
            csvfile.seek(0)
            for row in spamreader:
                i=i+1

                first = row[5][1:-1].split(', ')
                second = row[6][1:-1].split(', ')
                id=row[0]

                if len(first)!=len(second) or not len(first)==240:
                    continue
                #print(len(calc_entropy(first)))
                arr = [id] + calc_entropy(first)[0:-20] + calc_entropy(second)[0:-20]



                #print(', '.join(row))

                writer.writerow(arr)
                print(i * 100 / row_count)

def calc_entropy(arr):
    grad = []
    entropies = []
    arr = np.array(arr).astype(float)
    for i in range(0, len(arr)-1):
        delta = arr[i+1]-arr[i]
        smooth_grad = math.atan2(delta, 1)/math.pi
        grad.append(smooth_grad)

    for i in range(0, len(grad)):
        window = grad[i:i+10]
        window.sort()
        densities = list()
        for j in range(0, len(window)-1):
            if window[j+1]-window[j] == 0:
                density = 1
            else:
                density = 1/(window[j+1]-window[j])
            densities.append(density*math.log(density))
        entropy = sum(densities)
        if(entropy>0):
            entropies.append(math.log10(entropy))
        else:
            entropies.append(0)
    return entropies


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
