import requests

BASE_URL = "http://20.207.122.201/evaluation-service"
TOKEN = "PASTE_YOUR_ACCESS_TOKEN_HERE"


def fetch_data(endpoint):
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(BASE_URL + endpoint, headers=headers)
    return response.json()


def select_best_tasks(vehicles, max_hours):
    dp = [0] * (max_hours + 1)
    selected = [[] for _ in range(max_hours + 1)]

    for vehicle in vehicles:
        duration = vehicle["Duration"]
        impact = vehicle["Impact"]

        for hour in range(max_hours, duration - 1, -1):
            new_impact = dp[hour - duration] + impact

            if new_impact > dp[hour]:
                dp[hour] = new_impact
                selected[hour] = selected[hour - duration] + [vehicle]

    return selected[max_hours], dp[max_hours]


depots = fetch_data("/depots")["depots"]
vehicles = fetch_data("/vehicles")["vehicles"]

for depot in depots:
    hours = depot["MechanicHours"]
    tasks, impact = select_best_tasks(vehicles, hours)
    used_hours = sum(task["Duration"] for task in tasks)

    print("\nDepot:", depot["ID"])
    print("Available Hours:", hours)
    print("Used Hours:", used_hours)
    print("Total Impact:", impact)
    print("Selected Tasks:")

    for task in tasks:
        print(task["TaskID"], "| Duration:", task["Duration"], "| Impact:", task["Impact"])