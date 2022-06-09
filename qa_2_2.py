demodict = {}

demodict["hello"] = 1

print(demodict)
list1 = [1,2,3,45,65]

demodict["hi"] = list1
demodict["hello"] = demodict.get("hello", 0) + 1
demodict["hello"] = demodict.get("hello", 0) + 1
demodict["hello"] = demodict.get("hello", 0) + 1

print(demodict.get("bb",0))

print(demodict)
