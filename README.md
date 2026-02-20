# 📝 My First Python Project: CLI To-Do List

## 🌟 Why I Built This
This is my very first official Python project! I chose to build a To-Do List because the concept is both interesting and genuinely useful for my own daily organization. 

It has been incredibly cool to see my newly acquired programming skills come to life. Seeing a blank file turn into a tool that handles data and logic was fascinating to me. I’m proud of how I tackled input validation to make the app feel professional and robust.

## 🚀 Features
* **Add Tasks:** Quickly append new items to the list.
* **View Tasks:** See current tasks with clean, human-friendly numbering (starting at 1).
* **Smart Removal:** Delete tasks by their number using `.pop()` for precise data management.
* **Error Resilience:** I built `try/except` blocks to handle "nonsense" inputs (like letters or symbols) without the program crashing.
* **User-Centric Flow:** Includes "escape hatches" that allow you to cancel an action and return to the main menu.

## 🛠️ How it Works
This project uses several core Python concepts that I've been learning:
- **Loops:** A `while True` loop keeps the application alive.
- **Data Structures:** Uses a `list` to store tasks.
- **Exception Handling:** Uses `try/except` to catch `ValueError`.
- **Logic:** Uses `if/elif/else` statements combined with `.lower()` to handle diverse user inputs.

## 🖥️ How to Run
1. Ensure you have Python installed on your machine.
2. Clone this repository to your local computer.
3. Open your terminal and run:
   ```bash
   python todo.py

## 🗺️ Project Roadmap & Future Improvements
I view this as "Version 1.0." As I continue my Python journey, I plan to upgrade this tool with the following milestones:

- [ ] **Phase 1: Data Persistence** 💾  
  Currently, tasks disappear when the program closes. I plan to learn how to save them to a `.txt` or `.json` file so they stay saved.
- [ ] **Phase 2: Task Editing** ✏️  
  Add an "Edit" option so users can modify existing tasks without deleting them.
- [ ] **Phase 3: Priority & Dates** 📅  
  Implement "High/Medium/Low" priority levels and automatic timestamps for when tasks are created.
- [ ] **Phase 4: Search & Filter** 🔍  
  Add a search feature to find specific keywords within a long list of tasks.
- [ ] **Phase 5: "Clear All" Command** 🧹  
  A quick command to wipe the entire list with a confirmation prompt.
