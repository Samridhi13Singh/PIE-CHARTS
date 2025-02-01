import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('population.csv')

df=data.head()

print(df)

country=df['Country']
print(country)
pop = df['Population']

plt.figure(figsize=(9,6))

plt.pie(pop,labels=country,autopct='%1.1f%%',startangle=100,wedgeprops={'edgecolor':"black",'linewidth':3})
plt.title("Population v/s Country")
plt.show()
