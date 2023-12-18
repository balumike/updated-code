# -*- coding: utf-8 -*-


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import seaborn as sns


def load_time_data(file_path):
    """Load 'Time' data from a CSV file into a pandas DataFrame."""
    df_time = pd.read_csv(file_path)
    return df_time


def plot_covid_cases_over_time(dates, confirmed, released, deceased):
    """Plot COVID-19 cases over time."""
    plt.figure(figsize=(10, 6))

    # Plot 'confirmed' cases
    plt.plot(dates, confirmed, marker='o', linestyle='-', label='Confirmed')

    # Plot 'released' cases
    plt.plot(dates, released, marker='o', linestyle='-', label='Released')

    # Plot 'deceased' cases
    plt.plot(dates, deceased, marker='o', linestyle='-', label='Deceased')

    # Format the date labels
    date_format = DateFormatter("%Y-%m-%d")
    plt.gca().xaxis.set_major_formatter(date_format)

    # Rotate x-axis labels for better visibility
    plt.xticks(rotation=45)

    # Set plot labels and title
    plt.xlabel('Time')
    plt.ylabel('Count')
    plt.title('COVID-19 Cases Over Time')

    # Show a legend
    plt.legend()

    # Show the plot
    plt.grid(True)
    plt.show()


def load_age_data(file_path):
    """Load 'TimeAge' data from a CSV file into a pandas DataFrame."""
    time_age = pd.read_csv(file_path)
    return time_age


def plot_covid_cases_by_age(age_group_data):
    """Plot COVID-19 cases by age group."""
    plt.figure(figsize=(12, 6))

    # Use Seaborn to create a bar plot
    sns.barplot(data=age_group_data, x='age', y='confirmed', color='skyblue', label='Confirmed')
    sns.barplot(data=age_group_data, x='age', y='deceased', color='salmon', label='Deceased')

    plt.xlabel('Age Group')
    plt.ylabel('Number of Cases')
    plt.title('COVID-19 Cases by Age Group')
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()


def load_region_data(file_path):
    """Load 'Region' data from a CSV file into a pandas DataFrame."""
    df_region = pd.read_csv(file_path)
    return df_region


def plot_elderly_population_vs_nursing_home_count(df_region):
    """Plot scatter plot: Elderly Population Ratio vs. Nursing Home Count."""
    plt.figure(figsize=(10, 6))
    plt.scatter(df_region['elderly_population_ratio'], df_region['academy_ratio'], alpha=0.5, color='b')

    plt.xlabel('Elderly Population Ratio')
    plt.ylabel('Nursing Home Count')
    plt.title('Scatter Plot: Elderly Population Ratio vs. Nursing Home Count')

    plt.grid(True)
    plt.show()


def main():
    # Specify the file paths
    time_file_path = r'D:\CBI_Solutions\2023\November\Balu\Time.csv'
    age_file_path = r'D:\CBI_Solutions\2023\November\Balu\TimeAge.csv'
    region_file_path = r'D:\CBI_Solutions\2023\November\Balu\Region.csv'

    # Load and process 'Time' data
    df_time = load_time_data(time_file_path)
    dates = pd.to_datetime(df_time['date'])
    confirmed = df_time['confirmed']
    released = df_time['released']
    deceased = df_time['deceased']

    # Plot COVID-19 cases over time
    plot_covid_cases_over_time(dates, confirmed, released, deceased)

    # Load and process 'TimeAge' data
    age_group_data = load_age_data(age_file_path)
    plot_covid_cases_by_age(age_group_data)

    # Load and process 'Region' data
    df_region = load_region_data(region_file_path)
    plot_elderly_population_vs_nursing_home_count(df_region)


if __name__ == "__main__":
    main()

