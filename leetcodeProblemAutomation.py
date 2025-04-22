import json
import time
import os
import re
from seleniumbase import Driver
from reLogin import leetcode_login
import sys
cnt = 0

def cookiesCheck(driver):
    try:
        # Wait for avatar span (max 5 seconds)
        driver.wait_for_element('#navbar_user_avatar', timeout=5)
        return "Cookies Okay"
    except:
        return "Cookies Expired"
    
def getProblem(driver, problemID):
    try:
        problemID = str(problemID)

        # Step 1: Go to LeetCode problemset page
        driver.open("https://leetcode.com/problemset/all/")

        # Step 2: Wait for the search box and type the problem ID
        driver.wait_for_element('input[placeholder="Search questions"]', timeout=10)
        driver.type('input[placeholder="Search questions"]', problemID)
        
        # Step 3: Wait for the SECOND <a> tag that links to a problem
        time.sleep(5)

        # Step 4: Select all <a> tags within that rendered problem list
        links = driver.find_elements('a[href^="/problems/"]')

        # Step 5: Check if at least 2 links are there and return the second one
        if len(links) >= 2:
            href = links[1].get_attribute("href")
            slug_match = re.search(r"/problems/([^/?]*)", href)
            if slug_match:
                return slug_match.group(1)
            else:
                return "Failed to find the problem"
        else:
            return "Failed to find the problem"

    except Exception as e:
        return "Error fetching problem"
    
def getCppSolution(driver, problemSlug):
    try:
        # Navigate to the solutions tab for the problem
        solutions_url = f"https://leetcode.com/problems/{problemSlug}/solutions/"
        driver.open(solutions_url)

        # Wait for the search bar and enter "C++"
        driver.wait_for_element("input[placeholder='Search...']", timeout=10)
        driver.type("input[placeholder='Search...']", "cpp")

        # Wait for a few seconds for results to load
        time.sleep(3)

        # Extract the first C++ solution link
        driver.wait_for_element(f"a[href*='/problems/{problemSlug}/solutions/']", timeout=10)
        cpp_solution_link = driver.get_attribute(f"a[href*='/problems/{problemSlug}/solutions/']", "href")

        if not cpp_solution_link:
            return "Failed to find a C++ solution"

        # Navigate to the C++ solution page
        driver.open(cpp_solution_link)

        # Wait for the code block and extract the C++ code
        driver.wait_for_element("pre code.language-cpp", timeout=10)
        cpp_code = driver.get_text("pre code.language-cpp")

        return cpp_code or "Failed to find a C++ solution"

    except Exception as e:
        return "Error fetching C++ solution"
    
def submitSolution(driver, problemSlug, cppCode):
    try:
        # Navigate to the problem page
        problem_url = f"https://leetcode.com/problems/{problemSlug}/"
        driver.open(problem_url)

        # Wait for the Monaco Editor to load
        driver.wait_for_element(".monaco-editor", timeout=10)

        # Click inside the code editor to focus
        driver.click(".monaco-editor")

        # Clear any existing code
        driver.execute_script("window.monaco.editor.getModels()[0].setValue('');")

        # Insert the C++ code using Monaco API
        driver.execute_script(f"window.monaco.editor.getModels()[0].setValue({json.dumps(cppCode)});")

        # Click the Submit button
        driver.click("button[data-e2e-locator='console-submit-button']")
        print("🚀 Submitting the solution...")

        # Wait for a few seconds to allow submission
        time.sleep(5)
        
        print("✅ Submission complete! Check your LeetCode submissions.")

    except Exception as e:
        print(f"❌ Error during submission: {str(e)}")

def runLeetcodeProblemAutomation(ProblemID):
    global cnt

    script_dir = os.path.dirname(os.path.abspath(__file__))
    cookies_path = os.path.join(script_dir, "cookies.json")

    while cnt < 2 :

        # Launch browser with Undetectable Mode
        driver = Driver(uc=True, headless=True)

        driver.open("https://leetcode.com")

        try:
            with open(cookies_path, "r") as f:  # read cookies
                cookies = json.load(f)

            for cookie in cookies:
                driver.add_cookie(cookie)  # Add each cookie to the browser

            # Reload page after adding cookies
            driver.refresh()

            # Check if cookies are valid
            status = cookiesCheck(driver)
            if status != "Cookies Okay":
                driver.quit()
                result = leetcode_login()
                if result == "OK":
                    cnt += 1
                    continue
                else:
                    break
            
            problemSlug = getProblem(driver, ProblemID)
            if problemSlug == "Failed to find the problem" or problemSlug == "Error fetching problem":
                print("Error fetching daily problem")
                return
            
            cppCode = getCppSolution(driver, problemSlug)
            if cppCode == "Failed to find a C++ solution" or cppCode == "Error fetching C++ solution":
                print("Error fetching C++ solution")
                driver.quit()
                return
                
            submitSolution(driver, problemSlug, cppCode)

            break

        except Exception as e:
            break

        finally:
            driver.quit()

if __name__ == "__main__":
    if len(sys.argv) < 2 or not sys.argv[1].strip():
        print("Error: No problem ID provided. Please enter a valid problem ID.")
        sys.exit(1)

    problem_id = sys.argv[1].strip()

    if not problem_id.isdigit():
        print("Error: Invalid problem ID. Please enter a numeric value.")
        sys.exit(1)

    runLeetcodeProblemAutomation(problem_id)