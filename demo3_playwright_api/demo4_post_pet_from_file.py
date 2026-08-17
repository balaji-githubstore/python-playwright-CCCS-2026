import json
from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    # Read JSON file
    with open("test_data/new_pet.json", "r") as file:
        req_body = json.load(file)

    api_context = p.request.new_context()

    status = "sold"

    response = api_context.post(
        "https://petstore.swagger.io/v2/pet",
        data=req_body,
        headers={
            "Content-Type": "application/json"
        }
    )

    # Status
    print("Status:", response.status)

    # Body
    body = response.json()
    print(body)

    print(body["id"])
    print(body["category"]["id"])

    api_context.dispose()