import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

#must pip install imports
def show_trends():
    df = pd.read_csv("Task4a_data.csv")
    
    average_GBP_USD = round((df['GBP - USD'].mean()), 2)
    print('The average conversion rate for GBP - USD is: ',average_GBP_USD)
    print('')
    average_USD_GBP = round((df['USD - GBP'].mean()), 2)
    print('The average conversion rate for GBP - USD is: ',average_USD_GBP)

    x = df['GBP - USD']
    y = df.index=df['Date']

    stats = linregress(x, y)

    m = stats.slope
    b = stats.intercept

    # Change the default figure size
    plt.figure(figsize=(10,10))

    # Change the default marker for the scatter from circles to x's
    plt.scatter(x, y, marker='x')

    # Set the linewidth on the regression line to 3px
    plt.plot(x, m * x + b, color="red", linewidth=3)

    # Add x and y lables, and set their font size
    plt.xlabel("x", fontsize=20)
    plt.ylabel("Date", fontsize=20)

    # Set the font size of the number lables on the axes
    plt.xticks(fontsize=18)
    plt.yticks(fontsize=18)

    plt.show()

show_trends()
