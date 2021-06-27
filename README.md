# bark-ley project

According to the research of pet insurers MORE TH>N, five dogs go missing in the UK every single day. This means that 10% of dog owners in Britain have sadly experienced their dog go missing at least once in their lives. Bark-ley is started as a small gesture to help this situation. 

Currently, missing/found/stray dog data is scattered on multiple websites with different structures of data. Some websites have well-structured data while some rely on vague descriptions. The data is also focused on the dog only, even though data of the last seen place might be crucial to find the missing dog. The goal of this project is to create a centralised dataset, which is consisting of dog and location-based data.


### Directory Structure

```bash
├── barkley
│   ├── data
│   ├── scraping
│   │   ├── __init__.py
│   │   ├── scraper.py
│   │   ├── district_scraper.py
│   │   ├── doglost_scraper.py
│   │   └── vet_scraper.py
│   │
│   ├── processing
│   │   ├── __init__.py
│   │   ├── process_district_data.py
│   │   ├── process_vet_data.py
│   │   └── doglost_data.py
│   │
│   └── database
│       ├── __init__.py
│       └── insertion.py
├── .gitignore
├── README.md
└── requirements.txt
```


### Steps

1) Data Scraping
- scraper.py : template for all scraper classes
- district_scraper.py : collects district information
- doglost_scraper.py : collects missing dog data
- vet_scraper.py : collects veterinary practice data


2) Data Processing

- process_district_data.py : creates a matrix of distances between districts 
- process_vet_data.py : creates dictionary to map vets in a certain district
- doglost_data.py : cleans the missing dog dataset and adds extracted information


3) Data Insertion in Cloud(AWS RDS)
- insertion.py : inserts dataset into a data warehouse

### Summary

- Collected data:<br/>
  8655 missing dog data<br/>
  5271 vets<br/>
  2959 districts data<br/>

- The dataset is saved in a data warehouse
- Multiple scraper is created by using class inheritance
- Multi-threading is used for a scraper


