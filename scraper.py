from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import sys

driver = webdriver.Firefox()

# uncomment if using Phantomjs
#driver = webdriver.PhantomJS()

url = 'http://regsys.fbr.gov.pk/Registration/onlinesearchTaxpayer.aspx?rand=2'
driver.get(url)
cardNumber = '3540437900355'
try:
	dropDown = driver.find_element_by_id('ctl00_ContentPlaceHolder1_ctrlOnlineSearch_ddlSearchType')
	for option in dropDown.find_elements_by_tag_name('option'):
		if option.text == "CNIC":
			option.click()
	sleep(3)
	searchButton = driver.find_element_by_id('ctl00_ContentPlaceHolder1_ctrlOnlineSearch_btnSearch')
	textField = driver.find_element_by_id('ctl00_ContentPlaceHolder1_ctrlOnlineSearch_txtSearch2')
	#textField = driver.find_element_by_id('PralAJAXControls_ctl00_ContentPlaceHolder1_ctrlOnlineSearch_txtSearch2__')
	#textField = driver.find_element_by_name('ctl00$ContentPlaceHolder1$ctrlOnlineSearch$txtSearch2')
	textField.send_keys(cardNumber)
	searchButton.click()
except:
	print "Error: "+str(sys.exc_info())+" at line: "+str(sys.exc_traceback.tb_lineno)
	exit(-1)
