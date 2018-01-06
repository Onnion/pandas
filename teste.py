from pprint import pprint
from pandas import DataFrame
import json

data_json = json.load(open("data.json"))
data = DataFrame(data_json["data"], columns=["Email","Nome"])

pprint(data)