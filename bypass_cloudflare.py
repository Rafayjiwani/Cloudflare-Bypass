from seleniumbase import Driver
import random
import time

def get_random_ip(file_path):
    with open(file_path, 'r') as file:
        ips = [line.strip().split(':') for line in file]
    random_ip = random.choice(ips)
    formatted_ip = f"{random_ip[2]}:{random_ip[3]}@{random_ip[0]}:{random_ip[1]}"
    return formatted_ip

file_path = 'proxies.txt'
random_ip = str(get_random_ip(file_path))

# With Proxy List: 
driver = Driver(uc=True,proxy=random_ip)

# Without Proxy List:
# driver = Driver(uc=True)

driver.maximize_window()

def open_the_turnstile_page(sb):
    sb.uc_open("https://nopecha.com/demo/cloudflare")
    
def click_turnstile_and_verify(sb):
    try:
        sb.switch_to_frame("iframe")
    except:
        pass
    try:
        sb.uc_click("span.mark")
    except:
        pass
    for i in range(5):
        try:
            ff = driver.find_element(by='xpath',value="//*[@id='challenge-success']")
        except:
            break
        if ff.is_displayed():
            break
        time.sleep(1)
    try:
        ff = driver.find_element(by='xpath',value="//*[@id='challenge-success']")
    except:
        return
    if ff.is_displayed():
        return
    else:
        open_the_turnstile_page(sb)
        click_turnstile_and_verify(sb)
        

open_the_turnstile_page(driver)
click_turnstile_and_verify(driver)
