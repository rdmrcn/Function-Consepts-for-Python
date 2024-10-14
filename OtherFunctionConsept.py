import random

# Function to fetch nominees from a fictional data source
def fetch_nominees_from_source(year, category):
    # Example: Generate random nominees
    nominees = []
    for i in range(5):  # Let's assume there are 5 nominees for each category
        nominee = {
            "name": f"Nominee {i+1}",
            "category": category,
            "year": year
        }
        nominees.append(nominee)
    return nominees

# Function to get Oscar nominees
def get_oscar_nominees(year, category):
    # Code to fetch nominees for the given year and category
    nominees = fetch_nominees_from_source(year, category)
    return nominees

# Example usage:
year = 2023
category = "Best Picture"
nominees = get_oscar_nominees(year, category)
print(f"Oscar Nominees for {year} - {category}:")
for nominee in nominees:
    print(nominee["name"])






def get_oscar_nominees(year, category):
    # Code to fetch nominees for the given year and category
    # Assume nominees are fetched and stored in a list
    nominees = fetch_nominees_from_source(year, category)
    return nominees

# Example usage:
year = 2023
category = "Best Picture"
nominees = get_oscar_nominees(year, category)
print(f"Oscar Nominees for {year} - {category}:")
for nominee in nominees:
    print(nominee)
