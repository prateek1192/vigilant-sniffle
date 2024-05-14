import requests
import json


# Function to make a GET request to Grafana API
def get_request(endpoint, params=None):
    headers = {
        "Authorization": f"Bearer {SERVICE_ACCOUNT_TOKEN}",
        "Content-Type": "application/json"
    }
    response = requests.get(f"{GRAFANA_API_URL}/{endpoint}", headers=headers, params=params)
    return response.json()

# Function to make a POST request to Grafana API
def post_request(endpoint, data):
    headers = {
        "Authorization": f"Bearer {SERVICE_ACCOUNT_TOKEN}",
        "Content-Type": "application/json"
    }
    response = requests.post(f"{GRAFANA_API_URL}/{endpoint}", headers=headers, json=data)
    return response

# Function to list all dashboards
def list_dashboards():
    return get_request("search", params={"type": "dash-db"})

# Example: Import a dashboard
def import_dashboard(dashboard_json):
    import_request = {
        "dashboard": dashboard_json,
        "overwrite": False
    }
    # print("Request Body:")
    # print(json.dumps(import_request, indent=4))  # Print request body in JSON format
    response = post_request("dashboards/import", import_request)
    return response

# Example usage
if __name__ == "__main__":
    # List all dashboards
    dashboards = list_dashboards()
    print("List of Dashboards:")
    for dashboard in dashboards:
        print(dashboard["title"])

    # Import a dashboard
    with open("/Users/prateek.arora/go/src/github.com/dwx/charts/istio-addons/charts/grafana/dashboards/nodes/test-dash.json", "r") as file:
        dashboard_json = json.load(file)  # Read JSON content from file
        response = import_dashboard(dashboard_json)
        print("Response status code: ", response.status_code)
        print("Response headers: ", response.headers)
        print("Response body: ", response.text)
