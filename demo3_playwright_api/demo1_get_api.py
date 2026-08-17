from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    api_context = p.request.new_context(base_url="https://petstore.swagger.io/v2/")

    pet_id = 956

    response = api_context.get(
        f"pet/{pet_id}"
    )

    # status
    print("Status:", response.status)

    # body
    body = response.json()
    print(body)

    print(body["id"])
    print(body["category"]["id"])
    print(body["tags"][0])
    api_context.dispose()
    
    print(body["name"].upper())

    body["name"]="don"

    print(body["name"].upper())