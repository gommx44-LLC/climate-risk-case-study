#!/usr/bin/env python3
"""
This script will read the CSV and calculate the top 5 countries by deaths.
"""

import pandas as pd

def main():
    # Load data
    df = pd.read_csv('data/climate_impact_data_1993-2012.csv')
    
    # Group by country and sum deaths
    country_deaths = df.groupby('Country')['Deaths'].sum().reset_index()
    
    # Sort descending and get top 5
    top5 = country_deaths.sort_values('Deaths', ascending=False).head(5)
    
    # Print results
    print("Top 5 countries by total deaths (1993-2012):")
    for idx, row in top5.iterrows():
        print(f"{row['Country']}: {row['Deaths']} deaths")
    
    # Optionally save to a file
    top5.to_csv('results/top5_countries_by_deaths.csv', index=False)

if __name__ == '__main__':
    main()