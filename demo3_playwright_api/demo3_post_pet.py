from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    api_context = p.request.new_context()

    status = "sold"

    req_body = {
        "id": 123456,
        "category": {
            "id": 1,
            "name": "dogs"
        },
        "name": "tommy",
        "photoUrls": [
            "https://example.com/dog.jpg"
        ],
        "tags": [
            {
                "id": 1,
                "name": "friendly"
            }
        ],
        "status": "available"
    }

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

    # api_context.dispose()