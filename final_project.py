"""
Noah Knost, Faith Lee, Angielena Luong
CSE 163 Section AA, AE, AJ

This file consists of methods that take food insecurity data and unemployment
data in the United States in order to create visualizations that help
highlight the correlation between the two issues. This data incorporates
information pertaining to race, gender, and education level and their
relationship to food insecurity and unemployment.
"""
import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def insecurity_vs_unemployment_scatter_plot(df: pd.DataFrame) -> None:
    """
    Paramater - df: pd.DataFrame - contains food insecurity and unemployment
    data
    Plots a scatter plot of food insecurity vs unemployment from 2001 - 2021
    """
    fig = px.scatter(df, x='percent unemployed', y='Food insecure-percent',
                     range_y=[0, 20], range_x=[3,10], trendline="ols",
                     color="Year")
    fig.update_layout(
        xaxis_title="unemployment percentage",
        yaxis_title="food insecurity percentage",
        title="food insecurity vs unemployment from 2001 - 2021"
    )
    fig.write_image('images/insecurity_vs_unemployment_scatter_plot.png',
                    engine='kaleido')


def insecurity_vs_unemployment_with_time_scatter_plot(df: pd.DataFrame) -> None:
    """
    Paramater - df: pd.DataFrame - contains food insecurity and unemployment data
    Plots a scatter plot of food insecurity vs unemployment with respect to
    time from 2001 - 2021 
    """
    trace1 = go.Scatter(x=df['Year'], y=df['percent unemployed'],
                        name='Unemployment Rates')
    trace2 = go.Scatter(x=df['Year'], y=df['Food insecure-percent'],
                        name='Food Insecurity Rates')
    layout = go.Layout(title='Comparison of Food Insecurity and Unemployment '
                       'Rates', xaxis=dict(title='Time'),
                       yaxis=dict(title='Rate'))
    fig = go.Figure(data=[trace1, trace2], layout=layout)
    fig.write_image('images/insecurity_vs_unemployment_with_time_scatter_plot.png', engine='kaleido')


def insecurity_vs_unemployment_with_time_bar_plot(df: pd.DataFrame) -> None:
    """
    Paramater - df: pd.DataFrame - contains food insecurity and unemployment data
    Plots a bar plot of food insecurity vs unemployment with respect to time
    from 2001 - 2021 
    """
    trace1 = go.Bar(x=df['Year'], y=df['percent unemployed'],
                    name='Unemployment Rates')
    trace2 = go.Bar(x=df['Year'], y=df['Food insecure-percent'],
                    name='Food Insecurity Rates')
    layout = go.Layout(title='Comparison of Food Insecurity and '
                       'Unemployment Rates', xaxis=dict(title='Time'),
                       yaxis=dict(title='Rate'), barmode='overlay')
    fig = go.Figure(data=[trace2, trace1], layout=layout)
    fig.write_image('images/insecurity_vs_unemployment_with_time_bar_plot.png',
                    engine='kaleido')


def delta_insecurity_vs_delta_unemployment_with_time_bar_plot(df: pd.DataFrame) -> None:
    """
    Paramater - df: pd.DataFrame - contains food insecurity and unemployment
    data
    Plots a bar plot of the change in food insecurity vs change in
    unemployment with respect to time from 2001 - 2021 
    """
    trace1 = go.Bar(x=df['Year'], y=df['Change_Food_Insecurity'],
                    name='Change in Unemployment Rates')
    trace2 = go.Bar(x=df['Year'], y=df['Change_unemployed'],
                    name='Change in Food Insecurity Rates')
    layout = go.Layout(title='Comparison of change in Food Insecurity and '
                       'Unemployment Rates', xaxis=dict(title='Time'),
                       yaxis=dict(title='Rate'))
    fig = go.Figure(data=[trace2, trace1], layout=layout)
    fig.write_image('images/delta_insecurity_vs_delta_unemployment_with_time_bar_plot.png', engine='kaleido')


def ratio_insecurity_vs_unemployment_with_time_bar_plot(df: pd.DataFrame) -> None:
    """
    Paramater - df: pd.DataFrame - contains food insecurity and unemployment data
    Plots a bar plot of the ratio food insecurity vs unemployment with respect
    to time from 2001 - 2021 
    """
    fig = px.bar(df, x='Year', y='Ratio_Food_Insecurity_Unemployment')
    fig.update_layout(
        xaxis_title="Year",
        yaxis_title="food insecurity percentage over unemployment percentage",
        title="ratio food insecurity vs unemployment with respect to time from 2001 - 2021"
    )
    fig.write_image('images/ratio_insecurity_vs_unemployment_with_time_bar_plot.png', engine='kaleido')


def ratio_insecurity_vs_unemployment_with_time_scatter_plot(df: pd.DataFrame) -> None:
    """
    Paramater - df: pd.DataFrame - contains food insecurity and unemployment data
    Plots a scatter plot of the ratio food insecurity vs unemployment with
    respect to time from 2001 - 2021 
    """
    fig = px.scatter(df, x='Year', y='Ratio_Food_Insecurity_Unemployment')
    fig.update_layout(
        xaxis_title="Year",
        yaxis_title="food insecurity percentage over unemployment percentage",
        title="ratio food insecurity vs unemployment with respect to time from 2001 - 2021"
    )
    fig.write_image('images/ratio_insecurity_vs_unemployment_with_time_scatter_plot.png', engine='kaleido')


def ratio_delta_insecurity_vs_delta_unemployment_with_time_bar_plot(df: pd.DataFrame) -> None:
    """
    Paramater - df: pd.DataFrame - contains food insecurity and unemployment data
    Plots a bar plot of the ratio change in food insecurity vs change in
    unemployment with respect to time from 2001 - 2021 
    """
    fig = px.bar(df, x='Year', y='Ratio_Delta_Food_Insecurity_Unemployment')
    fig.update_layout(
        xaxis_title="Year",
        yaxis_title="change in food insecurity percentage over change in unemployment percentage",
        title="ratio change in food insecurity vs change in unemployment with respect to time from 2001 - 2021"
    )
    fig.write_image('images/ratio_delta_insecurity_vs_delta_unemployment_with_time_bar_plot.png', engine='kaleido')


def unemployment_and_education(unemployment_data: pd.DataFrame) -> None:
    """
    Takes the given unemployment dataframe and creates a multi-line line
    plot showing the unemployment percentage amongst those with high school,
    associate's, and professional degrees in the U.S. from 2010-2020.
    """
    # create line graph
    unemp_and_edu = px.line(unemployment_data, x='Date', y='High_School')

    unemp_and_edu.add_scatter(x=unemployment_data['Date'],
                              y=unemployment_data['High_School'],
                              mode='lines', name='High School Degree')
    unemp_and_edu.add_scatter(x=unemployment_data['Date'],
                              y=unemployment_data['Associates_Degree'],
                              mode='lines', name='Associate\'s Degree')
    unemp_and_edu.add_scatter(x=unemployment_data['Date'],
                              y=unemployment_data['Professional_Degree'],
                              mode='lines', name='Professional Degree')

    unemp_and_edu.update_layout(
        title='Unemployment Rates in the U.S. By Highest Level of Education, '
        '2010-2020', xaxis_title='Year',yaxis_title='Percent Unemployed',
        legend_title='Key'
    )

    unemp_and_edu.write_image('images/unemp_edu.png', engine='kaleido')


def food_insecurity(food_security_data: pd.DataFrame) -> None:
    """
    Takes the given food security dataframe and creates a line plot showing
    the U.S.' food insecurity rates from 2001-2021.
    """
    food_all_households = food_security_data[
                            food_security_data['Category'] == 'All households'
                          ]

    food_insecurity_all_hh = px.line(food_all_households, x='Year',
                                     y='Food insecure-percent')
    food_insecurity_all_hh.update_layout(
        title='Food Insecurity rate in All U.S. Households (2001-2021)',
        xaxis_title='Year',
        yaxis_title='Percent Food Insecure',
        legend_title='Key'
    )

    food_insecurity_all_hh.write_image('images/food_insecurity_all_hh.png',
                                       engine='kaleido')


def unemp_and_food_insecurity(food_security_data: pd.DataFrame,
                              unemployment_data: pd.DataFrame) -> None:
    """
    Takes the given unemployment and food security dataframes and creates a
    multi-line line
    plot showing the unemployment percentage amongst those with high school,
    associate's, and professional degrees as well as the food insecurity rates
    in the U.S. from 2010-2020.
    """
    food_all_households = food_security_data[
                            food_security_data['Category'] == 'All households'
                          ]

    food_all_hh_2010_2020 = food_all_households[
                                (food_all_households['Year'] >= 2010) &
                                (food_all_households['Year'] <= 2020)
                            ]

    # create line graph
    unemp_and_edu = px.line(unemployment_data, x='Date', y='High_School')

    unemp_and_edu.add_scatter(x=unemployment_data['Date'],
                              y=unemployment_data['High_School'],
                              mode='lines', name='High School Degree')
    unemp_and_edu.add_scatter(x=unemployment_data['Date'],
                              y=unemployment_data['Associates_Degree'],
                              mode='lines', name='Associate\'s Degree')
    unemp_and_edu.add_scatter(x=unemployment_data['Date'],
                              y=unemployment_data['Professional_Degree'],
                              mode='lines', name='Professional Degree')
    unemp_and_edu.add_scatter(x=food_all_hh_2010_2020['Year'],
                              y=food_all_hh_2010_2020['Food insecure-percent'],
                              mode='lines', name='Food Insecurity')

    unemp_and_edu.update_layout(
        title='Food Insecurity and Unemployment-by-Education Rates '
        '(2010-2020)',
        xaxis_title='Year', yaxis_title='Percentage', legend_title='Key'
    )

    unemp_and_edu.write_image('images/unemp_food.png', engine='kaleido')


def race_and_unemployment(food_data: pd.DataFrame) -> None:
    """
    Takes dataset food_data and graphs data for each race/ethnicity in the
    dataset and the food insecure-percent from years 2001 - 2021. Graphs four
    separate lines in a single graph for each race/ethnicity and their
    data on food insecurity rates.
    """
    race = food_data['Category'] == 'Race/ethnicity of households'
    white = food_data['Subcategory'] == 'White non-Hispanic'
    black = food_data['Subcategory'] == 'Black non-Hispanic'
    hispanic = food_data['Subcategory'] == 'Hispanic'
    other = food_data['Subcategory'] == 'Other'

    food_data = food_data[['Year', 'Category', 'Subcategory',
                           'Food insecure-percent']]
    result = food_data[race & (white | black | hispanic | other)]
    graph = px.line(result, x='Year', y='Food insecure-percent',
                    color='Subcategory')

    graph.update_layout(
        title='Food Insecurity by Race Over Time',
        xaxis_title='Year',
        yaxis_title='Food Insecure Percent',
        legend_title='Key'
        )

    # graph.show()
    graph.write_image('images/race_and_unemployment.png', engine='kaleido')


def gender_and_food(food_data: pd.DataFrame) -> None:
    """
    This function views how gender impacts food insecurity. A graph shows
    different households according to gender and plots the food insecure
    percent for each of them from the years 2001-2021. Takes food_data
    as a pandas dataframe and returns type None.
    """
    household_composition = food_data['Category'] == 'Household composition'
    women_1 = food_data['Sub-subcategory'] == 'Female head, no spouse'
    women_2 = food_data['Sub-subcategory'] == 'Women living alone'
    men_1 = food_data['Sub-subcategory'] == 'Male head, no spouse'
    men_2 = food_data['Sub-subcategory'] == 'Men living alone'
    food_data = food_data[['Year', 'Category', 'Sub-subcategory',
                           'Food insecure-percent']]
    result = food_data[(women_1 | women_2 | men_1 | men_2) &
                       household_composition]

    graph = px.line(result, x='Year', y='Food insecure-percent',
                    color='Sub-subcategory')
    graph.update_layout(
        title='Food Insecurity by Gender Over Time',
        xaxis_title='Year',
        yaxis_title='Food Insecure Percent',
        legend_title='Key'
        )
    graph.write_image('images/gender_and_food.png', engine='kaleido')


def race_percent_change(food_data: pd.DataFrame) -> pd.DataFrame:
    """
    Aims to answer: "Which race had the biggest percent change in food insecure
    rates from pre-covid to post covid?" Shows the differences in each race and
    potential impact of COVID-19 upon each. Takes food_data as a pandas
    dataframe and returns a pandas dataframe with information on the percent
    change in food insecurity rates for each race/ethnicity.
    """
    food_data = food_data[['Year', 'Category', 'Subcategory',
                           'Food insecure-percent']]
    race = food_data[food_data['Category'] == 'Race/ethnicity of households']
    race = race[['Year', 'Subcategory', 'Food insecure-percent']]

    race = race.pivot(index='Subcategory', columns='Year',
                      values='Food insecure-percent')
    race['Percent Change'] = (race[2021] - race[2019]) / race[2019] * 100
    race.index.name = 'Race/Ethnicity'
    race.columns.name = None


def main():
    food_security_all_households: pd.DataFrame = pd.read_csv("food_security/Food security, all households_2021.csv")
    unemployment_data: pd.DataFrame = pd.read_csv('unemployment/unemployment_data_us.csv')

    # reformat and sort df by date
    unemployment_data['Date'] = pd.to_datetime(unemployment_data['Date'],
                                               format='%b-%Y')
    sorted_unemp = unemployment_data.sort_values('Date')

    # creates graph of unemployment by education
    unemployment_and_education(sorted_unemp)

    # creates graph of food insecurity rates
    food_insecurity(food_security_all_households)

    # creates graph of unemployment and food insecurity with correlation
    unemp_and_food_insecurity(food_security_all_households, sorted_unemp)

    """
    Explores the correlation between unemployment and food insecurity rates in
    the United States
    """
    food_insecurity_df: pd.DataFrame = pd.read_csv("food_security/Food security, all households_2021.csv")
    food_insecurity_df = food_insecurity_df[food_insecurity_df['Category'] ==
                                            'All households']
    unemployment_df = pd.read_csv('unemployment/unemployment-Sheet1.csv')
    unemployment_df = unemployment_df.rename(columns={'year': 'Year'})
    combined_df = food_insecurity_df.merge(unemployment_df, on="Year")
    combined_df['Change_Food_Insecurity'] = combined_df['Food insecure-percent'].pct_change()
    combined_df['Change_unemployed'] = combined_df['percent unemployed'].pct_change()
    combined_df = combined_df.reset_index()
    combined_df['Ratio_Food_Insecurity_Unemployment'] = combined_df['Food insecure-percent'] / combined_df['percent unemployed']
    combined_df['Ratio_Delta_Food_Insecurity_Unemployment'] = combined_df['Change_Food_Insecurity'] / combined_df['Change_unemployed']
    insecurity_vs_unemployment_scatter_plot(combined_df)
    insecurity_vs_unemployment_with_time_scatter_plot(combined_df)
    insecurity_vs_unemployment_with_time_bar_plot(combined_df)
    delta_insecurity_vs_delta_unemployment_with_time_bar_plot(combined_df)
    ratio_insecurity_vs_unemployment_with_time_bar_plot(combined_df)
    ratio_insecurity_vs_unemployment_with_time_scatter_plot(combined_df)
    ratio_delta_insecurity_vs_delta_unemployment_with_time_bar_plot(combined_df)

    insecurity_vs_unemployment_scatter_plot_test()
    insecurity_vs_unemployment_with_time_scatter_plot_test()
    insecurity_vs_unemployment_with_time_bar_plot_test()
    delta_insecurity_vs_delta_unemployment_with_time_bar_plot_test()
    ratio_insecurity_vs_unemployment_with_time_bar_plot_test()
    ratio_insecurity_vs_unemployment_with_time_scatter_plot_test()
    ratio_delta_insecurity_vs_delta_unemployment_with_time_bar_plot_test()
    race_and_unemployment_test()
    gender_and_food_test()
    unemployment_and_education_test()
    food_insecurity_test()
    unemp_and_food_insecurity_test()

    food_data: pd.DataFrame = pd.read_csv("food_security/Food security, all households_2021.csv")
    race_and_unemployment(food_data)
    gender_and_food(food_data)
    race_percent_change(food_data)


def insecurity_vs_unemployment_scatter_plot_test() -> None:
    """
    Tests to make sure that the insecurity_vs_unemployment_scatter_plot
    function has an output graph file.
    """
    file_path = "images/insecurity_vs_unemployment_scatter_plot.png"
    if os.path.exists(file_path):
        print("The file exists.")
    else:
        print("The file does not exist. " + file_path)


def insecurity_vs_unemployment_with_time_scatter_plot_test() -> None:
    """
    Tests to make sure that the insecurity_vs_unemployment_with_time_scatter_
    plot function has an output graph file.
    """
    file_path = "images/insecurity_vs_unemployment_with_time_scatter_plot.png"
    if os.path.exists(file_path):
        print("The file exists.")
    else:
        print("The file does not exist. " + file_path)


def insecurity_vs_unemployment_with_time_bar_plot_test() -> None:
    """
    Tests to make sure that the insecurity_vs_unemployment_with_time_bar_plot
    function has an output graph file.
    """
    file_path = "images/insecurity_vs_unemployment_with_time_bar_plot.png"
    if os.path.exists(file_path):
        print("The file exists.")
    else:
        print("The file does not exist." + file_path)


def delta_insecurity_vs_delta_unemployment_with_time_bar_plot_test() -> None:
    """
    Tests to make sure that the delta_insecurity_vs_delta_unemployment_with_
    time_bar_plot function has an output graph file.
    """
    file_path = "images/delta_insecurity_vs_delta_unemployment_with_time_bar_plot.png"
    if os.path.exists(file_path):
        print("The file exists.")
    else:
        print("The file does not exist. " + file_path)


def ratio_insecurity_vs_unemployment_with_time_bar_plot_test() -> None:
    """
    Tests to make sure that the ratio_insecurity_vs_unemployment_with_time_bar
    _plot_test function has an output graph file.
    """
    file_path = "images/ratio_insecurity_vs_unemployment_with_time_bar_plot.png"
    if os.path.exists(file_path):
        print("The file exists.")
    else:
        print("The file does not exist." + file_path)


def ratio_insecurity_vs_unemployment_with_time_scatter_plot_test() -> None:
    """
    Tests to make sure that the ratio_insecurity_vs_unemployment_with_time_
    scatter_plot function has an output graph file.
    """
    file_path = "images/ratio_insecurity_vs_unemployment_with_time_scatter_plot.png"
    if os.path.exists(file_path):
        print("The file exists.")
    else:
        print("The file does not exist. " + file_path)


def ratio_delta_insecurity_vs_delta_unemployment_with_time_bar_plot_test() -> None:
    """
    Tests to make sure that the ratio_delta_insecurity_vs_delta_unemployment_
    with_time_bar_plot function has an output graph file.
    """
    file_path = "images/ratio_delta_insecurity_vs_delta_unemployment_with_time_bar_plot.png"
    if os.path.exists(file_path):
        print("The file exists.")
    else:
        print("The file does not exist. " + file_path)


def race_and_unemployment_test() -> None:
    """
    Tests to make sure that the race_and_employment function has an output
    graph file.
    """
    file_path = "images/race_and_unemployment.png"
    if os.path.exists(file_path):
        print("The file exists.")
    else:
        print("The file does not exist. " + file_path)


def gender_and_food_test() -> None:
    """
    Tests to make sure that the gender_and_food
    function has an output graph file.
    """
    file_path = "images/gender_and_food.png"
    if os.path.exists(file_path):
        print("The file exists.")
    else:
        print("The file does not exist. " + file_path)


def unemployment_and_education_test() -> None:
    """
    Tests to make sure that the unemployment_and_education function has an
    output graph file.
    """
    file_path = "images/unemp_edu.png"
    if os.path.exists(file_path):
        print("The file exists.")
    else:
        print("The file does not exist. " + file_path)


def food_insecurity_test() -> None:
    """
    Tests to make sure that the food_insecurity function has an output graph
    file.
    """
    file_path = "images/food_insecurity_all_hh.png"
    if os.path.exists(file_path):
        print("The file exists.")
    else:
        print("The file does not exist. " + file_path)


def unemp_and_food_insecurity_test() -> None:
    """
    Tests to make sure that the unemp_and_food_insecurity function has an
    output graph file.
    """
    file_path = "images/unemp_food.png"
    if os.path.exists(file_path):
        print("The file exists.")
    else:
        print("The file does not exist. " + file_path)


if __name__ == "__main__":
    main()