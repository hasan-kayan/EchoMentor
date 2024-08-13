from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager  # Import ChromeDriverManager
from bs4 import BeautifulSoup
import time

def open_whatsapp_web():
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--user-data-dir=chrome-data")  # Preserve user data to avoid re-login
    chrome_options.add_argument("--profile-directory=Default")
    
    # Set up the Chrome WebDriver with webdriver-manager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
    # Open WhatsApp Web
    driver.get("https://web.whatsapp.com")
    
    try:
        # Check if already logged in by looking for the presence of the chat list
        chat_list_present = driver.find_element(By.CLASS_NAME, "_2wP_Y")
        print("Already logged in, proceeding with scraping...")
    except:
        # If chat list is not found, wait for login
        print("Waiting for login via QR code...")
        time.sleep(20)  # Adjust this time according to your needs

    return driver

def scrape_messages(driver):
    time.sleep(15)  # Increased wait time
    
    # Print the current URL to ensure the correct page is loaded
    print(f"Current URL: {driver.current_url}")
    
    # Find the chat list
    chat_list = driver.find_elements(By.CLASS_NAME, "_2wP_Y")
    print(f"Found {len(chat_list)} chats.")
    
    # Print chat elements (for debugging)
    for chat in chat_list:
        print(chat.text)
    
    # Proceed with scraping
    for chat in chat_list:
        chat.click()
        time.sleep(3)
        
        # Scrape the chat
        try:
            contact_name = driver.find_element(By.CLASS_NAME, "_21nHd").text
            chat_number = driver.find_element(By.CLASS_NAME, "_3WQ4x").text  # Contact number
            messages = driver.find_elements(By.CLASS_NAME, "_1Gy50")  # Messages container
        except Exception as e:
            print(f"Error finding elements: {e}")
            continue

        # Extract messages
        chat_text = []
        for message in messages:
            soup = BeautifulSoup(message.get_attribute('innerHTML'), 'html.parser')
            chat_text.append(soup.text)
        
        # Save chat to file
        file_name = f"{contact_name}_{chat_number}.txt"
        with open(file_name, "w", encoding="utf-8") as file:
            file.write("\n".join(chat_text))
    
    print("Scraping completed.")


if __name__ == "__main__":
    driver = open_whatsapp_web()
    scrape_messages(driver)
    driver.quit()
