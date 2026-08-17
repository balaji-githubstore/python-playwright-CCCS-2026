from playwright.sync_api import sync_playwright

status="available"

with sync_playwright() as p:
    api_context=p.request.new_context()
    response = api_context.get(f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}")

    print(response.status)
    print(response.json()[0])