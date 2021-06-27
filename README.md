# bark-ley project

Bark-ley project is data engineering project on the purpose of creating centralised dataset for missing dog data.
Based on the last seen place(where they are lost), I created 



### Structure

```bash
├── barkley
│   ├── data - where collected/processed data is saved
│   ├── scraping
│   │   ├── __init__.py
│   │   ├── scraper.py - template for all scraper classes
│   │   ├── district_scraper.py - what collects district information
│   │   ├── doglost_scraper.py - what collects missing dog data
│   │   └── vet_scraper.py - what collects veterinary practice data
│   │
│   ├── processing
│   │   ├── __init__.py
│   │   ├── process_district_data.py - creates a matrix of distances between districts 
│   │   ├── process_vet_data.py - creates dictionary to map vets in a certain district
│   │   └── doglost_data.py - cleans the missing dog dataset and adds extracted information
│   │
│   └── database
│       ├── __init__.py - create engine
│       └── insertion.py - each data
├── .gitignore
├── README.md
└── requirements.txt
```


### Step

1) Data Scraping



2) Data Processing

The data was downloadaed from here:
- from collected district data, populations
- from collected district data, calculate the distance between districts
- Based on this distance table, 



3) Data Insertion in Cloud(AWS RDS)

