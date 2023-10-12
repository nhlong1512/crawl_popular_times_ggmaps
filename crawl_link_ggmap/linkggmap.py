import csv
from ctypes.wintypes import SERVICE_STATUS_HANDLE
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Initialize Firefox WebDriver and profile
profile = webdriver.FirefoxProfile()
profile.accept_untrusted_certs = True
url_file_driver = os.path.join('etc', 'geckodriver.exe')
service = SERVICE_STATUS_HANDLE(executable_path=url_file_driver, firefox_profile=profile)
driver = webdriver.Firefox(service=service)


# Open the CSV file containing place names and create a new CSV file for results
input_csv_filename = 'Food_HCM2.csv'
output_csv_filename = 'GGMap_HCM2.csv'

with open(input_csv_filename, 'r', newline='', encoding='utf-8') as input_csvfile, \
        open(output_csv_filename, 'w', newline='', encoding='utf-8') as output_csvfile:

    csv_reader = csv.DictReader(input_csvfile)
    fieldnames = csv_reader.fieldnames + ['GoogleMapsURL']  # Add a new column for results
    
    csv_writer = csv.DictWriter(output_csvfile, fieldnames=fieldnames)
    csv_writer.writeheader()
    
    for row in csv_reader:
        place_name = row['PlaceName']
        print(f"Searching for place: {place_name}")
        
        driver.get('https://www.google.com/maps')
        sleep(2)
        
        def searchplace(place_name):
            try:
                Place = driver.find_element(By.ID, 'searchboxinput')
                Place.clear()
                Place.send_keys(place_name)
                
                Submit = driver.find_element(By.XPATH, '//*[@id="searchbox-searchbutton"]')
                Submit.click()
                sleep(5)
                
                l = driver.find_element(By.XPATH, "/html/body/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[5]/button")
                l.click()
                sleep(2)
                
                try:
                    input_element = driver.find_element(By.CLASS_NAME, 'vrsrZe')
                    value = input_element.get_attribute('value')
                except Exception as e:
                    print('Không thể trích xuất link ggmap:', str(e))
                    value = None
                
                return value
            
            except Exception as e:
                print(f"An error occurred while searching for '{place_name}': {str(e)}")
                return None
        
        result = searchplace(place_name)
        row['GoogleMapsURL'] = result  # Add the result to the row
        
        # Write the updated row to the output CSV file
        csv_writer.writerow(row)

# Close the WebDriver when done
driver.quit()
