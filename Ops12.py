import requests

def get_http_method():
    while True:
        method = input("Enter HTTP Method (GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS): ").upper()
        if method in ['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'PATCH', 'OPTIONS']:
            return method
        else:
            print("Invalid HTTP Method. Please enter a valid method.")

def get_destination_url():
    return input("Enter the destination URL: ")

def print_request_info(url, method):
    print(f"\nRequest to be sent:")
    print(f"URL: {url}")
    print(f"HTTP Method: {method}\n")

def confirm_request():
    return input("Do you want to proceed with the request? (yes/no): ").lower() == 'yes'

def translate_status_code(status_code):
    status_codes = {
        200: "OK",
        201: "Created",
        204: "No Content",
        400: "Bad Request",
        401: "Unauthorized",
        403: "Forbidden",
        404: "Not Found",
        500: "Internal Server Error",
    }
    return status_codes.get(status_code, "Unknown Status Code")

def print_response_info(response):
    print("\nResponse Header Information:")
    for key, value in response.headers.items():
        print(f"{key}: {value}")
    print(f"\nStatus Code: {response.status_code} - {translate_status_code(response.status_code)}\n")

def main():
    url = get_destination_url()
    method = get_http_method()

    print_request_info(url, method)

    if confirm_request():
        response = getattr(requests, method.lower())(url)
        print_response_info(response)
    else:
        print("Request canceled.")

if __name__ == "__main__":
    main()


Resource - chatgpt
