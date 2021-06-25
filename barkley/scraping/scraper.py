from selenium import webdriver
import json

class Scraper:

    def __init__(self, ROOT_DOMAIN):
        self.ROOT_DOMAIN = ROOT_DOMAIN
        self.driver = webdriver.Firefox()

    def get_first_page(self):
        self.driver.get(self.ROOT_DOMAIN)
        self.driver.implicitly_wait(4)


    def get_page_by_url(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(4)


    def read_json(self, fpath):
        with open(fpath, 'r') as f:
            data = json.loads(f.read())
        return data


    def write_to_json(self, data, fpath):
        with open(fpath, 'w') as f:
            data = f.write(json.dumps(data))
        print(f'<{data}> is saved to {fpath}')


    def close(self):
        self.driver.close()
