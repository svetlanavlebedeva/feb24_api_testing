import requests

session = requests.Session()

session.headers = {"Authorization": "special-key"}
session.verify = False

session.get("https://petstore.swagger.io/v2/pet/findByStatus")
response = session.post("https://petstore.swagger.io/v2/pet", json={
        "name": "doggie",
        "photoUrls": []
    })
print(response.text)



