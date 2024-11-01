import unittest
from community_tools import EducationPlatform, CitizenScience  # Assuming these classes are in community_tools.py

class TestCommunityTools(unittest.TestCase):
    """Unit tests for community engagement tools."""

    def setUp(self):
        self.education_platform = EducationPlatform()
        self.citizen_science = CitizenScience()

    def test_add_resource(self):
        # Test adding an educational resource
        self.education_platform.add_resource("Test Resource", "This is a test resource.")
        self.assertEqual(len(self.education_platform.resources), 1)

    def test_collect_data(self):
        # Test collecting data for a citizen science project
        self.citizen_science.add_project("Test Project", "Test description", "Test method")
        self.citizen_science.collect_data("Test Project", {'data_point': 1})
        self.assertEqual(len(self.citizen_science.projects[0]['data']), 1)

if __name__ == "__main__":
    unittest.main()
