import unittest

from project.student import Student


class StudentTests(unittest.TestCase):
    def setUp(self):
        self.student = Student("Test Name")
        self.student_with_courses = Student("Test Name", {"Math": ["Note 1"]})

    def test_init__when_courses_is_none__expect_initialization_with_empty_dict(self):
        self.assertEqual("Test Name", self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_init__when_courses_is_not_none__expect_initialization_with_dict(self):
        self.assertEqual("Test Name", self.student.name)
        self.assertEqual({"Math": ["Note 1"]}, self.student_with_courses.courses)

    def test_enroll__when_course_exists(self):
        result = self.student_with_courses.enroll("Math", ["Note 2"])
        self.assertEqual(["Note 1", "Note 2"], self.student_with_courses.courses["Math"])
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_enroll__when_course_does_not_exists_and_student_add_notes(self):
        result = self.student_with_courses.enroll("English", ["Note 1"], "Y")
        self.assertEqual(["Note 1"], self.student_with_courses.courses["English"])
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll__when_course_does_not_exists_and_student_add_notes2(self):
        result = self.student_with_courses.enroll("English", ["Note 1"], "")
        self.assertEqual(["Note 1"], self.student_with_courses.courses["English"])
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll__when_course_does_not_exists_and_student_does_not_add_notes(self):
        result = self.student_with_courses.enroll("English", ["Note 1"], "N")
        self.assertEqual([], self.student_with_courses.courses["English"])
        self.assertEqual("Course has been added.", result)

    def test_add_notes_when_course_exists(self):
        result = self.student_with_courses.add_notes("Math", "test notes for add_notes")
        self.assertEqual(["Note 1", "test notes for add_notes"], self.student_with_courses.courses["Math"])
        self.assertEqual("Notes have been updated", result)

    def test_add_notes_when_course_does_not_exist(self):
        with self.assertRaises(Exception) as context:
            self.student.add_notes("Math", "test notes for add_notes")
        self.assertEqual("Cannot add notes. Course not found.", str(context.exception))

    def test_leave_course_when_course_exists(self):
        result = self.student_with_courses.leave_course("Math")
        self.assertEqual({}, self.student.courses)
        self.assertEqual("Course has been removed", result)

    def test_leave_course_when_course_does_not_exist(self):
        with self.assertRaises(Exception) as context:
            self.student.leave_course("English")
        self.assertEqual("Cannot remove course. Course not found.", str(context.exception))
