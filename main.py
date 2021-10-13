from serpapi import GoogleSearch
import pandas as pd
import json
import openpyxl

params = {
    "engine": "google_maps",
    "q": "Pos Indonesia Pusat",
    "hl": "id",
    "type": "search",
    "location": "Bandung",
    "api_key": "1c33c59f4cb1d26dd31598098acc27c528873a12c11c0f583d6cdcfec5fa6d1d"
}

search = GoogleSearch(params)
results = search.get_dict()

local_results = results['local_results']
data = pd.DataFrame(local_results)
data.to_excel("pos indonesia.xlsx")