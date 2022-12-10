import time
import RPi.GPIO as GPIO
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# set GPIO connection
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.IN, pull_up_down=GPIO.PUD_UP)


options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

service = Service(executable_path='/usr/bin/chromedriver')
browser = webdriver.Chrome(service=service,options=options)

#elem = browser.find_element_by_name('inquire')

while True:
	GPIO.output(17,0)
	GPIO.wait_for_edge(18,GPIO.FALLING)
	counter = 1
	#browser.get("https://localhost:3001/pending")
	browser.find_element(By.ID,'inquire').click()
	while True:
		GPIO.output(17,1)
		time.sleep(0.2)
		GPIO.output(17,0)
		time.sleep(0.2)	
		if counter >= 5:
			break

		counter = counter + 1
