'''
with open('file.txt') as file_object:
    contents = file_object.read()
    print(contents)

with open('file.txt') as file_object:
    for line in file_object:
        print(line.rstrip())
'''

import json
nums = [1,2,3,4,5,6,7]

with open('jsonfile.json','w') as obj:
    json.dump(nums,obj)

with open('jsonfile.json','r') as obj:
    aa = json.load(obj)
print(aa)