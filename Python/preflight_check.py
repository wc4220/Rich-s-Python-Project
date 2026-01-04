import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

def check_setup():
    print("--- 🛠️ Starting Pre-Flight Check ---")

    # 1. Check Libraries
    print(f"✅ Pandas Version: {pd.__version__}")
    print(f"✅ Selenium Version: {selenium.__version__}")

    # 2. Check File System (Local Directory)
    current_dir = os.getcwd()
    print(f"✅ Working Directory: {current_dir}")

    # 3. Check Browser Automation (The most important part for CMMS)
    print("\nAttempting to open a 'Robot' browser window...")
    try:
        # This automatically downloads the driver and opens Chrome
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless") # Uncomment this later to run in background
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        
        driver.get("https://www.google.com")
        print(f"✅ Browser Control: Success (Page Title: {driver.title})")
        driver.quit()
    except Exception as e:
        print(f"❌ Browser Control Failed: {e}")
        print("\nNOTE: This is common on company laptops. If it failed, you might need to use Edge instead of Chrome.")

    print("\n--- ✨ Environment is Ready! ---")

if __name__ == "__main__":
    check_setup()