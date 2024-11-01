"""
Plant Traits Module

This module contains classes and functions for defining, modifying, and analyzing plant traits.
"""

import logging
from typing import Dict, Any, List

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PlantTrait:
    def __init__(self, name: str, description: str, value: Any):
        """
        Initializes a PlantTrait instance.

        Parameters:
        - name (str): The name of the trait.
        - description (str): A brief description of the trait.
        - value (Any): The current value of the trait (e.g., True/False, numeric).
        """
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return f"{self.name}: {self.description} (Value: {self.value})"

class Plant:
    def __init__(self, species: str):
        """
        Initializes a Plant instance.

        Parameters:
        - species (str): The name of the plant species.
        """
        self.species = species
        self.traits: Dict[str, PlantTrait] = {}

    def add_trait(self, trait: PlantTrait):
        """
        Adds a trait to the plant.

        Parameters:
        - trait (PlantTrait): The PlantTrait instance to add.
        """
        self.traits[trait.name] = trait
        logging.info(f"Added trait: {trait} to {self.species}")

    def modify_trait(self, trait_name: str, new_value: Any):
        """
        Modifies the value of an existing trait.

        Parameters:
        - trait_name (str): The name of the trait to modify.
        - new_value (Any): The new value for the trait.
        """
        if trait_name in self.traits:
            old_value = self.traits[trait_name].value
            self.traits[trait_name].value = new_value
            logging.info(f"Modified trait '{trait_name}' from {old_value} to {new_value} for {self.species}")
        else:
            logging.warning(f"Trait '{trait_name}' not found in {self.species}.")

    def analyze_traits(self) -> List[str]:
        """
        Analyzes the traits of the plant and returns a summary.

        Returns:
        - list: A list of strings summarizing the traits.
        """
        summary = [str(trait) for trait in self.traits.values()]
        logging.info(f"Trait analysis for {self.species}: {summary}")
        return summary

# Example usage
if __name__ == "__main__":
    # Create a plant instance
    sunflower = Plant("Sunflower")

    # Define and add traits
    height_trait = PlantTrait("Height", "Maximum height of the plant", "3m")
    drought_resistance_trait = PlantTrait("Drought Resistance", "Ability to withstand drought", True)
    flowering_time_trait = PlantTrait("Flowering Time", "Time taken to flower", "60 days")

    sunflower.add_trait(height_trait)
    sunflower.add_trait(drought_resistance_trait)
    sunflower.add_trait(flowering_time_trait)

    # Modify a trait
    sunflower.modify_trait("Height", "3.5m")

    # Analyze traits
    traits_summary = sunflower.analyze_traits()
    print(traits_summary)
