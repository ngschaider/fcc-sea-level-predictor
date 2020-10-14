import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    """
    Use Pandas to import the data from epa-sea-level.csv.
    """
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")


    """
    Use matplotlib to create a scatter plot using the "Year" column as the x-axis and the "CSIRO Adjusted Sea Level" column as the y-axix.
    """
    # Create scatter plot
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])


    """
    Use the linregress function from scipi.stats to get the slope and y-intercept of the line of best fit. Plot the line of best fit over the top of the scatter plot. Make the line go through the year 2050 to predict the sea level rise in 2050.
    """
    # Create first line of best fit
    slope, intercept, r_value, p_value, stderr = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x = np.linspace(1880, 2050, 2050-1880)
    plt.plot(x, intercept + x * slope, color="red")


    """
    Plot a new line of best fit just using the data from year 2000 through the most recent year in the dataset. Make the line also go through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000.
    """
    # Create second line of best fit
    dfSinceY2K = df[df["Year"] >= 2000]
    slope, intercept, r_value, p_value, stderr = linregress(dfSinceY2K["Year"], dfSinceY2K["CSIRO Adjusted Sea Level"])
    x = np.linspace(1880, 2050, 2050-1880)
    plt.plot(x, intercept + x * slope, color="green")
    
    
    """
    The x label should be "Year", the y label should be "Sea Level (inches)", and the title should be "Rise in Sea Level".
    """
    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()