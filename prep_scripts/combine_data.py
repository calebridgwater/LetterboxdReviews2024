import pandas as pd
import os

# Load original reviews data and scraped metadata
reviews_file = os.path.join('data', 'reviews.csv')
metadata_file = os.path.join('data', 'movie_metadata.csv')
accolades_file = os.path.join('data', 'movie_accolades.csv')

reviews_df = pd.read_csv(reviews_file)
metadata_df = pd.read_csv(metadata_file)
accolades_df = pd.read_csv(accolades_file)

# Merge the original reviews data with the scraped movie data
combined_df = reviews_df.merge(metadata_df, left_on='Name', right_on='Title', how='left')

# Save the combined data to Excel
combined_output_file = os.path.join('data', 'combined_movie_data.xlsx')
combined_df.to_csv(combined_output_file, sheet_name='Movies', index=False)
accolades_df.to_csv(combined_output_file, sheet_name='Accolades', index=False, startrow=len(combined_df) + 2)

print(f"Data combination complete. Saved to {combined_output_file}")
