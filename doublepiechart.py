label1=['A','B','C','D','E']
value1=[23,67,33,44,22]

labal2=['a','b','c','d','e']
value2=[34,6,73,42,7]

plt.figure(figsize=(10,10))

plt.pie(value1,labels=label1,autopct='%1.0f%%',radius=1.5,wedgeprops={'edgecolor':"black"})
plt.pie(value2,labels=labal2,autopct='%1.0f%%',radius=0.8,wedgeprops={'edgecolor':"black"})
plt.show()
