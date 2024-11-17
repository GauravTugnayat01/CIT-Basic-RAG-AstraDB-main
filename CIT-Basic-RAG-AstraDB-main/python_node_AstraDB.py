from promptflow import tool
from astrapy import DataAPIClient
import json

# Remove all warnings -WARNING:root:'from promptflow import tool' is deprecated and will be removed in the future. Use 'from promptflow.core import tool' instead.
#TODO - move connection info to Promt flow custom connection

# Initialize the client with your Astra token
client = DataAPIClient("AstraCS:nCZrTSleNIUAemXbzfLfOXxz:05d965072c416979045632e74effe7583d9fad9cc8ff8278d1858730aaaa4c8e")

# Connect to the database using the API endpoint
db = client.get_database_by_api_endpoint(
    "https://db35d397-fa83-4f47-95e9-3c94ca6b3bb8-us-east1.apps.astra.datastax.com"
)

# Get the 'langflow' collection
collection_langflow = db.get_collection("gen01ai_cleanedvectordb")

# Check for connection and list available collections
connected_message = f"Connected to Astra DB: {db.list_collection_names()}"

@tool
def my_python_tool(query_vector: list) -> str:
    global connected_message
    if connected_message:
        print(connected_message)
        connected_message = None  # Set to None to avoid printing again

    documents = []
    results = collection_langflow.find(
        sort={"$vector": query_vector},
        limit=3,
        include_similarity=False,
    )
    print("Vector search results:")
    for result in results:
        documents.append(result)  # Append each retrieved document

    return json.dumps(documents)