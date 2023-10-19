import csv
a=[]
with open('C:/Users/vostro/Pictures/enjoysport - enjoysport.csv','r') as csvfile:
    for row in csv.reader(csvfile):
        a.append(row)
num_attribute=len(a[0])-1
hypothesis=['0']*num_attribute
for i in range(0,len(a)):
    if a[i][num_attribute]=='yes':
        for j in range(0,num_attribute):
            if hypothesis[j]=='0' or hypothesis[j]==a[i][j]:
                hypothesis[j]=a[i][j]
            else:
                hypothesis[j]='?'
print(hypothesis)
    
