# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import math

import numpy as np
import csv

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

#df = pd.read_csv('D:\\dataset2.csv',engine='python', sep=';', on_bad_lines='skip'  )
#output = np.zeros(shape=(df.shape[0], 221))
#for i in range(0, df.shape[0]):
#    data=df.values[i][0:241]#
#
#    temp= np.append(calc_entropy(data)[0:-20], data[-1])
#    output[i] = temp
#    print(str(round(i/df.shape[0]*100, 2)) + "%")
#
#dataFrame = pd.DataFrame(output)
#dataFrame.to_csv("output2.csv")
#print(df.values[0])
results0_r = []
results1_r=[]
results2_r=[]
with open('D:\\1_detector\\results\\output_result.csv') as results1_f:
    results1 = csv.reader(results1_f, delimiter=',')
    for row in results1:
        results1_r.append(row)
with open('D:\\2_detector\\results\\output_result.csv') as results2_f:
    results2 = csv.reader(results2_f, delimiter=',')
    for row in results2:
        results2_r.append(row)
with open('D:\\0_detector\\results\\output_result.csv') as results0_f:
    results0 = csv.reader(results0_f, delimiter=',')
    for row in results0:
        results0_r.append(row)
for i in range(1, len(results0_r)):
    first0 = np.array(results0_r[i][439-1:439+219-1]).astype(float)
    second0 = np.array(results0_r[i][439+219-1:439+438-1]).astype(float)
    first1 = np.array(results1_r[i][439-1:439+219-1]).astype(float)
    second1 = np.array(results1_r[i][439+219-1:439+438-1]).astype(float)
    first2 = np.array(results2_r[i][439-1:439+219-1]).astype(float)
    second2 = np.array(results2_r[i][439+219-1:439+438-1]).astype(float)

    firstEtalon = np.array(results0_r[i][1-1:220-1]).astype(float)
    secondEtalon = np.array(results0_r[i][220-1:439-1]).astype(float)

    error0 = np.square(np.subtract(first0, firstEtalon)).mean() + np.square(np.subtract(second0, secondEtalon)).mean()/0.088
    error1 = np.square(np.subtract(first1, firstEtalon)).mean() + np.square(np.subtract(second1, secondEtalon)).mean()/0.056
    error2 = np.square(np.subtract(first2, firstEtalon)).mean() + np.square(np.subtract(second2, secondEtalon)).mean()/0.080
    errors = [error0,error1,error2]
    max_item = min(errors)
    print(f'{errors.index(max_item)}')


