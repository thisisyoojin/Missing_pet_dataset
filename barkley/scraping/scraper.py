from selenium import webdriver
import json
import time
import os
import requests

class Scraper:

    def __init__(self, ROOT_DOMAIN, option=None):
        self.ROOT_DOMAIN = ROOT_DOMAIN
        self.option = option
        self.driver = None

    def start(self):
        self.driver = webdriver.Firefox(self.option)

    def get_page_by_url(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(4)


    def read_urls(self, fpath):
        if os.path.isfile(fpath):
            with open(fpath, 'r') as f:
                urls = f.readlines()
        else:
            urls = []
        return urls


    def read_json(self, fpath):
        if os.path.isfile(fpath):
            with open(fpath, 'r') as f:
                data = f.read()
        else:
            data = []
        return data


    def write_to_text(self, data, fpath, type='a'):
        with open(fpath, type) as f:
            f.write(data)
        time.sleep(2)


    def write_to_json(self, data, fpath, type='a'):
        with open(fpath, type) as f:
            f.write(json.dumps(data)+'\n')
        


    def save_img_file(self, src_url, fpath):
        response = requests.get(src_url)
        with open(fpath, 'wb+') as f:
            f.write(response.content)


    def close(self):
        self.driver.close()




class UrlScraper(Scraper):
    """
    get_urls_in_current_page

    """

    def __init__(self, ROOT_DOMAIN, next_xpath='', items_xpath='', anchor_xpath=''):
        super().__init__(ROOT_DOMAIN)
        self.urls = []
        self.next_xpath = next_xpath
        self.items_xpath = items_xpath
        self.anchor_xpath = anchor_xpath


    def get_next(self, cur_page):
        try:
            next_page = self.driver.find_element_by_xpath(self.next_xpath).get_attribute('href')
            while cur_page == next_page:
                time.sleep(2)
                next_page = self.driver.find_element_by_xpath(self.next_xpath).get_attribute('href')
            return next_page
        except:
            print('There is no next page.')
            return None


    def get_urls_in_current_page(self):
        urls = []
        items = self.driver.find_elements_by_xpath(self.items_xpath)
        for itm in items:
            url = itm.find_element_by_xpath(self.anchor_xpath).get_attribute('href')
            urls.append(url)
        return urls


    def get_urls_to_file(self, fpath):
        
        self.start()
        current_page = self.ROOT_DOMAIN
        idx, next = 0, True
        
        while next:
            self.get_page_by_url(current_page)
            cur_urls = self.get_urls_in_current_page()
            self.urls.extend(cur_urls)
            
            idx += 1
            print(f"page {idx} is extracted")
            next = self.get_next(current_page)
            current_page = next
            self.write_to_text('\n'+'\n'.join(cur_urls), fpath)

        self.close()
        print('Finished getting urls.')
