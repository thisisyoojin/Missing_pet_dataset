# bark-ley project

Bark-ley project is data engineering project on the purpose of creating centralised dataset for missing dog data.

Based on the last seen place(where they are lost), I created 


### Step

1) Data Scraping

2) Data Processing

The data was downloadaed from here:
- from collected district data, populations
- from collected district data, calculate the distance between districts
- Based on this distance table, 

### Structure

```bash
├── barkley
│   ├── data
│   ├── resources
│   ├── scraping
│   │   ├── __init__.py - download postcode file + extract distrct unique
│   │   ├── scraper.py
│   │   ├── district_scraper.py
│   │   ├── doglost_scraper.py
│   │   └── vet_scraper.py
│   ├── processing
│   │   ├── __init__.py
│   │   ├── district_data.py - create distances, combine warden > district.json
│   │   ├── vet_data.py - clean the data, create nearest by area > vets.json
│   │   └── doglost_data.py - clean the dataset, combine with distrct data, vet data > pets.json
│   └── database
│       ├── __init__.py - create engine
│       └── insertion.py - each data,
├── .gitignore
├── README.md
└── requirements.txt
```

