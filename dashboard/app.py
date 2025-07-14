import pandas as pd
import dash
from dash import html, dcc
import plotly.express as px
import datetime


# load the dataset from EDA notebook source
df = pd.read_csv('./data/hr_data_more.csv')

# Calculate Tenure in years
df['Tenure'] = (pd.to_datetime('today') - pd.to_datetime(df['DateofHire'])).dt.days / 365

# Gender Distribution by Department (Histogram)
fig_hist = px.histogram(df, x='Department', color='Sex', title='Gender Distribution by Department')

# Employee Status Distribution (Pie)
fig_pie = px.pie(df, names='EmploymentStatus', title='Employee Status Distribution')

# Average Salary by Department (Bar)
fig_bar = px.bar(df.groupby('Department', as_index=False).mean(numeric_only=True), 
                 x='Department', y='Salary', title='Average Salary by Department')

# Salary Distribution by Gender (Box)
fig_box = px.box(df, x='Sex', y='Salary', title='Salary Distribution by Gender')

# Correlation Heatmap for Numeric HR Variables
num_df = df[['Salary', 'Absences', 'EngagementSurvey', 'EmpSatisfaction']]
corr_matrix = num_df.corr()
fig_heatmap = px.imshow(
    corr_matrix,
    text_auto=True,
    color_continuous_scale="RdBu",
    title="Correlation Between Numeric HR Variables"
)

# Scatter plot: EngagementSurvey vs EmpSatisfaction
fig_scatter = px.scatter(
    df, x='EngagementSurvey', y='EmpSatisfaction', color='Sex',
    title='Engagement Survey vs Employee Satisfaction',
    hover_data=['Department', 'PerformanceScore']
)

# Attrition rate by department (Termd/Total)
attrition_df = df.groupby('Department').agg(
    total=('EmpID', 'count'),
    resigned=('Termd', 'sum')
)
attrition_df['attrition_rate'] = attrition_df['resigned'] / attrition_df['total'] * 100
fig_attrition = px.bar(
    attrition_df.reset_index(),
    x='Department', y='attrition_rate',
    title='Attrition Rate by Department',
    labels={'attrition_rate': 'Attrition Rate (%)'}
)

# Violin plot: Salary distribution by Department and Gender
fig_violin = px.violin(df, x='Department', y='Salary', color='Sex', box=True, points='all',
                       title='Salary Distribution by Department and Gender')

# Bar chart: Average Engagement Survey by Department
engagement_df = df.groupby('Department', as_index=False)['EngagementSurvey'].mean()
fig_engagement = px.bar(engagement_df, x='Department', y='EngagementSurvey',
                        title='Average Engagement Survey Score by Department')

# Pie chart: Marital Status Distribution
fig_marital = px.pie(df, names='MaritalDesc', title='Marital Status Distribution')

# Histogram: Absences
fig_absences = px.histogram(df, x='Absences', nbins=20, title='Absences Distribution')

# Box plot: Engagement Survey by Employment Status
fig_engage_status = px.box(df, x='EmploymentStatus', y='EngagementSurvey', color='EmploymentStatus',
                           title='Engagement Survey by Employment Status')

# Engagement vs Performance (Scatter)
fig_engage_perf = px.scatter(
    df, x='EngagementSurvey', y='PerformanceScore', color='Department',
    title='Engagement vs Performance Score',
    hover_data=['Sex', 'Salary']
)

# Tenure vs ManagerRating (Scatter)
fig_tenure_manager = px.scatter(
    df, x='Tenure', y='ManagerRating', color='Department',
    title='Tenure vs Manager Rating',
    hover_data=['Sex', 'Salary']
)

# Workload distribution by Department (Bar)
if 'Workload' in df.columns:
    workload_df = df.groupby('Department', as_index=False)['Workload'].mean()
    fig_workload = px.bar(workload_df, x='Department', y='Workload', title='Average Workload by Department')
else:
    fig_workload = None

# Turnover rate by Department (Bar)
turnover_df = df.groupby('Department').agg(
    total=('EmpID', 'count'),
    turnover=('Termd', 'sum')
)
turnover_df['turnover_rate'] = turnover_df['turnover'] / turnover_df['total'] * 100
fig_turnover = px.bar(
    turnover_df.reset_index(),
    x='Department', y='turnover_rate',
    title='Turnover Rate by Department',
    labels={'turnover_rate': 'Turnover Rate (%)'}
)

# start the dashboard
app = dash.Dash(__name__)
app.layout = html.Div(children=[
    html.H1(children='HR Dashboard'),
    dcc.Graph(figure=fig_hist),
    dcc.Graph(figure=fig_pie),
    dcc.Graph(figure=fig_bar),
    dcc.Graph(figure=fig_box),
    dcc.Graph(figure=fig_heatmap),
    dcc.Graph(figure=fig_scatter),
    dcc.Graph(figure=fig_attrition),
    dcc.Graph(figure=fig_violin),
    dcc.Graph(figure=fig_engagement),
    dcc.Graph(figure=fig_marital),
    dcc.Graph(figure=fig_absences),
    dcc.Graph(figure=fig_engage_status),
    dcc.Graph(figure=fig_engage_perf),
    dcc.Graph(figure=fig_tenure_manager),
    dcc.Graph(figure=fig_turnover),
] + ([dcc.Graph(figure=fig_workload)] if fig_workload else []))

if __name__ == '__main__':
    app.run(debug=True)