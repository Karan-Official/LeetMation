from seleniumbase import Driver
import json
import time
import os

def load_credentials():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    credentials_path = os.path.join(script_dir, "credentials.json")

    try:
        with open(credentials_path, "r") as f:
            credentials = json.load(f)
        return credentials.get("username"), credentials.get("password")
    except Exception as e:
        return None, None

def leetcode_login():
    
    username, password = load_credentials()
    if not username or not password:
        return "Error Load Credentials"

    script_dir = os.path.dirname(os.path.abspath(__file__))
    cookies_path = os.path.join(script_dir, "cookies.json")
    
    # Launch browser with Undetectable Mode
    driver = Driver(uc=True, headless=True)

    try:
        # Open LeetCode login page
        url = "https://leetcode.com/accounts/login"
        driver.uc_open_with_reconnect(url, reconnect_time=6)

        # Type username and password
        driver.type('input[name="login"]', username)
        driver.type('input[name="password"]', password)

        # Wait for Sign In button to appear
        driver.wait_for_element("#signin_btn", timeout=10)

        # Click the Sign In button
        driver.click("#signin_btn")

        # Wait for login process
        time.sleep(5)

        # Check if login was successful using profile avatar
        login_status = cookies_check(driver)

        if login_status == None:
            return "Error Login"
        
        # Extract session cookies
        cookies = extract_cookies(driver)

        if cookies:
            result = save_cookies_to_json(cookies, cookies_path)
            if result == None:
                return "Error Saving Cookies"
            
        return "OK"

    except Exception as e:
        return "Error Login"

    finally:
        # Close browser
        driver.quit()


def cookies_check(driver):
    try:
        # Wait for avatar span (max 5 seconds)
        driver.wait_for_element('#navbar_user_avatar', timeout=5)
        return "Cookies Okay"
    except:
        return None
    

def extract_cookies(driver):
    try:
        # Get all cookies from the browser session
        all_cookies = driver.get_cookies()

        # Extract specific cookies
        leetcode_session = None
        csrftoken = None

        for cookie in all_cookies:
            if cookie['name'] == 'LEETCODE_SESSION':
                leetcode_session = cookie['value']
            elif cookie['name'] == 'csrftoken':
                csrftoken = cookie['value']

        if leetcode_session and csrftoken:
            return [
                {
                    "name": "LEETCODE_SESSION",
                    "value": leetcode_session,
                    "domain": ".leetcode.com",
                    "path": "/",
                    "httpOnly": True,
                    "secure": True,
                    "sameSite": "Lax"
                },
                {
                    "name": "csrftoken",
                    "value": csrftoken,
                    "domain": ".leetcode.com",
                    "path": "/",
                    "httpOnly": False,
                    "secure": True,
                    "sameSite": "Lax"
                }
            ]
        else:
            return None

    except Exception as e:
        return None
    
def save_cookies_to_json(cookies, filepath):
    try:
        with open(filepath, "w") as f:
            json.dump(cookies, f, indent=2)
        return "Success"
    except Exception as e:
        return None
