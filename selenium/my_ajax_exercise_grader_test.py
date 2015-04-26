import unittest
from test_initializer import TestInitializer
from page_objects import CourseName, LoginPage, MyAjaxExerciseGrader

class MyAjaxExerciseGraderTest(unittest.TestCase):
    def setUp(self):
        testInitializer = TestInitializer()
        self.driver = testInitializer.getFirefoxDriverWithLoggingEnabled()
        testInitializer.recreateDatabase()
        LoginPage(self.driver).loginToCourse(CourseName.APLUS)

    def testShouldGiveZeroPointsOnEmptySubmit(self):
        myAjaxExercisePage = MyAjaxExerciseGrader(self.driver)
        myAjaxExercisePage.submit()

        self.assertEqual(myAjaxExercisePage.getAllowedSubmissions(), '1/10')
        self.assertEqual(myAjaxExercisePage.getExerciseScore(), '0 / 100')
        self.assertEqual(myAjaxExercisePage.getNumberOfSubmitters(), '1')
        self.assertEqual(myAjaxExercisePage.getAverageSubmissionsPerStudent(), '1.00')

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)