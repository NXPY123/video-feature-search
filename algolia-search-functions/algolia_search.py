
import os
from algoliasearch.search_client import SearchClient


def search(query_string):
    # Connect and authenticate with your Algolia app
    client = SearchClient.create(os.environ["ALGOLIA_APP_ID"], os.environ["ALGOLIA_API_KEY"])
    index_name = "firebase-search-index"
    index = client.init_index(index_name)
    res = index.search(query_string)
    # Search the index and print the results

    return res
