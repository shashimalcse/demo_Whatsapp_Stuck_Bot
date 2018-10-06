#---Whatsapp_Stuck----
#I used python 2.7 and Chrome browser
from selenium import webdriver
browser=webdriver.Chrome("C:\Python27/chromedriver")
browser.get('http://web.whatsapp.com')
name=raw_input("Enter the name:")
msg=raw_input("Enter the msg:")
number_of_msgs=int(raw_input("Enter number_of_msgs:"))
user=browser.find_element_by_xpath('//span[@title="{}"]'.format(name))
user.click()
msgbox=browser.find_element_by_class_name("_1Plpp")
for i in range(number_of_msgs):
    msgbox.send_keys(msg)
    btn=browser.find_element_by_class_name("_35EW6")
    btn.click()
    
    


