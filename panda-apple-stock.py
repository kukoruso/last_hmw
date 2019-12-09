from matplotlib import pylab as plt
import pandas as pd

pd.plotting.register_matplotlib_converters()

df1 = pd.read_csv("AAPL.csv")
print(df1.head())
df1['last_hmw'] = pd.to_datetime(df1.Date)
# print(df1.head())

df2 = pd.read_excel("ATVI.csv")
print(df2)
df2['last_hmw'] = pd.to_datetime(df2.date)
indexes = []
for date2 in df2.Date:
    for index, date1 in enumerate(df1.Date):
        if date2 == date1:
            indexes.append(index)


mean = df1["Close"].mean()

df3 = pd.read_csv("SNE.csv")
df3['last_hmw'] = pd.to_datetime(df3.Date)


'''
ax = df1.plot(x="Date", y="Close", style='r-', linewidth=0.6, label="Stock price, mean="+str(mean), title="Apple stock vs Iphone launch date", figsize=(17, 9))
df1.plot(x="Date", y="Close", style='-o', ms=7, markevery=indexes, linewidth=0, ax=ax, label="Iphone launch date")
plt.xlabel("Dates")
'''
plt.figure("Apple Stock")
plt.plot(df1["last_hmw"], df1["Close"], 'r-', linewidth=0.6, label="APPL Stock price, mean="+str(mean))
plt.plot(df1["last_hmw"], df1["Close"], '-o', ms=7, markevery=indexes, linewidth=0, label="Iphone launch date")
plt.plot(df3["last_hmw"], df3["Close"], 'b-', linewidth=1, label="Facebook")
plt.xlabel("last_hmw")
plt.legend(loc="upper left")





plt.show()