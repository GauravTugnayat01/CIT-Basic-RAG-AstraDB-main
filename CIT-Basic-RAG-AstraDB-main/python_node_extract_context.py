import warnings
from promptflow.core import tool
import json

# Ignore specific warnings
warnings.filterwarnings("ignore", category=DeprecationWarning, module="promptflow")

@tool
def my_python_tool(input1: str) -> str:
    # Parse the JSON string to a list of dictionaries
    documents = json.loads(input1)
    
    # Extract only the 'content' from each document
    content_list = [doc['text'] for doc in documents if 'text' in doc]
    
    # Join the content into a single string, or format as needed
    content_list2 =  "\n\n".join(content_list)
    content_list2 = content_list2.replace("+","")
    return content_list2
