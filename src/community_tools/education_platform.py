import json
import random

class EducationPlatform:
    """Class for managing educational resources and training modules."""
    
    def __init__(self):
        self.resources = []
        self.modules = []

    def add_resource(self, title: str, content: str):
        """Add an educational resource."""
        resource = {
            'title': title,
            'content': content
        }
        self.resources.append(resource)
        print(f"Resource '{title}' added.")

    def add_module(self, title: str, content: str, questions: list):
        """Add a training module with assessment questions."""
        module = {
            'title': title,
            'content': content,
            'questions': questions
        }
        self.modules.append(module)
        print(f"Module '{title}' added.")

    def list_resources(self):
        """List all educational resources."""
        print("Available Resources:")
        for resource in self.resources:
            print(f"- {resource['title']}")

    def list_modules(self):
        """List all training modules."""
        print("Available Training Modules:")
        for module in self.modules:
            print(f"- {module['title']}")

    def take_module(self, title: str):
        """Take a training module and answer questions."""
        module = next((m for m in self.modules if m['title'] == title), None)
        if module:
            print(f"Taking module: {module['title']}")
            print(module['content'])
            score = 0
            for question in module['questions']:
                print(question['question'])
                answer = input("Your answer: ")
                if answer.lower() == question['answer'].lower():
                    score += 1
            print(f"You scored {score}/{len(module['questions'])} in '{module['title']}'")
        else:
            print(f"Module '{title}' not found.")

# Example usage
if __name__ == "__main__":
    platform = EducationPlatform()
    platform.add_resource("Introduction to Ecosystems", "This resource covers the basics of ecosystems.")
    platform.add_module("Ecosystem Dynamics", "This module covers the interactions within ecosystems.", [
        {'question': "What is an ecosystem?", 'answer': "A community of living organisms and their environment."},
        {'question': "What is biodiversity?", 'answer': "The variety of life in the world or in a particular habitat."}
    ])
    platform.list_resources()
    platform.list_modules()
    platform.take_module("Ecosystem Dynamics")
