
# Employee Engagement Analytics Dashboard

## Overview

Employee Engagement Analytics is a comprehensive dashboard for HR professionals to visualize, analyze, and gain actionable insights from employee data. The dashboard leverages Python, Dash, and Plotly to deliver interactive charts and advanced analytics, supporting data-driven decisions in workforce management.

## Features

- Gender distribution by department
- Employee status and attrition analysis
- Salary and performance analytics
- Engagement and satisfaction metrics
- Advanced insights: tenure, manager ratings, workload, turnover
- Correlation heatmaps and custom visualizations

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/reissboafo/employee-engagement-analytics.git
   cd employee-engagement-analytics
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare your data**
   - Place your HR data CSV files in the `data/` directory.
   - Ensure column names match those expected by the dashboard (see sample files).

4. **Run the dashboard**
   ```bash
   cd dashboard
   python app.py
   ```
   - Access the dashboard at `http://localhost:8050`

## Usage

- Explore interactive charts for key HR metrics.
- Filter and compare departments, employee statuses, and engagement scores.
- Use the dashboard to identify trends, risks, and opportunities for improving employee engagement.

## File Structure

- `dashboard/app.py` - Main dashboard application
- `data/` - HR data files (CSV)
- `notebooks/` - Jupyter notebooks for exploratory data analysis
- `README.md` - Project documentation

## License

This project is licensed under the MIT License.

## Contact

For questions or support, please contact [Reiss Boafo](mailto:reissboafo@live.com).