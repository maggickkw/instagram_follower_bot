from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

SIMILAR_ACCOUNT = "HANDLE_OF_ACCOUNT"
PHONE_NUMBER = "YOUR_PHONE_NUMBER OR EMAIL"
PASSWORD = "YOUR_PASSWORD"

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome()


    def login(self):
        self.driver.get("https://www.instagram.com/")
        sleep(5)

        phone_number = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        phone_number.send_keys(PHONE_NUMBER)
        password = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(PASSWORD)

        sleep(3)

        login_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]')
        login_button.click()

        sleep(7)

        dismiss_modal = self.driver.find_element(By.CSS_SELECTOR, '._ac8f')
        dismiss_modal.click()

        sleep(2)

        dismiss_notification = self.driver.find_element(By.CSS_SELECTOR, '._a9--._a9_1')
        dismiss_notification.click()
        sleep(2)



    def find_followers(self):

        sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
        sleep(5)

        followers = self.driver.find_element(By.CSS_SELECTOR, '.x78zum5.x1q0g3np.xieb3on a')
        followers.click()
        sleep(3)

        # modal = self.driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')
        # for i in range(10):
        #     self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
        #     sleep(2)





    def follow(self):
        sleep(5)
        div_element = self.driver.find_element(By.CSS_SELECTOR, 'div._aano')
        for _ in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", div_element)
            sleep(2)

        buttons = self.driver.find_elements(By.CSS_SELECTOR, 'div._aano  button._acan._acap._acas._aj1-')
        # print the number of buttons found
        print(f"Found {len(buttons)} buttons")
        sleep(2)
        # iterate over the buttons and print their text content
        for button in buttons:
            button.click()
            sleep(5)


        self.driver.quit()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
