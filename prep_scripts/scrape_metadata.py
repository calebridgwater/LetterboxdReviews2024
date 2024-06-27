import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

def get_wikipedia_data(movie_title):
    search_url = f"https://en.wikipedia.org/wiki/{movie_title.replace(' ', '_')}
    response = requests.get(search_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    data = {
        'Title': movie_title,
        'Runtime': None,
        'Director': None,
        'Actors': None,
        'Producers': None,
        'Music': None,
        'Production Companies': None,
        'Distributors': None,
        'Budget': None,
        'Box Office': None
     }

    accolades = []
    
    try:
        infobox = soup.find('table', {'class': 'infobox vevent'})
        if infobox:
            rows = infobox.find_all('tr')
            for row in rows:
                header = row.find('th')
                if header:
                    header_text = header.get_text(' '), strip=True)
                    if 'Running time' in header_text:
                        data['Runtime'] = row.find('td').get_text(' '), strip=True)
                    elif 'Directed by' in header_text:
                        data['Director']= row.find('td').get_text(' ', strip=True)
                    elif 'Starring' in header_text:
                        data['Actors'] = row.find('td').get_text(' ', strip=True)
                    elif 'Produced by' in header_text:
                        data['Producers'] = row.find('td').get_text(' ', strip=True)
                    elif 'Music by' in header_text:
                        data ['Music'] = row.find('td').get_text(' ', strip=True)]
                    elif 'Production company' in header_text:
                        data['Production Companies'] = row.find('td').get_text(' ', strip=True)
                    elif 'Distributed by' in header_text:
                        data['Distributors'] = row.find('td').get_text(' ', strip=True)
                    elif 'Budget' in header_text:
                        data['Budget'] = row.find('td').get_text(' ', strip=True)
                    elif 'Box office' in header_text:
                        data['Box Office'] = row.find('td').get_text(' ', strip=True)
                        
        accolade_selection = soup.find('span', {'id': 'Accolades'})
        if accolade_selection:
            table = accolade_selection.find_next('table')
            if table:
                rows = table.find_all('tr')[1:]  # Skip the header row
                for row in rows:
                    cells = row.find_all('td')
                    if len(cells) >= 3:
                        award = cells[0].get_text(strip=True)
                        category = cells[1].get_text(strip=True)
                        result = cells[2].get_text(strip=True)
                        accolades.append({
                            'Title': movie_title,
                            'Award': award,
                            'Category': category,
                            'Result': result
                        })
    except Exception as e:
        print("An error occurred for {}: {}".format(movie_title, e))}
    
    return data, accolades

# Load movie list from the Excel file
file_path = os.path.join('data', 'reviews.csv')
reviews_df = pd.read_csv(file_path)
movie_titles = reviews_df['Name'].unique()

# Scrape data for each movie
all_movie_data = []
all_accolades = []

for movie in movie_titles:
    print(f"Scraping data for {movie}...")
    movie_data, accolades = get_wikipedia_data(movie)
    all_movie_data.append(movie_data)
    all_accolades.extend(accolades)

# Convert scraped data to DataFrames
movie_data_df = pd.DataFrame(all_movie_data)
accolades_df = pd.DataFrame(all_accolades)

# Save the scraped data to CSV files
movie_data_df.to_csv(os.path.join('data', 'movie_metadata.csv'), index=False)
accolades_df.to_csv(os.path.join('data', 'movie_accolades.csv'), index=False)

print("Data scraping complete. Saved to data/movie_metadata.csv and data/movie_accolades.csv")