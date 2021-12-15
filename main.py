import requests
from datetime import *
import os

print("Hi, I hope you were able to code today!")

####################################################
USERNAME = "yussuf"
TOKEN = os.environ.get("PIXELA_TOKEN")
GRAPHID = "graph-for-coding"
headers = {
    "X-USER-TOKEN": TOKEN
}
####################################################
#####  CREATING A USER IN PIXELA  #####
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint)
# print(response.text)
#####  CREATING A PIXELA TABLE  #####
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params = {
    "id": "graph-for-coding",
    "name": "Coding Graph",
    "unit": "hour",
    "type": "float",
    "color": "momiji"
}
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)
###########################################
##### TODAYS DATE BUT FORMATTED CORRECTLY TO FIT THE "date" PARAMETER IN THE pixel_params  #####
today = datetime.now()
formatted_today = today.strftime("%Y%m%d")
################################################

print(f"Today's date is: {today.date()}")

#####  CREATES A PIXEL INTO THE DATE GIVEN IN THE "date" PARAMETER AND SETS ITS QUANTITY  #####
pixel_params = {
    "date": formatted_today,
    "quantity": input("How many hours did you code today? ")
}
response = requests.post(url=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}", json=pixel_params, headers=headers)
print(response.text)
####################################################################################################################
put_params = {
    "quantity": "20"
}
#####  PUTS/CHANGES A PIXEL  #####
# response = requests.put(url=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{formatted_today}", json=put_params, headers=headers)
# print(response.text)
# response = requests.delete(url=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{formatted_today}", headers=headers)
# print(response.text)