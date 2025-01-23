import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def predict_sea_level():
    """Функція для прогнозування рівня моря до 2050 року."""
    df = pd.read_csv('epa-sea-level.csv')

    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = range(1880, 2051)
    plt.plot(years_extended, [slope * year + intercept for year in years_extended], label='Best Fit Line (1880-2014)', color='blue')

    df_2000_onwards = df[df['Year'] >= 2000]
    slope_2000, intercept_2000, _, _, _ = linregress(df_2000_onwards['Year'], df_2000_onwards['CSIRO Adjusted Sea Level'])
    plt.plot(years_extended, [slope_2000 * year + intercept_2000 for year in years_extended], label='Best Fit Line (2000-2014)', color='red')

    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    plt.legend()

    plt.tight_layout()
    return plt
