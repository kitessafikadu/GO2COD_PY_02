# Top 10 Richest Billionaires Scraper
This project is Task 2 of my Python programming internship at [GO2COD](https://go2cod.com.et/). 
It is a web scraping application that retrieves data on the richest billionaires in the world from a specified website,
processes the data, and outputs the top 10 billionaires, including their company, executive name, net worth, and country.

# Introduction
This project uses Python's requests and BeautifulSoup libraries to fetch and parse data from CEOWORLD, a website that publishes a list of the richest billionaires globally. The project then processes this data to extract essential details about each billionaire, ranks them by net worth, and outputs the top 10 to both the console and a CSV file.

## Features
Fetches and parses billionaire data from the web.

Extracts relevant details including:
* Rank
* Company
* Executive Name
* Net Worth
* Country
  
Cleans and processes the net worth data for sorting.
Sorts by net worth in descending order to find the top 10 richest billionaires.
Outputs the top 10 results to the console and saves them to a CSV file.

## Requirements
Python 3.x
### Required Python packages:
* pandas
* requests
* beautifulsoup4
* 
Make sure you have Python 3 installed, then install the required packages.

The top 10 richest billionaires, along with their company, executive name, net worth, and country, will be displayed in the console.
The results will also be saved to a CSV file at the specified location.
Project Structure
plaintext

## Output
The script saves the top 10 richest billionaires to a CSV file named top_ten_richest.csv.
This file will contain the following columns:

* Rank: Position on the richest list
* Company: Associated company or companies
* Executive Name: Name of the billionaire
* Net Worth: Billionaire’s net worth in billions (numeric)
* Country: Country of origin or residence
