import csv
from collections import Counter

with open("data.csv", newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
weight = []
total_weight = 0

for i in range(len(file_data)):
    n_number = file_data[i][2]
    weight.append(float(n_number))
    total_weight += weight[i]

weight.sort()

def mean():
    n = len(weight)
    total = 0

    for x in weight:
        total += x
    
    mean = total / n
    
    print("Mean/Average of the weights are " + str(mean))

def median():
    n = len(weight)
    
    if n % 2 == 0:
        median1 = float(weight[n // 2])
        median2 = float(weight[n // 2 - 1])
        median = (median1 + median2) / 2
    else:
        median = weight[n // 2]
        print(n)
    
    print("Median is " + str(median))

def mode():
    data = Counter(weight)
    mode_data_for_range = {
        "75-85": 0,
        "85-95": 0,
        "95-105": 0,
        "105-115": 0,
        "115-125": 0,
        "125-135": 0,
        "135-145": 0,
        "145-155": 0,
        "155-165": 0,
        "165-175": 0
    }
    
    for Weight, occurance in data.items():
        if 75 < float(Weight) < 85:
            mode_data_for_range["75-85"] += occurance
            
        if 85 < float(Weight) < 95:
            mode_data_for_range["85-95"] += occurance
            
        if 95 < float(Weight) < 105:
            mode_data_for_range["95-105"] += occurance
            
        if 105 < float(Weight) < 115:
            mode_data_for_range["105-115"] += occurance
            
        if 115 < float(Weight) < 125:
            mode_data_for_range["115-125"] += occurance
            
        if 125 < float(Weight) < 135:
            mode_data_for_range["125-135"] += occurance
            
        if 135 < float(Weight) < 145:
            mode_data_for_range["135-145"] += occurance
            
        if 145 < float(Weight) < 155:
            mode_data_for_range["145-155"] += occurance
            
        if 155 < float(Weight) < 165:
            mode_data_for_range["155-165"] += occurance
            
        if 165 < float(Weight) < 175:
            mode_data_for_range["165-175"] += occurance
    
    mode_range, mode_occurence = 0, 0
    for range, occurence in mode_data_for_range.items():
        if occurence > mode_occurence:
            mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
    mode = float((mode_range[0] + mode_range[1]) / 2)
    print("The mode is: " + mode)