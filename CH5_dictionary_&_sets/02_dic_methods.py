myDict = {
   "key": "value",
   "shivam":"code",
   "score" : "100",
   "marks": [1,2,9],
   "anotherDict": {'shivam' : 'smart'},
   1:2
}

print(myDict.keys()) #print the keys

print(myDict.items()) #update the value of keys
myDict.update({'score':'200'})
print(myDict)

print(myDict.get("shivam")) #gets the vale of the key 



