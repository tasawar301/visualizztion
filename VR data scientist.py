import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
ds_salaries = pd.read_csv('ds_salaries.csv')

# Mapping of experience levels to their full forms
experience_level_full_form = {
    'EN': 'Entry-level',
    'MI': 'Mid-level',
    'SE': 'Senior-level',
    'EX': 'Executive'
}

# Applying the full form mapping to the dataset
ds_salaries['experience_level_full'] = ds_salaries['experience_level'].map(experience_level_full_form)

# Function to create a box plot with full form experience levels
def create_box_plot_with_full_experience(df, x, y, title, xlabel, ylabel):
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x=x, y=y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)  # Rotate x labels for better readability
    plt.show()

# Function to create a scatter plot with a specified color palette and legend
def create_scatter_plot(df, x, y, title, xlabel, ylabel, palette, legend_title):
    plt.figure(figsize=(10, 6))
    scatter_plot = sns.scatterplot(data=df, x=x, y=y, palette=palette)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    unique_values = len(df[x].unique())
    if unique_values <= 10:
        plt.legend(title=legend_title)
    else:
        scatter_plot.legend_.remove()
    plt.show()

# Function to create a histogram with title and labels
def create_histogram(df, column, title, xlabel, ylabel, bins):
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column], bins=bins, kde=False)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

# Function to create a line plot for trends over time with title and labels
def create_trend_line_plot(df, x, y, title, xlabel, ylabel, marker_style):
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df, x=x, y=y, marker=marker_style)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

# Create the box plot with full form experience levels
create_box_plot_with_full_experience(
    df=ds_salaries,
    x='experience_level_full',
    y='salary_in_usd',
    title='Salary Distribution Across Different Experience Levels',
    xlabel='Experience Level',
    ylabel='Salary in USD'
)

# Create the scatter plot with a specified color palette and legend
create_scatter_plot(
    df=ds_salaries,
    x='experience_level',  # Replace with the correct column name
    y='salary_in_usd',
    title='Salary vs. Numeric Experience Level',
    xlabel='Numeric Experience Level',
    ylabel='Salary in USD',
    palette='coolwarm',
    legend_title='Experience Level'
)

# Create the histogram with title and labels
create_histogram(
    df=ds_salaries,
    column='salary_in_usd',
    title='Distribution of Salaries in Data Science',
    xlabel='Salary in USD',
    ylabel='Frequency',
    bins=30
)

# Calculate the average salary by work year
average_salary_by_year = ds_salaries.groupby('work_year')['salary_in_usd'].mean().reset_index()

# Create the line plot for the average salary trend over the years with title and labels
create_trend_line_plot(
    df=average_salary_by_year,
    x='work_year',
    y='salary_in_usd',
    title='Average Salary Trend in Data Science (2020-2023)',
    xlabel='Year',
    ylabel='Average Salary in USD',
    marker_style='o'
)
