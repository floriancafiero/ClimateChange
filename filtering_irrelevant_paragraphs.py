# Filtering out the rows where the mentioned_countries is "None"
filtered_data = data[data['mentioned_countries'] != "None"]

# Save the filtered data back to a CSV file
filtered_file_path = '/mnt/data/filtered_final_data_IPCC.csv'
filtered_data.to_csv(filtered_file_path, index=False)

filtered_file_path
