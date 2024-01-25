def extract_countries(text):
    """
    Extracts a list of countries mentioned in a text, handling non-string inputs.
    Returns "None" if no countries are found.
    """
    countries = set()
    if isinstance(text, str):
        for country in pycountry.countries:
            if country.name in text:
                countries.add(country.name)
    return list(countries) if countries else "None"

# Reapply the function with the updated approach
data['mentioned_countries'] = data['paragraph'].apply(extract_countries)

# Display the first few rows to show the results
data[['paragraph', 'mentioned_countries']].head()
