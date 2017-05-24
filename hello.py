'''
print("hello python!")

name = "yuxzh"
print(name.title())

print(3/2)



print(bicks)
print(bicks[1])

bicks.insert(1,1)
print(bicks)

bicks.append('f1')
print(bicks)

del bicks[1]
print(bicks)

f1 = bicks.pop()
print(bicks)
print(f1)

d = bicks.pop(3)
print(bicks)
print(d)
bicks.remove('a')
print(bicks)


bicks = ['a','b','c','d','e','f']
newBicks = bicks
newBicksTemp = bicks[:]
bicks.append('aaaa')
print(bicks)
print(newBicks)
print(newBicksTemp)
newBicks.append("bbbb")
print(bicks)
print(newBicks)
print(newBicksTemp)
'''

'''
user = {
    'name' : 'bob',
    'age'  : 16,
}
for k,v in user.items():
    print(k + ':' + str(v))
print(user.keys())

msg = input("hello,da xiong di:")
print(msg)


def pet(petName='dog',petAge=18):
    print('petName==='+petName)
    print('petAge===='+str(petAge))

pet('cat',33)
'''
def build(first,last,**user_info):
    profile = {}
    profile['first_name'] = first
    profile['last'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile

tmp = build('firstname','lastname',location='china',age=18)
print(tmp)
for k,v in tmp.items():
    print(k + "===" + str(v))