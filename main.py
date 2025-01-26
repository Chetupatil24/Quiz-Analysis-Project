import requests
import matplotlib.pyplot as plt
import zipfile
import os

# API Endpoints
CURRENT_QUIZ_API = "https://jsonkeeper.com/b/LLQT"
SUBMISSION_DATA_API = "https://api.jsonserve.com/rJvd7g"
QUIZ_ANALYTICS_API = "https://api.jsonserve.com/XgAgFJ"


# Fetch current quiz data (latest quiz submission)
def fetch_current_quiz_data():
    try:
        response = requests.get(CURRENT_QUIZ_API, verify=False)  # Disabling SSL verification
        response.raise_for_status()  # Check if the request was successful
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching current quiz data: {e}")
        return None


# Fetch submission data (historical quiz performance)
def fetch_submission_data():
    try:
        response = requests.get(SUBMISSION_DATA_API, verify=False)  # Disabling SSL verification
        response.raise_for_status()  # Check if the request was successful
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching submission data: {e}")
        return None


# Fetch quiz analytics data (for additional insights)
def fetch_quiz_analytics():
    try:
        response = requests.get(QUIZ_ANALYTICS_API, verify=False)  # Disabling SSL verification
        response.raise_for_status()  # Check if the request was successful
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching quiz analytics data: {e}")
        return None


# Analyze the current quiz data
def analyze_quiz_data(current_quiz_data):
    print("Analyzing current quiz data...")
    # Debugging step: print the structure of current_quiz_data
    print("Current quiz data structure:", current_quiz_data)
    
    # Check if 'questions' key exists and access accordingly
    if 'questions' in current_quiz_data:
        questions = current_quiz_data['questions']
    else:
        print("Error: 'questions' key not found in the current quiz data")
        return {}

    # Example analysis: count number of questions
    num_questions = len(questions)
    print(f"Number of questions in the quiz: {num_questions}")

    # Implement your analysis logic here
    return {'quiz_summary': 'Analysis complete'}


# Analyze the submission data (historical performance)
def analyze_submission_data(submission_data):
    print("Analyzing submission data...")
    # Implement your logic for analyzing submission data
    # For simplicity, return a mock analysis result
    return {'submission_summary': 'Analysis complete'}


# Generate insights based on analysis results
def generate_insights(submission_analysis, quiz_analysis):
    print("Generating insights...")
    weak_areas = {"Math": 2, "Science": 3, "English": 1}  # Example weak areas (Topic: Number of mistakes)
    improvement_trends = {"user_1": 0.75, "user_2": 0.85, "user_3": 0.90}  # Example improvement trend (User: Mean Score)
    return weak_areas, improvement_trends


# Create recommendations based on insights
def create_recommendations(weak_areas, improvement_trends):
    print("Creating recommendations...")
    recommendations = {}
    for topic in weak_areas:
        recommendations[topic] = f"Focus on {topic} to improve."
    
    for user in improvement_trends:
        if improvement_trends[user] < 0.8:
            recommendations[user] = f"Work on practice tests to improve {user}'s score."
        else:
            recommendations[user] = f"{user} is on the right track!"
    
    return recommendations


# Save recommendations to a text file
def save_recommendations_to_file(recommendations, filename="recommendations.txt"):
    with open(filename, 'w') as file:
        for rec in recommendations:
            file.write(f"Recommendation for {rec}: {recommendations[rec]}\n")
    print(f"Recommendations saved to {filename}")


# Visualize performance data (weak areas and improvement trends)
def visualize_performance(weak_areas, improvement_trends, save_images=True):
    """
    Visualize the weak areas and improvement trends for the user and save them as image files.
    """
    # Weak areas visualization (Bar plot for each topic's weak performance)
    topics = list(weak_areas.keys())
    weaknesses = list(weak_areas.values())

    plt.bar(topics, weaknesses)
    plt.xlabel('Topic')
    plt.ylabel('Weakness Frequency')
    plt.title('Weak Areas in Topics')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    if save_images:
        plt.savefig('weak_areas.png')
        print("Weak areas plot saved as weak_areas.png")
    else:
        plt.show()

    # Improvement trend visualization (Scatter plot for user improvement trends)
    users = list(improvement_trends.keys())
    trends = list(improvement_trends.values())

    plt.scatter(users, trends)
    plt.xlabel('User ID')
    plt.ylabel('Improvement Trend (Mean Score)')
    plt.title('User Improvement Trends')
    plt.tight_layout()

    if save_images:
        plt.savefig('improvement_trends.png')
        print("Improvement trends plot saved as improvement_trends.png")
    else:
        plt.show()


# Save all necessary files into a ZIP file for submission
def create_submission_package():
    # Create a ZIP file to store all outputs
    zip_filename = 'submission_package.zip'
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        # Add recommendation text file
        zipf.write('recommendations.txt')
        # Add plots
        zipf.write('weak_areas.png')
        zipf.write('improvement_trends.png')
        print(f"All output files are saved into {zip_filename}")

    # Clean up individual files after zipping
    os.remove('recommendations.txt')
    os.remove('weak_areas.png')
    os.remove('improvement_trends.png')


# Main function to coordinate the workflow
def main():
    # Fetch the data from the APIs
    print("Fetching data...")
    current_quiz_data = fetch_current_quiz_data()
    submission_data = fetch_submission_data()
    quiz_analytics = fetch_quiz_analytics()

    if current_quiz_data and submission_data:
        # Analyze the data
        print("Analyzing data...")
        quiz_analysis = analyze_quiz_data(current_quiz_data)
        submission_analysis = analyze_submission_data(submission_data)
        
        # Generate insights
        print("Analyzing quiz data...")
        weak_areas, improvement_trends = generate_insights(submission_analysis, quiz_analysis)
        
        # Create recommendations
        recommendations = create_recommendations(weak_areas, improvement_trends)
        
        # Print and save recommendations
        for rec in recommendations:
            print(f"Recommendation for {rec}: {recommendations[rec]}")
        
        save_recommendations_to_file(recommendations)
        
        # Visualize results and save images
        print("Generating visualizations...")
        visualize_performance(weak_areas, improvement_trends, save_images=True)

        # Create the submission package
        create_submission_package()

        print("All tasks completed successfully!")


if __name__ == "__main__":
    main()

























