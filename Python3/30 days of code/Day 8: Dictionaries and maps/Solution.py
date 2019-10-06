#Task
'''Given n names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. You will then be given an unknown number of names to query your phone book for. For each name queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; if an entry for name is not found, print Not found instead'''
#Solution
n= int(input())
phonebook={}
for i in range(n):
    d=input().split()
    phonebook[d[0]]= d[1]

while True:
    try:   
        for j in range(n):
            name=str(input())
            if name in phonebook:
                print(str(name)+ "=" +str(phonebook[name]))
            else:
                print("Not found")
    except: break
