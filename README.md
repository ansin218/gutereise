# Gute Reise

* Tracks prices between Munich (MUC) and Chennai (MAA), Mumbai (BOM), Delhi (DEL), Kolkata (CCU) and Bengaluru (BLR) for all available operating airlines.
* Tracks flights every day with departure day being 1, 7, 15, 30, 60 and 90 days after current day.
* Tracks return flights with 20 days window between departure date and return date.

## Setup

* Clone or download this directory.
* Sign up for the API here: https://developers.amadeus.com/
* Create a file API_KEY.txt to enter the `client_id` and `client_secret` in one single seperate by single space character.
* Run the `price_scraper.py` file.
* Data grabbed can be found inside `data` folder in xlsx format.

## Disclaimer

* The following project has been created by the author strictly for educational purposes such as studying airline pricing.
* The author is not responsible if the scraper breaks in future due to changes applied at target website's end.
* Data for some airlines may be missing due to the nature of scraping cached data or no available flights on the given date.

## License

The following project is released under MIT license.