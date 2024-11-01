# EGaia Core User Guide

This user guide provides instructions on how to utilize the community engagement tools available in the EGaia Core project. These tools are designed to facilitate education and participation in ecological restoration efforts.

## Community Engagement Tools

### Education Platform

The education platform allows users to create and participate in courses related to ecological restoration.

#### Creating a Course

To create a course, use the following function:

```python
1 create_course(title, content)
```

- Parameters:
   - title: The title of the course.
   - content: The content or curriculum of the course.

Example

```python
1 create_course("Introduction to Ecological Restoration", "This course covers the basics of ecological restoration...")
```

## Citizen Science
The citizen science module enables users to contribute their observations of local ecosystems.

### Submitting an Observation
To submit an observation, use the following function:

```python
1 submit_observation(observation)
```

- Parameters:
   - observation: A dictionary containing details about the observation (e.g., species, location, date).

Example

```python
observation = {
    "species": "Oak Tree",
    "location": "Central Park",
    "date": "2023-10-01"
}
submit_observation(observation)
```

## Getting Help
If you encounter any issues or have questions about using the community engagement tools, please reach out to the project maintainers at [support@egaia.com].

