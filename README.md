# Grazioso Salvare - Data Dashboard (CS-340 Project)

## About the Project

This project provides a full-stack, database-connected dashboard to help **Grazioso Salvare** identify suitable rescue dogs based on real-world shelter data. It consists of:
- A **MongoDB** database model
- A **CRUD Python module** to interact with MongoDB
- A **Dash and Plotly** powered dashboard web application
- Interactive controls to filter rescue dogs and visualize their data

The dashboard allows dynamic exploration of animal records, mapping their locations, and displaying breed distributions graphically.

---

## Final Reflection

### 1. How do you write programs that are maintainable, readable, and adaptable?

To create maintainable and adaptable code, I use clear naming conventions, modular designs, and documentation within the code itself.  
In this project, the **CRUD Python module** separated database logic from the dashboard frontend, making it reusable and easy to debug.  
This approach let me connect dashboard widgets cleanly to MongoDB without duplicating connection or query logic.  
In the future, I could reuse this same CRUD module for other applications, like a mobile app, admin dashboard, or data export tool, with minimal changes.

---

### 2. How do you approach a problem as a computer scientist?

I approach problems methodically by breaking them down into smaller tasks.  
For this project, I first designed the database and CRUD functionality separately, ensuring the model layer was stable.  
Next, I layered on the view (dashboard) and controller (callbacks) systematically, verifying each feature individually.  
Compared to earlier courses, this project emphasized **system integration** and **user experience** more heavily, requiring careful attention to interaction design.  
In future client projects, I would continue using modular architecture, clear API design, and iterative testing to ensure reliability and flexibility.

---

### 3. What do computer scientists do, and why does it matter?

Computer scientists design, build, and maintain the systems that process, store, and analyze information.  
Our work connects people with data, solving real-world problems more efficiently.  
In this case, by creating a dashboard for Grazioso Salvare, I provided tools to **streamline their rescue operations**, **save time**, and **improve outcomes** when selecting and training search-and-rescue dogs.  
Well-structured systems like this enable organizations to make better decisions and expand their positive impact.

---

## Technologies Used

- **MongoDB** - flexible document database for animal shelter records
- **PyMongo** - Python library for connecting to MongoDB
- **Dash** - Python web framework for building interactive dashboards
- **Dash Leaflet** - mapping library for displaying animal locations
- **Plotly Express** - visualization library for creating pie charts
- **JupyterDash** - running Dash apps inside Jupyter Notebooks

---

## Installation and Usage

1. Install required Python packages:

```bash
pip install pymongo dash dash-leaflet jupyter-dash plotly
