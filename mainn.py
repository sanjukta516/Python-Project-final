import pandas as pd
import numpy as np
from student_record import StudentRecord

# Read student data
data = pd.read_csv("student_data.csv")

# Calculate basic statistics
total_students = len(data)
average_hours = np.mean(data["study_hours"])
average_score = np.mean(data["assessment_score"])
highest_score = np.max(data["assessment_score"])
lowest_score = np.min(data["assessment_score"])

# Function to calculate grades
def calculate_grade(score):
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"

# Add a grade column
data["grade"] = data["assessment_score"].apply(calculate_grade)

# Display results
print("===== STUDENT PERFORMANCE DASHBOARD =====")
print("Total students:", total_students)
print("Average study hours:", round(average_hours, 2))
print("Average assessment score:", round(average_score, 2))
print("Highest score:", highest_score)
print("Lowest score:", lowest_score)

print("\n===== STUDENT GRADES =====")
print(data[["student_id", "assessment_score", "grade"]])
# Course-wise analysis using Pandas

print("\n===== COURSE-WISE ANALYSIS =====")

course_summary = data.groupby("course").agg(
    total_students=("student_id", "count"),
    average_study_hours=("study_hours", "mean"),
    average_score=("assessment_score", "mean"),
    highest_score=("assessment_score", "max"),
    lowest_score=("assessment_score", "min")
)

course_summary["average_study_hours"] = (
    course_summary["average_study_hours"].round(2)
)

course_summary["average_score"] = (
    course_summary["average_score"].round(2)
)

print(course_summary)
import matplotlib.pyplot as plt
import os

# Create a folder to store graphs
os.makedirs("graphs", exist_ok=True)

# Scatter plot
plt.figure(figsize=(8, 5))

plt.scatter(
    data["study_hours"],
    data["assessment_score"]
)

plt.title("Study Hours vs Assessment Scores")
plt.xlabel("Study Hours")
plt.ylabel("Assessment Score")
plt.grid(True)

plt.tight_layout()
plt.savefig("graphs/study_hours_vs_scores.png")
plt.show()
# Histogram of assessment scores
plt.figure(figsize=(8, 5))

plt.hist(
    data["assessment_score"],
    bins=7,
    edgecolor="black"
)

plt.title("Distribution of Assessment Scores")
plt.xlabel("Assessment Score")
plt.ylabel("Number of Students")

plt.tight_layout()
plt.savefig("graphs/score_histogram.png")
plt.show()
# Data validation and outlier analysis

print("\n===== DATA QUALITY CHECK =====")

# Check missing values
print("\nMissing values in each column:")
print(data.isnull().sum())

# Check duplicate records
print("\nDuplicate rows:", data.duplicated().sum())

# Check invalid values
invalid_hours = ((data["study_hours"] < 0) |
                 (data["study_hours"] > 24)).sum()

invalid_scores = ((data["assessment_score"] < 0) |
                  (data["assessment_score"] > 100)).sum()

print("Invalid study-hour records:", invalid_hours)
print("Invalid assessment scores:", invalid_scores)

# Detect possible score outliers using IQR
q1 = data["assessment_score"].quantile(0.25)
q3 = data["assessment_score"].quantile(0.75)

iqr = q3 - q1

lower_limit = q1 - 1.5 * iqr
upper_limit = q3 + 1.5 * iqr

outliers = data[
    (data["assessment_score"] < lower_limit) |
    (data["assessment_score"] > upper_limit)
]

print("\nPossible score outliers:")
print(outliers[["student_id", "assessment_score"]])

# Check correlation between study hours and scores
correlation = data["study_hours"].corr(
    data["assessment_score"]
)

print("\nCorrelation before outlier removal:",
      round(correlation, 3))

# Compare correlation after removing detected score outliers
clean_data = data.drop(index=outliers.index)

if len(clean_data) >= 2:
    new_correlation = clean_data["study_hours"].corr(
        clean_data["assessment_score"]
    )

    print("Correlation after outlier removal:",
          round(new_correlation, 3))
else:
    print("Not enough records for comparison.")

print("\nNote: Correlation does not prove causation.")
import json

# Create a summary of the student data
summary = {
    "total_students": int(len(data)),
    "average_study_hours": round(float(data["study_hours"].mean()), 2),
    "average_assessment_score": round(
        float(data["assessment_score"].mean()), 2
    ),
    "highest_score": int(data["assessment_score"].max()),
    "lowest_score": int(data["assessment_score"].min()),
    "course_summary": {}
}

# Add course-wise statistics
for course, group in data.groupby("course"):
    summary["course_summary"][course] = {
        "student_count": int(len(group)),
        "average_score": round(
            float(group["assessment_score"].mean()), 2
        )
    }

# Save summary as a JSON file
with open("summary.json", "w") as file:
    json.dump(summary, file, indent=4)

print("\nJSON summary saved successfully!")