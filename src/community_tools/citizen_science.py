import random
import pandas as pd

class CitizenScience:
    """Class for managing citizen science participation."""
    
    def __init__(self):
        self.projects = []

    def add_project(self, title: str, description: str, data_collection_method: str):
        """Add a citizen science project."""
        project = {
            'title': title,
            'description': description,
            'data_collection_method': data_collection_method,
            'data': []
        }
        self.projects.append(project)
        print(f"Project '{title}' added.")

    def list_projects(self):
        """List all citizen science projects."""
        print("Available Citizen Science Projects:")
        for project in self.projects:
            print(f"- {project['title']}: {project['description']}")

    def collect_data(self, project_title: str, data_entry: dict):
        """Collect data for a specific project."""
        project = next((p for p in self.projects if p['title'] == project_title), None)
        if project:
            project['data'].append(data_entry)
            print(f"Data collected for project '{project_title}': {data_entry}")
        else:
            print(f"Project '{project_title}' not found.")

    def analyze_data(self, project_title: str):
        """Analyze collected data for a specific project."""
        project = next((p for p in self.projects if p['title'] == project_title), None)
        if project and project['data']:
            df = pd.DataFrame(project['data'])
            print(f"Data Analysis for project '{project_title}':")
            print(df.describe())
        else:
            print(f"No data available for project '{project_title}'.")

# Example usage
if __name__ == "__main__":
    citizen_science = CitizenScience()
    citizen_science.add_project("Bird Watching", "Collect data on bird species in your area.", "Field observations")
    citizen_science.add_project("Water Quality Monitoring", " Monitor water quality in your local waterways.", "Water sampling")
    citizen_science.list_projects()
    citizen_science.collect_data("Bird Watching", {'species': 'Robin', 'location': 'Backyard', 'date': '2023-02-15'})
    citizen_science.collect_data("Water Quality Monitoring", {'location': 'River', 'date': '2023-02-20', 'pH': 7.5})
    citizen_science.analyze_data("Bird Watching")
    citizen_science.analyze_data("Water Quality Monitoring")
