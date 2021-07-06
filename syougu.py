import json
import csv
import requests


KEYID = "1b9d61a49a052442"
COUNT = 100
PREF = "Z011"
FREEWORD = "静岡駅"
FORMAT = "json"

PARAMS = {"key": KEYID, "count":COUNT, "large_area":PREF, "keyword":FREEWORD, "format":FORMAT}

def write_data_to_csv(params):
    restaurants = [["名称","営業日","住所","アクセス"]]
    json_res = requests.get("http://webservice.recruit.co.jp/hotpepper/gourmet/v1/", params=params).text
    response = json.loads(json_res)
    if "error" in response["results"]:
        return print("エラーが発生しました！")
    for restaurant in response["results"]["shop"]:
        rest_info = [restaurant["name"], restaurant["open"], restaurant["address"], restaurant["access"]]
        restaurants.append(rest_info)
    with open("restaurants_list.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(restaurants)
    return print(restaurants)

write_data_to_csv(PARAMS)
