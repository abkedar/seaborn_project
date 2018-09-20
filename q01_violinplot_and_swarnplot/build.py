# %load q01_violinplot_and_swarnplot/build.py
# Default imports
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.switch_backend('agg')
data = pd.read_csv('data/loan_prediction.csv')
col1 = data['Property_Area']
col2 = data['LoanAmount']
col3 = data['Gender']
def plot(data, c1, c2, c3):
    plt.figure(figsize=(15, 6))
    ax = sns.violinplot(x=col1, y=col2, data=data, hue = col3, split=True, inner= None)
    sns.swarmplot(y=col2, x=col1, data= data, hue = col3,palette='BuGn_r')
    plt.show()
plot(data, col1, col2, col3)






