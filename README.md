# RIPA-2018-datasette
Publishing datasette of CA's RIPA 2018 data

_Assembly Bill 953 requires each state and local agency in California that employs peace officers to annually report to the Attorney General data on all stops, as defined in Government Code 12525.5(g)(2), conducted by the agency's peace officers. The bill requires the collected data to include specified information, including the time, identity, date and location of the stop, and the reason for the stop. The current dataset (RIPA Stop Data.csv)  is composed of data collected by the eight largest agencies in the state between July and December of 2018._

Data can be found on the California's DOJ Open Data website: https://openjustice.doj.ca.gov/data

Direct link to data: https://data-openjustice.doj.ca.gov/sites/default/files/dataset/2020-01/RIPA%20Stop%20Data%202018.csv

Data README: https://data-openjustice.doj.ca.gov/sites/default/files/dataset/2020-01/RIPA%20Dataset%20Read%20Me%2020200106.pdf

***
The dataset is 1.8 million rows and 143 columns (around 650 MB). This is too large to serve as one table. It is also unnecessarily cumbersome. There's a datasette instance serving it at <http://ripa-2018.herokuapp.com>. 
The goal of this project is to deploy a _"broken down"_ version of this where each subset of columns (`ROS_`, `G_`, `RAE_`, etc) is its own table. Each stop instance has an attached `DOJ_RECORD_ID` and each person stopped is assigned a `PERSON_NUMBER`. 
The first attempt at _"breaking down"_ this dataset created a `UNIQUE_INDEX` by combining `DOJ_RECORD_ID` and `PERSON_NUMBER` and using this to connect each table to one another. 
There's a draft of this idea already at <https://ripa-2018-db.herokuapp.com>. 

However, this still takes too long to work. Heroku apps timeout after 30 seconds so if a query takes longer than that it will error out. A simple query aggregating number of people of each race/ethnicity by agency takes between 28 and 31 seconds so it sometimes errors out and others it doesn't. 

TODO:
- Create "smaller" `unique_id` that could potentially save memory. Right now `UNIQUE_INDEX` is a 22 character string. Potentially, all we need is a seven digit numeric id. 
- Automate deployment:
  - Ideally, as the project evolves we can include useful table views and queries (included in the metadata). However, datasette doesn't allow you to "update" a deployment's metadata, one must deploy the app altogether. 
    This means that even thought the underlying SQLite database might be created/transformed very few times, it must be included in each deployment which is a heavy process. As of now, the database is 1.1 gb.  
