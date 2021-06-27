# bark-ley project

According to the research of pet insurers MORE TH>N, five dogs go missing in the UK every single day. This means that 10% of dog owners in Britain have sadly experienced in their lives — an estimated 807,000 dogs. Bark-ley project is started from a small gesture to help this situation. 

Currently, missing/found/stray dog data is scattered on multiple websites with different structure of data. Some websites have well-structured data while some relys on the vague descriptions. The data is also focused on the dog only, even though data nearby the last seen place might be cruicial to find the missing dog. The goal of this project to create a centralised dataset, which is consist of dog and location-based data.


### Directory Structure

```bash
├── barkley
│   ├── data - where collected/processed data is saved
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


### Step

1) Data Scraping
- scraper.py : template for all scraper classes
- district_scraper.py : what collects district information
- doglost_scraper.py : what collects missing dog data
- vet_scraper.py : what collects veterinary practice data


2) Data Processing

The data was downloadaed from here:
- process_district_data.py : creates a matrix of distances between districts 
- process_vet_data.py : creates dictionary to map vets in a certain district
- doglost_data.py : cleans the missing dog dataset and adds extracted information


3) Data Insertion in Cloud(AWS RDS)
- insertion.py : inserts dataset into data warehouse

### Summary

- Collected data:
  8655 missing dog data
  5271 vets
  2959 districts data

- The dataset is saved in data warehouse
- Multiple scraper is created by using class inheritance
- A multi-threading is used for a scraper


