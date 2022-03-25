#          LIBRARYS           #
from selenium import webdriver
import requests
from selenium.webdriver.common.keys import Keys
import time
from pymsgbox import *
###############################

##########################################################################
path_ = 'C:\Program Files (x86)\chromedriver.exe'  # The Path of WebDriver
driver = webdriver.Chrome(path_) # WebDriver Chrome
##########################################################################

##########################################################
link_of_site = 'https://facebook.com' # Facebook Link
request_server = requests.get(link_of_site) # Request ...
response_ = request_server.status_code # Response ...
##########################################################

#############################################################################
# Login_Facebook_Method is the function to Login by Your Account in Facebook
def Login_Facebook_Method(email_address_or_phone_number='' , password_key=''):
    # open site in chrome browser
    driver.get(link_of_site)
    # find name : email in HTML code
    email = driver.find_element_by_name('email')
    time.sleep(0.3)
    # put email_address_or_phone_number in the email irea
    email.send_keys(email_address_or_phone_number)
    # wait 1 second and search on next name : pass in HTML code
    time.sleep(1)
    password = driver.find_element_by_name('pass')
    time.sleep(0.3)
    # put password in the pass irea
    password.send_keys(password_key)
    time.sleep(1)
    # search on login name Button
    login = driver.find_element_by_name('login')
    time.sleep(0.3)
    # CLICK
    login.click()
##############################################################################

######################################################################
if response_ == 200:
    Login_Facebook_Method('hyxvfptvf@cutradition.com', 'derradji.b76f')
else:
    # Message Box : Site not Working ...
    alert(text='Site not Working', title='Error Request', button='OK')
######################################################################