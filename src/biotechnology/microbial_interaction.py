"""
Microbial Interaction Module

This module contains classes and functions for enhancing soil health through microbial solutions.
"""

import logging
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Microbe:
    def __init__(self, name: str, benefits: List[str]):
        """
        Initializes a Microbe instance.

        Parameters:
        - name (str): The name of the microbial species.
        - benefits (list): A list of benefits provided by the microbe.
        """
        self.name = name
        self.benefits = benefits

    def __str__(self):
        return f"{self.name} with benefits: {', '.join(self.benefits)}"

class Soil:
    def __init__(self, nutrients: Dict[str, float], microbes: List[Microbe] = None):
        """
        Initializes a Soil instance.

        Parameters:
        - nutrients (dict): A dictionary of nutrient levels in the soil.
        - microbes (list): A list of Microbe instances present in the soil.
        """
        self.nutrients = nutrients
        self.microbes = microbes if microbes is not None else []

    def add_microbe(self, microbe: Microbe):
        """
        Adds a microbe to the soil.

        Parameters:
        - microbe (Microbe): The Microbe instance to add.
        """
        self.microbes.append(microbe)
        logging.info(f"Added microbe: {microbe}")

    def analyze_health(self) -> Dict[str, Any]:
        """
        Analyzes the health of the soil based on nutrient levels and microbial presence.

        Returns:
        - dict: A summary of the soil's health.
        """
        health_summary = {
            "nutrient_levels": self.nutrients,
            "microbial_count": len(self.microbes),
            "microbial_benefits": [microbe.benefits for microbe in self.microbes]
        }
        logging.info(f"Soil health analysis: {health_summary}")
        return health_summary

class MicrobialEnhancer:
    def __init__(self):
        """
        Initializes the MicrobialEnhancer instance.
        """
        logging.info("Microbial Enhancer initialized.")

    def enhance_soil_health(self, soil: Soil, microbes: List[Microbe]) -> Soil:
        """
        Introduces beneficial microbes to improve soil health.

        Parameters:
        - soil (Soil): The Soil object to be enhanced.
        - microbes (list): A list of Microbe instances to introduce.

        Returns:
        - Soil: The enhanced Soil object.
        """
        logging.info(f"Enhancing soil health with microbes: {[microbe.name for microbe in microbes]}")
        for microbe in microbes:
            soil.add_microbe(microbe)

        logging.info("Soil health enhancement complete.")
        return soil

# Example usage
if __name__ == "__main__":
    # Create soil instance
    initial_nutrients = {"nitrogen": 20.0, "phosphorus": 15.0, "potassium": 10.0}
    soil = Soil(nutrients=initial_nutrients)

    # Create microbial instances
    rhizobacteria = Microbe("Rhizobacteria", ["Nitrogen fixation", "Disease resistance"])
    mycorrhizae = Microbe("Mycorrhizae", ["Nutrient absorption", "Soil structure improvement"])

    # Initialize the microbial enhancer
    enhancer = MicrobialEnhancer()

    # Enhance soil health
    enhanced_soil = enhancer.enhance_soil_health(soil, [rhizobacteria, mycorrhizae])

    # Analyze the enhanced soil health
    health_analysis = enhanced_soil.analyze_health()
    print(health_analysis)
