from selenium import webdriver
import json


class Vet_Scraper:

    def __init__(self):
        self.ROOT_DOMAIN = "https://findavet.rcvs.org.uk/find-a-vet-practice/?filter-choice=location&filter-keyword=+&filter-searchtype=practice#primary-navigation"
        self.driver = webdriver.Firefox()
        self.vets = []

    def get_page(self, domain):
        self.driver.get(domain)
        self.driver.implicitly_wait(5)


    def get_item_info(self):

        divs = self.driver.find_elements_by_xpath("//div[contains(@id, 'item')]")
        for d in divs:
            name, address, post_code, phone, email = None, None, None, None, None
            name = d.find_element_by_xpath(".//h2[@class='item-title']/a").text
            address = d.find_element_by_xpath(".//div[@class='item-address']").text
            post_code = d.find_element_by_xpath(".//div[@class='item-address']/span").text
            
            try:
                phone = d.find_element_by_xpath(".//span[contains(@class, 'tel')]").text.lstrip('phone2 ')
                email = d.find_element_by_xpath(".//a[contains(@class, 'email')]").text.lstrip('envelope ')
            except Exception as e:
                print(e)
            
            finally:
                self.vets.append({'name': name, 'address': address, 'post_code': post_code, 'phone': phone, 'email': email})



    def get_next_page(self):
        
        paging = self.driver.find_element_by_xpath("//ol[@class='paging']/li[@class='next']")
        
        try:
            next = paging.find_element_by_xpath(".//a").get_attribute('href')
        except:
            next = None
        return next

    
    def start_scraping(self):
        
        self.get_page(self.ROOT_DOMAIN)
        idx = 1
        
        while True:
            
            print(f"Page {idx} extracting...")
            self.get_item_info()
            next = self.get_next_page()
            
            if next is None:
                break
            idx += 1

            self.get_page(next)

        return self.vets



if __name__ == "__main__":
    
    vet_scraper = Vet_Scraper()
    vet_data = vet_scraper.start_scraping()
    
    with open(f'data/vets.txt', 'w') as f:
        f.write(json.dumps(vet_data))


