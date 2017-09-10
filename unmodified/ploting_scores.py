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
pretty_time = time.strftime('%dd:%Hh:%Mm:%Ss', time.gmtime(timer))
days = int(pretty_time.split(':')[0][:2])
days = days-1
pretty_time = str(int(days / 10))+str(int(days %10))+pretty_time[2:]


stable_x = 0
for i in y:
    if i > 750:
        break
    stable_x +=1

stable_x_list = x[stable_x:]
stable_y_list = y[stable_x:]
avg_list_better = [mean_with_length(stable_y_list,i) for i in range(len(stable_y_list))]


print("Timer: ", pretty_time, "\nIterations: ", n, "\nAverage overall: ", mean(y))
print("Average after reached 750: ", mean(stable_y_list),"\nMax: ", max(y))

plt.plot(x,y,'r.', label = 'score', ms = 3)
plt.plot(x,avg_list, lw = 2, label = 'average overall')
plt.plot(stable_x_list, avg_list_better, label = 'average after reached 750', lw = 2, color = 'green')
plt.xlabel('Iterations', fontsize = 15)
plt.ylabel('Score', fontsize = 15)
plt.title('Unmodified', fontsize = 20)
plt.legend(loc = 'upper left')
plt.savefig('Unmodified.png')
plt.show()
