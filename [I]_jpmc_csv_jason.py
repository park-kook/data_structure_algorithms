import pandas as pd
import json

def excel_to_hierarchical_json(excel_file_path, json_file_path):
    # Read the Excel file
    df = pd.read_excel(excel_file_path)
    
    # Filter the data where year > 2000
    filtered_df = df[df['year'] > 2000]
    
    # Create a dictionary to hold the hierarchical data
    books_by_author = {}
    
    for _, row in filtered_df.iterrows():
        author = row['author']
        book_info = {
            'name': row['name'],
            'year': row['year']
        }
        
        if author not in books_by_author:
            books_by_author[author] = []
        
        books_by_author[author].append(book_info)
    
    # Convert the books_by_author dictionary to the desired JSON format
    data_list = [{author: books} for author, books in books_by_author.items()]
    
    output_data = {
        "data": data_list
    }
    
    # Write the data to a JSON file
    with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
        json.dump(output_data, jsonfile, indent=4)
    
    print(f"Excel data has been successfully converted to hierarchical JSON and saved to {json_file_path}")

# File paths
excel_file_path = 'bookstore.xlsx'
json_file_path = 'bookstore_hierarchical.json'

# Convert Excel to JSON
excel_to_hierarchical_json(excel_file_path, json_file_path)




{
    "data": [
        {
            "J.K. Rowling": [
                {
                    "name": "Harry Potter and the Order of the Phoenix",
                    "year": 2003
                },
                {
                    "name": "Harry Potter and the Deathly Hallows",
                    "year": 2007
                }
            ]
        },
        {
            "Stephen King": [
                {
                    "name": "Book by Stephen King",
                    "year": 2005
                }
            ]
        }
        // Add other authors and their books here
    ]
}
