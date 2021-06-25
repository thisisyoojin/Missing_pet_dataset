Barkley dataset

.
├── barkley
│   ├── data
│   ├── resources
│   ├── scraping
│   │   ├── __init__.py - download postcode file + extract distrct unique
│   │   ├── scraper.py
│   │   ├── warden_scraper.py
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


-pipenv install -r requirements.txt
