import json
#merges two json files with scores
#script opens files named:  data_old.json, data_new.json

data_old = open('data_old.json', 'r')
data_new = open('data_new.json', 'r')

data_old_dict = json.load(data_old)
data_new_dict = json.load(data_new)

data_old.close()
data_new.close()

y = list(data_new_dict.values())
n = len(data_old_dict)

counter = 0
for i in y:
    data_old_dict[n+counter] = i
    counter+=1

data_merged = open('data.json', 'w')
json.dump(data_old_dict, data_merged)
data_merged.close()
