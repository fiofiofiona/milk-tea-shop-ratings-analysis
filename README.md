# Proposal
For my final project, I would like to collect information from Yelp about bubble milk tea shops in Chicago, including their locations, products and prices, ratings and reviews, etc, and analyze these data to see what makes a bubble milk tea shop have high or low ratings. 

Born and raised in Taiwan, I personally love bubble milk tea. But sometimes online ratings and reviews of a bubble milk tea shop may only reflect one aspect of its milk tea (location, price, milk tea sweetness, bubble tasty or not...). Moreover, small businesses can be easily influenced by local customers and neighborhood, while understanding what impacts these environmental factors would bring may be time and effort consuming to many of them. This data analysis project could act as a good practice of utilizing existing data to map and explore relationships between shops and local communities. I will conduct analysis on data on bubble milk tea shops in Chicago, and see if their ratings on Yelp were influenced by the characteristics of the shop and the demographics of the neighborhood and customers. 

To-do list:
- Access data from Yelp fusion API and Google Maps Places API, and filter data for bubble milk tea shops in Chicago
- Analyze these data to locate which area in Chicago has the most and best bubble milk tea shops, in terms of ratings, price, and the variety of products. 
- What are the distributions of age, gender, race and ethnicity groups in each area, and would these variables have any correlation with the ratings, products or prices of local milk tea shops?


# Execution Plan
1. By the end of week 5, I will have collected bubble milk tea shop data from Yelp API and Google Map API, as well as neighborhood demographics from Citfy of Chicago data portal. 

2. By the end of week 6, I will have cleaned all datasets, prepared data for analysis, and completed exploratory data analysis.

3. By the end of week 7, I will conduct analysis to explore correlation between shops characteristics and ratings, and correlation between neighborhood demographics and ratings. 

4. By the end of week 8, I will have finished all data analyses and report. 


## Data collection
1. Yelp Fusion API: accessed stores using "bubble tea" term, at Chicago, IL location, and is_closed status is FALSE
2. Google Maps: only 20 entries available, not used in analysis
3. Chicago Population Counts dataset: from [Chicago City Data Portal](https://data.cityofchicago.org/Health-Human-Services/Chicago-Population-Counts/85cm-7uqa)

## Data Cleaning
Cleaned yelp_data_file.csv
1. Price data was missing in some entries. Reorganized columns "location", "phone", "display_phone", "distance".
2. Aggregated yelp data by region. 

Cleaned population data
1. Extracted 2019 data and kept only data at zip code level.
2. Merged population data and yelp data based on zip codes in population data. 

## Data analysis
* Descriptive: Explored number of bubble tea shops, average rating, average review count, and average price in each zip code region.

* Correlations: How each of these three factors of bubble tea shops correlate with population demographics in each region.
