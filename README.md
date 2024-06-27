# LetterboxdReviews2024

This repository utilizes your personal exported 'reviews' data from your letterboxd account, and adds details like the runtime, box office, budget, directors, actors, and producers to  your exported data through a python web scraping script to retrieve this information from the film's Wikipedia pages. Downstream analysis to follow.

## Instructions

1. **Export your data**- You must have a Letterboxd account to complete the following actions. In letterboxd, navigate to your 'Account Settings' and to the 'Data' tab. Select 'Export your data' and access this zip file in your downloads.

2. **Clone this repository**-

    ```bash
    git clone https://github.com/yourusernam/LetterBodxdReviews2024.git
    ```

3. **Add your exported data**- Extract your `reviews.csv` file, from the 'letterboxd-yourusername-date of export' zip file, and add this `reviews.csv` file to the `data/` folder of your this repository.

4. **Instal required packages**-

    ```bash
    pip install -r requirements.txt
    ```

5. **Collect extra metadata for your watched films**- Fetch extra details on your watched films (Producer, Director, box office, budget, accolades, stars, cinematography, run time, etc.) by running the web scraping script to extract this data from the Wikipedia page for your watched films.

    ``` bash
    python scripts/scrape_metadata.py
    ```

6. **Combine datasets**- Combine your exported 'reviews' data with the newly collected 'scrape_metadata' data into a single, richer data set of your reviews, ratings, films, and their associated details.

    ```bash
    python scripts/combine_data.py
    ```

7. **Analyze your watched films!** Run the analysis script and view the results.

    ```bash
    python analysis_scripts/year_data_analysis.py
    ```

## File structure

- `data/`: Houses the user's added data (`reviews.csv`), and the generated data sets from the `scrape_metadata.py` and `combine_data.py` scripts.
- `scripts/`: this folder contains the scripts for scraping your film's metadata from their wikipedia entries and for combining this data with your personal `reviews.csv` data for easier downstream analysis.
- `analysis_scripts/`: This folder contains the script(s) for analyzing your letterboxd watched films data that has been combined in previous steps.

## `.gitignore`

The `data/` directory has been added to the .gitignore to ensure that a user's personal review data is not committed to thier public repository.
