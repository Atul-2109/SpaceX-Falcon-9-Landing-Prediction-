Data Collection with Web Scraping is performed to collect Falcon 9 historical launch records from a Wikipedia page titled `List of Falcon 9 and Falcon Heavy launches`
<br> https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches<br>

Objectives:<br>
Web scrap Falcon 9 launch records with `BeautifulSoup`: <br>
- Extract a Falcon 9 launch records HTML table from Wikipedia,<br>
- Parse the table and convert it into a Pandas data frame<br>

And,<br>

Data Wrangling:<br>
Here, we perform some <u>Exploratory Data Analysis (EDA)</u> to find some patterns in the data and determine what would be the label
for training supervised models. <br> 
In the data set, there are several different cases where the booster did not land successfully. Sometimes a landing was attempted <br> 
but failed due to an accident; for example <br>
<code>True Ocean</code> means the mission outcome was successfully landed to a specific region of the ocean.  <br>
<code>False Ocean</code> means the mission outcome was unsuccessfully landed to a specific region of the ocean.  <br>
<code>True RTLS</code> means the mission outcome was successfully landed to a ground pad. <br>
<code>False RTLS</code> means the mission outcome was unsuccessfully landed to a ground pad. <br>
<code>True ASDS</code> means the mission outcome was successfully landed on  a drone ship. <br>
<code>False ASDS</code> means the mission outcome was unsuccessfully landed on a drone ship. 

Here, we mainly convert those outcomes into Training Labels with `1` means the booster successfully landed `0` means it was unsuccessful.

Objectives<br>
Perform exploratory  Data Analysis and determine Training Labels <br>
- Exploratory Data Analysis<br>
- Determine Training Labels <br>
