import matplotlib.pyplot as plt
import json

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

def mean_with_length(numbers, length):
    sum = 0
    for i in range(length):
        sum+=numbers[i]
    return sum / max(length,1)


fil = open('data.json', 'r')

data_dict = json.load(fil)

fil.close()
x = list(data_dict.keys())
y = list(data_dict.values())

avg_list = [mean_with_length(y,i) for i in range(len(x))]

print(mean(y))

plt.plot(x,y,'r.', ms = 3)
plt.plot(x,avg_list, lw = 2)
plt.show()
