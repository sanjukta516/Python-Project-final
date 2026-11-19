class StudentRecord:
    def __init__(self, student_id, course, study_hours, assessment_score):
        self.student_id = student_id
        self.course = course
        self.study_hours = study_hours
        self.assessment_score = assessment_score

    def calculate_grade(self):
        score = self.assessment_score

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