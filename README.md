Student Performance and Study-Hours Dashboard

1. Project Overview

This project analyzes students' study hours and assessment scores using Python. It summarizes student performance, compares courses, identifies possible data-quality issues, and generates graphs for visualization.

2. Objectives

- Analyze the relationship between study hours and assessment scores.
- Calculate average, highest, and lowest scores.
- Compare student performance across courses.
- Visualize the data using graphs.
- Export summary statistics to a JSON file.
- Test the grade-calculation function.

3. Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- CSV file handling
- JSON file handling
- Unit testing with unittest

4. Project Files

- "mainn.py" — Main program for data analysis.
- "student_record.py" — Contains the StudentRecord class and grade-calculation method.
- "student_data.csv" — Dataset containing student information, study hours, and assessment scores.
- "test_project.py" — Tests the grade-calculation method.
- "summary.json" — Stores summary statistics in JSON format.
- "graphs/" — Contains the generated graphs.

5. How to Run the Project

1. Install Python.

2. Install the required libraries using:
   
   "python -m pip install pandas numpy matplotlib"

3. Open the project folder in VS Code.

4. Run the main program:
   
   "python mainn.py"

5. Run the unit tests:
   
   "python -m unittest -v test_project"

6. Expected Outputs

The program displays summary statistics and course-wise analysis. It generates a scatter plot of study hours versus assessment scores, a score histogram, and a JSON summary file.

7. Conclusion

This project demonstrates how Python can be used to read, analyze, test, and visualize student-performance data. It also provides practice with functions, classes, data structures, file handling, and data-analysis libraries.