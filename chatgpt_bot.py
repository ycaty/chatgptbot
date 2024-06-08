import undetected_chromedriver as uc
import time
import pickle
from selenium.webdriver.common.keys import Keys
from colorama import Fore, Style, init


# Define a custom user agent


class chatgptBot():
    def __init__(self):
        print("beep boop chatgpt bot skelly")

    def doLogin(self, username=None, password=None):
        my_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"

        # Set up Chrome options
        options = uc.ChromeOptions()
        options.headless = False
        options.add_argument(f"user-agent={my_user_agent}")

        # Initialize Chrome Webdriver with the specified options
        self.driver = uc.Chrome(options=options)

        # Make a request to your target website.
        self.driver.get("https://chat.openai.com/")

        time.sleep(3)
        # Find and click the login button using the provided HTML structure
        login_button = self.driver.find_element("xpath", "//button[@data-testid='login-button']")
        login_button.click()
        time.sleep(3)

        self.driver.find_element("xpath", """//*[@id="email-input"]""").send_keys(username)


        time.sleep(.3)
        self.driver.find_element("xpath", """//*[@id="email-input"]""").send_keys(Keys.ENTER)

        time.sleep(3)
        self.driver.find_element("xpath", '//*[@id="password"]').send_keys(password)
        time.sleep(3)
        self.driver.find_element("xpath", '//*[@id="password"]').send_keys(Keys.ENTER)


        print("waiting for login...")
        input("<<press enter>>")

    def send_message(self, msg):
        time.sleep(5)
        self.driver.find_element("xpath", '//*[@id="prompt-textarea"]  ').send_keys(msg)
        time.sleep(3)
        self.driver.find_element("xpath", '//*[@id="prompt-textarea"]  ').send_keys(Keys.ENTER)
        time.sleep(3)

    def read_all_messages(self):
        logz = self.driver.find_elements("class name", "markdown")
        print(Fore.GREEN + "Number of elements found:", len(logz))
        print(Style.RESET_ALL)

        for log in logz:
            print(Fore.YELLOW + '==========================')
            print(Fore.WHITE + log.text)
            print(Style.RESET_ALL)

    def debug_read_all_messages(self):
        while True:
            logz = self.driver.find_elements("class name", "markdown")
            print(Fore.GREEN + "Number of elements found:", len(logz))
            print(Style.RESET_ALL)

            for log in logz:
                print(Fore.YELLOW + '==========================')
                print(Fore.WHITE + log.text)
                print(Style.RESET_ALL)
                input('Press Enter to continue...')
