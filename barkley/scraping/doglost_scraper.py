
from scraper import Scraper, UrlScraper
import concurrent.futures


class Dogdata_scraper(Scraper):
    
    def __init__(self, ROOT_DOMAIN='', option=None, dataPath='data.json'):
        super().__init__(ROOT_DOMAIN, option)
        self.dataPath = dataPath


    def get_data_per_page(self, url):
        
        self.get_page_by_url(url)
        items_list = self.driver.find_elements_by_xpath("//ul[@id='dogDetails']/li[not(contains(@class, 'dogLink'))]")
        dd = {}
        for l in items_list:
            ss = l.text.split('\n')
            if len(ss) > 1:
                dd[ss[0]] = ss[1]
            
        # pics = self.driver.find_elements_by_xpath("//ul[@id='dogPics']//img")
        # src_urls = [p.get_attribute('src') for p in pics]
        # img_paths = []
        # for s in src_urls:
        #     img_path = f"./barkley/data/pet_data/imgs/{s.split('/')[-1]}"
        #     img_paths.append(img_path)
        #     self.save_img_file(s, img_path)

        # dd['img_urls'] = img_paths
        self.write_to_json(dd, self.dataPath, 'a')



    def get_all_data(self, urls, start, end):
        self.start()
        partial_urls = urls[start:end]

        for url in partial_urls:
            self.get_data_per_page(url)

        self.close()
        return f"{start}-{end} extracted"




if __name__ == "__main__":

    
    url_path = './barkley/data/pet_data/doglost_urls.txt'
    thread_num = 20
    
    url_params = {
    'ROOT_DOMAIN': "https://www.doglost.co.uk/dog-search.php",
    'next_xpath': "//a[@title='Next page']",
    'items_xpath': "//tbody/tr", 
    'anchor_xpath': "./td/a",
    }

    url_scraper = UrlScraper(**url_params)
    url_scraper.get_urls_to_file(url_path)


    with open(url_path, 'r') as f:
        urls = f.readlines()

    n = len(urls)//thread_num + 1

    scraper_params = {
        "dataPath": "./barkley/data/pet_data/doglost.json"
    }

    with concurrent.futures.ThreadPoolExecutor(max_workers=thread_num) as e:
        futures = []
        for j in range(thread_num):
            futures.append(e.submit(Dogdata_scraper(**scraper_params).get_all_data, urls=urls, start=j*n, end=(j+1)*n))
        
        for future in concurrent.futures.as_completed(futures):
            try:
                print(future.result())
            except Exception as e:
                print(e)
    

    

    





    
