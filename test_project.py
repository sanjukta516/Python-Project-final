import unittest
from student_record import StudentRecord


class TestStudentRecord(unittest.TestCase):

    def test_grade_A(self):
        student = StudentRecord("S001", "Python", 5, 85)
        self.assertEqual(student.calculate_grade(), "A")

    def test_grade_C(self):
        student = StudentRecord("S002", "Java", 3, 65)
        self.assertEqual(student.calculate_grade(), "C")

    def test_grade_F(self):
        student = StudentRecord("S003", "Python", 2, 40)
        self.assertEqual(student.calculate_grade(), "F")


if __name__ == "__main__":
    unittest.main()