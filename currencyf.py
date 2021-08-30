with open("CurrencyRate.txt") as file1:
    lines=file1.readlines()

currencyDict={}
for line in lines:
    passed=line.split("\t")
    currencyDict[passed[0]]=passed[1]

with open("mostfrequentlyused.txt") as file2:
    lines=file2.readlines()

freqDict={}
for line in lines:
    passed=line.split("\t")
    freqDict[passed[0]]=passed[1]

def defaultCal():
    print("\nEnter the Amount")
    try:
        amount=int(input())
        for i in freqDict.keys():
            print(str(amount)+" US Dollor is equal to "+str(amount*float(currencyDict[i]))+" "+str(i))
    except:
        print("\nPlease Enter the amount correctly")

def manualCal():
    print("\nPlease Select the name of currency using only the options Available")
    [print(item)for item in currencyDict.keys()]
    flag=0
    currency1=input("Please Enter which currency you want\n")
    for i in currencyDict.keys():
        if i==currency1:
            flag=1
    if flag==0:
        print("\nPlease Select the currency from the give list")
        return
    flag =0
    currency2=input("Please Enter in which Currency you want to convert\n")
    for i in currencyDict.keys():
        if i==currency2:
            flag=1
    if flag==0:
        print("\nPlease Select the currency from the give list")
        return
    flag =0
    print("\nEnter the Amount")
    try:
        amount=int(input())
        print(str(amount)+" "+str(currency1)+" is equal to "+str(amount*float(currencyDict[currency2])/float(currencyDict[currency1]))+" "+str(currency2))
    except:
        print("\nPlease Enter the amount correctly")

print("\n\t\t\tCURRENCY CALULATOR")
print("\nDo you want Default Currency Calculator or you want manual Currency Calculator\nIn Default mode you will get most frequently used results and it's expected that you have Enter in US Dollar\n")
print("\nPress\n1 for Default Calculator \n2 for Manual Calculator\n")
choice=int(input())
if choice == 1:
    defaultCal()
else:
    manualCal()