from promptflow import tool
import json
import re

# Function to clean content by removing line breaks, extra spaces, and special characters
def clean_content(content):
    # Remove newline characters, multiple spaces, and spaces around hyphens
    content = re.sub(r'[\n\r]+', ' ', content)  # Remove all newlines and replace with a space
    content = re.sub(r'\s*-\s*', '-', content)  # Remove spaces around hyphens
    content = re.sub(r'\s+', ' ', content)      # Replace multiple spaces with a single space
    # Remove specific Unicode symbols like ® and bullet points
    content = re.sub(r'[\u00ae\u25cf]', '', content)
    return content.strip()  # Remove leading and trailing whitespace

# Tool function for processing JSON input
@tool
def my_python_tool(input1: str, astradbJSON: str) -> str:
    
    astradbJSON = json.loads(astradbJSON)

    # Apply the cleaning function to each item in the JSON array
    for item in astradbJSON:
        if 'content' in item:
            item['content'] = clean_content(item['content'])

   
    return json.dumps(astradbJSON)
