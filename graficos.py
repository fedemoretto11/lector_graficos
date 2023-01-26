import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("topSubscribed.csv")
sns.lineplot(x="Youtube Channel", y="Subscribers", data=df.head(10))
plt.show()