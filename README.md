# 📝 My Python Journey: CLI To-Do List (V2.0)

## 🌟 Evolution of the Project
This project started as a simple script to learn Python basics. Since then, I have refactored it into a **professional, modular application** that handles data persistence and robust error checking. 

Watching this transition from a "temporary" list to a tool that actually saves my data to a hard drive has been the most exciting part of my coding journey so far

## 🚀 Key Upgrades (V2.0)
* **Data Persistence:** I moved beyond temporary memory. Tasks are now automatically saved to and loaded from `to_do_list.json`.
* **Modular Architecture:** I separated the code into `to_do_list.py` and `storage.py`. This makes the code cleaner and follows the "Separation of Concerns" principle.
* **Error Resilience:** I implemented `try/except` blocks to handle missing files and "nonsense" user inputs (like letters where numbers should be) without the program crashing.
* **Refined Logic:** Using "Truthiness" (`if not tasks`) and centralized functions to keep the code DRY (Don't Repeat Yourself).

## 🛠️ The Tech Stack
- **Persistence:** `json` module for reading/writing structured data.
- **Modularity:** Custom module imports (`import storage`) for organized code.
- **Logic:** `enumerate()` for human-friendly indexing, `.lower()` for case-insensitive commands, and list manipulation.
- **Exception Handling:** Catching `FileNotFoundError` and `ValueError`.

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
