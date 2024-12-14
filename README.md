# 🌐 CLIMATE: Typhoon and Climate Awareness Platform
[![Python](https://img.shields.io/badge/Python-Programming-orange)](https://www.python.org/)  
[![SDG 13](https://img.shields.io/badge/SDG-13-blue)](https://sdgs.un.org/goals/goal13)  
---

## 📜 Project Overview
The Philippines experiences numerous typhoons annually, making it crucial for people to have adequate knowledge about these natural disasters. **CLIMATE** is an innovative platform designed to enhance public understanding of typhoons and their connection to global climate change. By interpreting complex climate data into user-friendly and interactive tools, CLIMATE bridges the gap between scientific research and public awareness.

### ✨ Key Features:
- **Article and Typhoon Repository**: A database of articles and detailed records of past and present typhoons, including their names, years of occurrence, affected areas, and wind speeds.
- **Interactive Typhoon Database**: Tools for users to search, add, and delete typhoon-related information and articles.
- **Wind Speed Calculator**: An interactive tool to estimate typhoon strength using user inputs and the Saffir-Simpson scale, displaying converted wind speed values across units.

### ❌ Excluded Features:
- Prediction or forecasting of typhoon paths.
- Real-time weather updates.
- Integration with emergency response systems.
- Analysis of non-typhoon climate phenomena.

### 🔍 Target Users:
- **Students**: For educational purposes to foster understanding of typhoons and climate change.
- **Researchers and Educators**: As a teaching and reference resource.
- **General Public**: To promote climate awareness and engagement.

### 🛠️ SMART Objectives:
1. **Specific**: Provide an engaging and interactive platform for exploring typhoon data and climate-related articles.
2. **Measurable**: Support at least 10 test users performing operations like accessing articles and exploring the database.
3. **Achievable**: Deliver all core functionalities (repository, database, wind speed calculator) within one month.
4. **Relevant**: Align with global climate awareness goals by making typhoon information easily accessible and educational.
5. **Time-bound**: Ensure a fully operational system is ready before the project deadline.

---

## 📊 Python Concepts and Libraries

The CLIMATE project uses Python and its standard library Tkinter to create a graphical user interface (GUI), alongside SQLite for database management. Below are the details:

1. **Tkinter**:
   - **Label**: Displays text or images.
   - **Button**: Triggers actions in the system.
   - **Entry**: Single-line text input (e.g., for user input).
   - **Text**: Multi-line text input (e.g., for article content).
   - **Canvas**: Supports custom drawings and scrollable frames.

   **Geometry Management**:
   - `pack`: Used for simple stacking of widgets.
   - `grid`: Provides table-like layouts for concise widget placement.
   - `place`: Enables precise widget positioning using x, y coordinates.

2. **Object-Oriented Programming (OOP)**:
   - **Classes**: Each class represents a specific window or functionality.
   - **Encapsulation**: Groups related widgets and methods within classes.
   - **Abstraction**: Hides complex implementation details, exposing essential functionality.
   - **Inheritance**: Extends functionality by creating instances of other classes.
   - **Polymorphism**: Enables buttons and events to call different methods for various actions.

3. **Event Handling**:
   - `command`: Attaches functions to button clicks.
   - `bindings`: Associates events (e.g., key presses, mouse clicks) with handler functions.

4. **SQLite3**:
   - A lightweight, serverless database used to store typhoon data and articles efficiently.
   - Queries are managed in a separate file (`climateDatabase`) for improved readability and maintainability.

---

## 🌍 Sustainable Development Goal (SDG) Integration

CLIMATE aligns with **SDG 13: Climate Action**, by:
- Enhancing climate literacy among students, educators, and the general public.
- Encouraging proactive measures by providing accessible information about typhoons and their impact.
- Contributing to education and advocacy for climate change mitigation and adaptation.

---

## 🛠️ Instructions for Running the Program

1. **Download the ZIP File**:
   - Go to the project repository and download the ZIP file.
   - Extract the contents to your desired location.

2. **Run the Program**:
   - Open a terminal or command prompt.
   - Navigate to the extracted folder.
   - Run the following command:
     ```bash
     python climate.py
     ```

3. **Explore the Application**:
   - The GUI will launch, allowing you to interact with the platform.

---

## 📫 Project Developed By
**Batangas State University - The National Engineering University**
- **Developer Name**: [Dela Cruz Chester Paul D.]
- **Contact Information**:
  - **Email**: 23-09196@g.batstate-u.edu.ph
  - **Phone**: (+63) 969-5038-566
  - 👤 [GitHub Profile](https://github.com/Azeltdz)
