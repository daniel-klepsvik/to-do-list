# 📝 My Python Journey: CLI To-Do List (V2.1)

## 🌟 Evolution of the Project
This project started as a simple script to learn Python basics. Since then, I have refactored it into a **professional, modular application** that handles data persistence and robust error checking. 

Watching this transition from a "temporary" list to a tool that actually saves my data to a hard drive has been the most exciting part of my coding journey so far

## 🚀 Key Upgrades (V2.1)
* **Modular Architecture:** Fully separated the logic into `main.py` (User Interface) and `storage.py` (Data Handling). This follows the **Separation of Concerns** principle used in professional software development.
* **Smart Data Persistence:** Tasks are automatically synced to `tasks.json`. I implemented a `load_tasks()` function that handles the initial file check and loading sequence automatically.
* **Global Constants:** Implemented `FILENAME` constants in the storage layer. This provides a "single source of truth," making the project much easier to configure and maintain.
* **Error Resilience:** Robust `try/except` blocks prevent crashes from missing files or "nonsense" user inputs (like entering letters where a task number is expected).
* **Clean Code (DRY):** Optimized logic using "Truthiness" (`if not tasks`) and `enumerate()` for human-friendly indexing to keep the codebase "Don't Repeat Yourself" compliant.

## 🛠️ The Tech Stack
- **Persistence:** `json` module for structured, permanent data storage.
- **Environment Management:** Implemented a `.gitignore` to ensure the repository remains clean of `__pycache__` and local data files.
- **Modularity:** Advanced module imports and function encapsulation to decouple logic from the main execution loop.
- **Standardization:** Adheres to **PEP 8** naming conventions, specifically using `ALL_CAPS` for global constants.

## 🖥️ How to Run
1. Ensure you have Python installed.
2. Clone this repository.
3. Run the application:
   ```bash
   python to_do_list.py

## 🗺️ Project Roadmap & Future Improvements
I view this as "Version 2.0." As I continue my Python journey, I plan to upgrade this tool with the following milestones:

- [x] **Phase 1: Data Persistence** 💾  
  Currently, tasks disappear when the program closes. I plan to add a way to save them to a `.json` file so they stay saved.
- [ ] **Phase 2: Task Editing** ✏️  
  Add an "Edit" option so users can modify existing tasks without deleting them.
- [ ] **Phase 3: Priority & Dates** 📅  
  Implement "High/Medium/Low" priority levels and automatic timestamps for when tasks are created.
- [ ] **Phase 4: Search & Filter** 🔍  
  Add a search feature to find specific keywords within a long list of tasks.
- [ ] **Phase 5: "Clear All" Command** 🧹  
  A quick command to wipe the entire list with a confirmation prompt.
