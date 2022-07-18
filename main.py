import requests
from datetime import datetime

gender = "male"
weight_kg = "70"
height_cm = "1.70"
AGE = "33"
add_row_sheety_endpoint = "your sheety add row endpoint"
nutrition_app_id = "app id from nutrition page"
nutrition_api_key = "api key from nutrition page"
exercise_endpoint = "exercice page endpoint"
exercise_text = input("Tell me which exercises you did: ")

headers = {"x-app-id": nutrition_app_id,
           "x-app-key": nutrition_api_key,
           }
parameters = {
    "query": exercise_text,
    "gender": gender,
    "weight_kg": weight_kg,
    "height_cm": height_cm,
    "age": AGE
}

response_nutrition = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response_nutrition.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]

        }
    }

    sheet_response = requests.post(add_row_sheety_endpoint, json=sheet_inputs)

    print(sheet_response.text)
