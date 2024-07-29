import fastly
from fastly.api import backend_api
from pprint import pprint

# Prompt for Fastly API token
api_token = input("Enter your Fastly API token: ")

# Configuration for the Fastly API
configuration = fastly.Configuration()
configuration.api_token = api_token  # Use the entered API token

# Create an API client using the configured settings
with fastly.ApiClient(configuration) as api_client:
    api_instance = backend_api.BackendApi(api_client)

    # Prompt for service ID and version ID
    service_id = input("Enter the service ID: ")
    version_id = int(input("Enter the version ID: "))

    # Options for the API call
    options = {
        'service_id': service_id,
        'version_id': version_id,
    }

    # Perform the API call to list backends
    try:
        api_response = api_instance.list_backends(**options)
        # Loop through each backend in the response and print the 'ssl_check_cert' value
        for backend in api_response:
            print(f"Backend name: {backend.name}, SSL Check Cert: {backend.ssl_check_cert}")
    except fastly.ApiException as e:
        print(f"Exception when calling BackendApi->list_backends: {e}\n")
