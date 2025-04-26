# CS-340
# Grazioso Salvare Rescue Animal Dashboard

## Project Overview

The Grazioso Salvare Rescue Animal Dashboard is a web application built for an international rescue-animal training company. It enables users to visualize and interact with shelter animal data, helping staff identify and categorize dogs suitable for rescue training. The dashboard uses MongoDB for backend data storage and the Dash framework for its interactive interface.

## Features
- Display unfiltered and filtered animal shelter data in a dynamic table.
- Filter animals by rescue type (Water Rescue, Mountain Rescue, Disaster Tracking).
- Visualize data with dynamic charts:
  - Geolocation map
  - Breed pie chart
- Branded with the Grazioso Salvare logo and developer identifier.

## Tools & Technologies
- **MongoDB**: Flexible, scalable, and integrates easily with Python via `pymongo`.
- **Dash Framework**: Python-based, supports MVC pattern, and provides interactive UI components.
- **pandas**: For data manipulation and conversion between MongoDB and table formats.
- **dash-leaflet**: For geolocation mapping.
- **plotly.express**: For dynamic charting.
- **JupyterDash**: For development in a Jupyter Notebook environment.

## Setup Instructions

### 1. Set up MongoDB:
- Install MongoDB and create a database.
- Import the provided shelter data CSV into MongoDB.

### 2. Configure the CRUD Module:
- Update `animal_shelter.py` with your MongoDB credentials.
- Ensure CRUD operations and filtering are supported.

### 3. Run the Dashboard:
- Open `ProjectTwoDashboard.ipynb` or your dashboard script.
- Add branding and implement filtering, tables, and charts as described.

### 4. Testing:
- Test all dashboard features.
- Take screenshots of each state.

## Reflection

### 1. How do you write programs that are maintainable, readable, and adaptable?
I prioritize modularity, clear documentation, and consistent coding standards. In this project, I created a standalone CRUD Python module (from Project One) to handle all database operations. This separation made my dashboard code cleaner and easier to maintain. 

The main advantages were:
- **Reusability**: The CRUD module can be used in future projects needing MongoDB operations.
- **Maintainability**: Updates to database logic are centralized, reducing errors and duplication.
- **Readability**: The dashboard code focuses on UI and data visualization, while the CRUD module handles data access.

In the future, I can reuse or adapt this module for other dashboards, analytics tools, or any application needing database access.

### 2. How do you approach a problem as a computer scientist?
I start by analyzing requirements and breaking the problem into smaller, manageable tasks. For Grazioso Salvare, I identified the need for flexible data storage, robust querying, and interactive visualization. I selected the right tools (MongoDB, Dash), used the MVC design pattern, and built the project iteratively—testing and refining as I went.

Compared to previous assignments, this project required integrating multiple technologies and focusing on real-world client needs. In the future, I will continue using modular design, iterative development, and thorough testing to create scalable, client-focused solutions.

### 3. What do computer scientists do, and why does it matter?
Computer scientists solve complex problems by designing, building, and optimizing software systems. Our work enables organizations to process information efficiently and make data-driven decisions. 

In this project, my dashboard helps Grazioso Salvare quickly identify and categorize dogs for rescue training, improving their operations and outcomes for both animals and staff.

By building maintainable, adaptable software, computer scientists empower organizations to scale, innovate, and respond to changing needs—creating real value for businesses and society.

## Artifacts
- **Dashboard Code**: `ProjectTwoDashboard.ipynb`
- **CRUD Module**: `animal_shelter.py`
- **Screenshots**: See `/screenshots` folder
- **This README**: Portfolio reflection and project documentation

## Repository Link
(https://github.com/Tlofty92/CS-340)

This README serves as both documentation for the project and a reflection on my learning, as required for my Computer Science program portfolio.
