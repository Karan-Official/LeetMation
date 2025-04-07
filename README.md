<h1 align="center">LeetMation</h1>

<p align="center">
  <b>by Karan Prajapati</b>  
</p>

<p align="center">
  🚀 Automate your LeetCode workflow with style and efficiency!  
</p>

---

## 📌 Description

**LeetMation** is an automation tool designed to streamline your LeetCode problem-solving workflow. Built with efficiency in mind, this program:

- Automatically logs in to a user's LeetCode account using provided credentials
- Solves the **Daily Challenge** as well as **any problem by its problem ID**
- Writes and submits solutions in **C++**
- Uses **web scraping techniques** to:
  - Fetch the problem statement
  - Retrieve or generate a valid solution
  - Upload and submit the solution on behalf of the user

### 💡 Why LeetMation?
LeetMation removes the repetitive tasks from your coding practice routine. Whether you're grinding daily problems or targeting specific ones, it gets the job done while you focus on logic — not clicks.

> ⚠️ **Note**: This tool is for educational and personal productivity purposes only. Use responsibly and in compliance with LeetCode's terms of service.

---

## 🛠️ Technologies Used

### 📦 Libraries & Frameworks
- **[SeleniumBase](https://seleniumbase.io/)** – for automating browser actions and interacting with the LeetCode interface
- **reLogin (Custom Module)** – handles secure login to LeetCode accounts using user credentials

### 📚 Standard Python Modules
- `json` – to handle config and data serialization
- `time` – for controlling script timing and delays
- `os` – for file and system operations
- `re` – regular expressions for parsing and matching
- `sys` – system-specific parameters and functions
- `subprocess` – to run shell commands (e.g., compiling and running C++ code)
- `shutil` – for file operations (copying, deleting, etc.)
- `pathlib` – object-oriented file system paths
- `ctypes` – for interacting with C-level APIs
- `platform` – to detect and adapt to OS-level configurations

---

## ⚠️ LeetCode Setup Requirement

Before using **LeetMation**, make sure to configure your LeetCode editor with the correct language settings:

1. **Log in to your LeetCode account** manually (just once).
2. Open any coding problem in the **LeetCode Editor**.
3. From the language dropdown, select **C++**.
4. LeetCode will remember this language as your default.

> 🛠️ LeetMation relies on this setting to paste and submit C++ code automatically.  
> Make sure it's set to C++ before running the script, or the submission may fail or go to the wrong language tab.

---

## ⚙️ Installation & Setup

Follow these steps to install and set up **LeetMation**:

1. **Download the ZIP** of this repository and **unzip** it to a location of your choice.

2. **Open a terminal** (or Command Prompt) inside the unzipped folder.

3. Run the following command:
   ```bash
   python ./setup.py
   ```

   ✅ This will:
   - Create a **hidden folder** to securely store your LeetCode credentials.
   - Generate an **executable file**:
     - `.bat` file for **Windows**
     - `.sh` script for **macOS/Linux**

4. After successful setup, you may delete the project folder — the executable (`.bat` or `.sh`) will be sufficient to run the automation.

5. To automate LeetCode submissions, simply run:
   - On **Windows**: Double-click the `.bat` file
   - On **Mac/Linux**: Execute the `.sh` file from terminal

> ⚠️ Make sure Python is installed and added to your system path. This script uses Python 3.

---

## 🚀 Usage

Once the executable file is created (`.bat` for Windows or `.sh` for macOS/Linux), simply run it to start the automation.

You will be presented with two options:

1. **Solve Daily Problem**
   - Automatically fetches the current **LeetCode Daily Challenge**
   - Retrieves the solution
   - Submits it on your behalf

2. **Solve Problem by ID**
   - Prompts you to enter the **Problem ID**
   - Fetches the corresponding problem
   - Retrieves the solution
   - Submits it automatically

> ⚠️ **Note:** If the submission fails once or twice, try running the script again. This can happen due to internal issues or network connectivity problems.

---
