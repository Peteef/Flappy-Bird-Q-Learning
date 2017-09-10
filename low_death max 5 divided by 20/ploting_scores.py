import matplotlib.pyplot as plt
import json
import time

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

n = len(x)

timer = n * 1.5
timer += sum(y)*0.6
pretty_time = time.strftime('%d:%H:%M:%S', time.gmtime(timer))
days = int(pretty_time.split(':')[0])
days = days-1
pretty_time = str(int(days / 10))+str(int(days %10))+pretty_time[2:]


print("Timer: ", pretty_time, "\nIterations: ", n, "\nAverage score: ", mean(y), )


plt.plot(x,y,'r.', label = 'score', ms = 3)
plt.plot(x,avg_list, lw = 2, label = 'average')
plt.xlabel('Iterations', fontsize = 15)
plt.ylabel('Score', fontsize = 15)
plt.title('Low death max 5 div 20', fontsize = 20)
plt.legend(loc = 'upper left')
plt.savefig('Low death max 5 div 20' + '.png')
plt.show()
