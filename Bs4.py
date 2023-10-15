import sys
import requests
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from datetime import date
from datetime import datetime
# scraper
def scrape(url,model):
    global item
    # openning url in chrome
    driver = webdriver.Chrome('./chromedriver') 
    driver.get(url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    button = driver.find_element(By.CSS_SELECTOR,'section[data-load-more="next"] button.button.small.square-round.bordered')
    button.click()
    time.sleep(1)

    # passing url to bs4
    soup = BeautifulSoup(driver.page_source, "lxml")
    cars = soup.find_all('article', class_='serp-item list')
    for car in cars:
        car_url = car.find('a')['href']
        if (car.img['src'] != "/img/empty.png"):
            img = car.img['src']
        else:
            img = car.find('img', class_='lazy')['data-src']
            
        print(f'ITEM: {item + 1}')
        print('IMG: ' + img)
        print("URL: " + car_url)
        print('DATE: ' + str(date.today()) )
        
        # Save to file
        session = requests.Session()
        session.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
        temp = session.get(img , allow_redirects=True)
        print(f'HTTPS: {temp.status_code}')
        print('---------------------')

        directory_path = f'C:/Users/mhmds/Desktop/Soup/{model}' # Replace with the desired directory path
        # current_datetime = datetime.now()
        # folder_name = str(current_datetime.strftime("%Y-%m-%d %H.%M.%S"))
        folder_name = str(date.today())
        # Create a new folder in the specified directory
        os.makedirs(os.path.join(directory_path, folder_name), exist_ok=True)
        ifile = open(rf'C:\Users\mhmds\Desktop\Soup\{model}\{folder_name}\{item+1}.jpg' ,'wb')
        ifile.write(temp.content)

        item +=1
        
        if item == 100:
            sys.exit()
# passing the model and url to scrapper function
def option(model):
    if model == '206':
        urls = ['https://www.sheypoor.com/s/tehran-province/vehicles/car?q=206&wi=1','https://www.sheypoor.com/s/mazandaran/vehicles/car?q=206&wi=1', 'https://www.sheypoor.com/s/alborz/vehicles/car?q=206&wi=1','https://www.sheypoor.com/s/isfahan-province/vehicles/car?q=206&wi=1']
        for url in urls:
            scrape(url,model)
    elif model == '111':
        urls = ['https://www.sheypoor.com/s/tehran-province/vehicles/car?q=111&wi=1','https://www.sheypoor.com/s/mazandaran/vehicles/car?q=111&wi=1','https://www.sheypoor.com/s/isfahan-province/vehicles/car?q=111&wi=1','https://www.sheypoor.com/s/alborz/vehicles/car?q=111&wi=1']
        for url in urls:    
            scrape(url,model)
    elif model == '405':
        urls = ['https://www.sheypoor.com/s/tehran-province/vehicles/car?q=405&wi=1','https://www.sheypoor.com/s/mazandaran/vehicles/car?q=405&wi=1', 'https://www.sheypoor.com/s/alborz/vehicles/car?q=405&wi=1','https://www.sheypoor.com/s/isfahan-province/vehicles/car?q=405&wi=1']
        for url in urls:    
            scrape(url,model)
    elif model == '207':
        urls = ['https://www.sheypoor.com/s/tehran-province/vehicles/car?q=207&wi=1','https://www.sheypoor.com/s/mazandaran/vehicles/car?q=207&wi=1', 'https://www.sheypoor.com/s/alborz/vehicles/car?q=207&wi=1','https://www.sheypoor.com/s/isfahan-province/vehicles/car?q=207&wi=1']
        for url in urls:    
            scrape(url,model)
    else:
        print('NOT SUPPURTED!!!')
        print('---------------------')
        print('Suppurted Models: 111 206 207 405')
        option(input('Try Again >> '))

item = 0
os.system('cls')
print('Suppurted Models: 111 206 207 405')
option(input('Model >> '))