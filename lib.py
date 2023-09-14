# import numpy as np # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import plotly.express as px

plt.style.use("seaborn-dark-palette")
plt.style.use("dark_background")


def loadData(path):
    data = pd.read_csv(path)
    return data


def nanInfo(data):
    return data.isna().sum()


def describeData(data):
    return data.describe().T


def preprocessData(data):

    # inorder to remove all the null values
    data.dropna(inplace=True)
    # change the datatype of the column
    data["No of student"] = data["No of student"].str.replace(",", "").astype(int)
    # conver object into numerical
    data["International Student"] = data["International Student"].str.replace("%", " ")
    data["International Student"] = pd.to_numeric(
        data["International Student"], errors="coerce"
    )
    data["International Student"] = data["International Student"] / 100

    data.columns = data.columns.str.strip()

    # split the male and female ratio column
    data[["Female", "Male"]] = (
        data["Female:Male Ratio"].str.split(":", expand=True).astype(int)
    )

    # remove the original column from the dataset
    data.drop(columns=["Female:Male Ratio"], inplace=True)


## Visualization
def plotLocTrend(data):
    # group by on basis of location column
    monthly_trends = data.groupby("Location")["No of student"].sum().reset_index()

    # creation of lineplot
    fig_monthly_trends = px.line(
        monthly_trends,  # DataFrame containing the data
        x="Location",  # x-values: job titles
        y="No of student",  # y-values: sum of salaries
        labels={"job_title": "Job"},  # Customize label for the x-axis
        title="Number of Students Trends by Location",  # Set the title of the plot
        height=800,  # Set the height of the plot
    )

    # show the plot
    fig_monthly_trends.show()


def plotLocDistribution(data):
    top10_job_title = data["Location"].value_counts()[:10]
    # creation of bar plot
    fig = px.bar(
        y=top10_job_title.values,
        x=top10_job_title.index,
        color=top10_job_title.index,
        color_discrete_sequence=px.colors.sequential.PuBuGn,
        # Set color palette
        text=top10_job_title.values,
        title="Top 10 Location ",
        template="plotly_dark",
    )

    # Update the layout of the plot
    fig.update_layout(
        title_text="Distribution of location",
        height=650,
        xaxis_title="location",
        yaxis_title="Count",
        font=dict(size=17, family="Franklin Gothic"),
    )

    # Display the plot
    fig.show()


def plotStudentLocDistribution(data):
    fig = px.bar(data, x="Location", y="No of student")

    # Update the layout of the plot
    fig.update_layout(
        title_text="Number of Studnet Distribution with location",
        # Set the title of the plot
        height=650,  # Set the height of the plot
        xaxis_title="Location",  # Label for the x-axis
        yaxis_title="Number of Students",  # Label for the y-axis
        font=dict(size=17, family="Franklin Gothic")
        # Set the font size and family for the text
    )

    # Display the plot
    fig.show()


def plotStudentSalaryDistribution(data):
    top5_salary = data["No of student"].sort_values(ascending=False).head(5)

    # bar blot for the no of student
    fig = px.bar(
        y=top5_salary.values,  # y-values: top 5 salaries
        x=top5_salary.index,  # x-values: indices of the top 5 salaries
        color=top5_salary.index,  # Color the bars based on the indices
        color_discrete_sequence=px.colors.sequential.PuBuGn,
        # Set color palette
        text=top5_salary.values,  # Display the salary values on top of the bars
        title="Top 5 Number of students",  # Set the title of the plot
        template="plotly_dark",  # Use a dark template for the plot
    )

    # Update the layout of the plot
    fig.update_layout(
        title_text="Number of students Distribution",
        height=650,
        xaxis_title="Number of students",  # Label for the x-axis
        yaxis_title="Count",  # Label for the y-axis
        font=dict(size=17, family="Franklin Gothic")
        # Set the font size and family for the text
    )

    # Display the plot
    fig.show()
