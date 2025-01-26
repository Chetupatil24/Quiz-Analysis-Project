# Quiz Analysis Project

This project analyzes quiz data to identify weak areas, track user improvement trends, and generate insights and recommendations for better performance. It also generates visualizations and saves the output for easy submission.


## Features
Fetch quiz data and historical performance data from APIs.
Analyze quiz data to identify weak areas and trends.
Generate recommendations for improvement.
Visualize results as bar and scatter plots.
Save outputs (recommendations, plots) as files.
Package all outputs into a single .zip file for submission.


## Requirements
Prerequisites:
1. Python 3.8+
2. Libraries:
            requests
            matplotlib
            zipfile
            os


## How to Run the Project
Clone the repository or copy the files into your project directory.
Ensure the required libraries are installed in your environment.
Run the script:  python main.py


## Outputs Generated
* recommendations.txt: Contains topic-wise and user-specific improvement suggestions.
* weak_areas.png: A bar plot visualizing weak areas based on quiz data.
* improvement_trends.png: A scatter plot showing user improvement trends over time.
* submission_package.zip: A zip file containing all the output files for submission.


## Project Workflow
* Data Fetching:

    * Fetches quiz and submission data from the following APIs:
       * Current Quiz: jsonkeeper.com
       * Submission Data: jsonserve.com
       * Quiz Analytics: jsonserve.com
    * SSL verification is disabled to avoid certificate errors.

* Data Analysis:

    * Analyzes the number of questions in the quiz and     identifies weak areas. 

* Insights and Recommendations:

    * Generates insights for weak topics and user improvement trends.
    * Creates recommendations based on insights.

* Visualization:

    * Generates two plots:
        * Weak Areas: Bar plot of weak topics.
        * mprovement Trends: Scatter plot of user improvement trends.

* Output Packaging:

Saves the recommendations and plots.
Packages all outputs into a single zip file for submission.

## Files in the Repository

    * main.py: Main Python script to fetch, analyze, and generate outputs.
    * README.md: Documentation file (this file).
    * submission_package.zip: Generated zip file containing all output files.


# Example Workflow

    # Run the script
    python main.py

    # Outputs:
    # - recommendations.txt
    # - weak_areas.png
    # - improvement_trends.png
    # - submission_package.zip


## Customization

You can customize:

    * API endpoints (CURRENT_QUIZ_API, SUBMISSION_DATA_API, QUIZ_ANALYTICS_API) in the main.py file.
    * Output file names or directory by modifying the save_recommendations_to_file and visualize_performance functions.# Quiz-Analysis-Project
# Quiz-Analysis-Project
