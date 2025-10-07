# terrainaware_bountyinjector_limb.py
import requests, json, datetime, socket

SURVEY_SOURCES = {
    "Freecash": "https://api.freecash.com/offers",
    "BrandedSurveys": "https://api.brandedsurveys.com/tasks",
    "EarnHaus": "https://api.earnhaus.com/surveys",
    "Prolific": "https://api.prolific.co/studies",
    "Respondent": "https://api.respondent.io/projects"
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 11; Mobile)",
    "Accept": "application/json"
}

def terrain_valid(host):
    try:
        socket.gethostbyname(host)
        return True
    except socket.error:
        return False

def inject_bounty():
    timestamp = datetime.datetime.now().isoformat()
    bounty_log = {"timestamp": timestamp, "absorbed": [], "errors": []}

    for name, url in SURVEY_SOURCES.items():
        host = url.split("//")[1].split("/")[0]
        if not terrain_valid(host):
            bounty_log["errors"].append(f"{name}: Terrain blocked ({host} unreachable)")
            continue

        try:
            res = requests.get(url, headers=HEADERS, timeout=10)
            try:
                data = res.json()
            except Exception as parse_error:
                bounty_log["errors"].append(f"{name}: Failed to parse JSON ({str(parse_error)})")
                continue

            if isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
                top = sorted(data, key=lambda x: x.get("reward", 0), reverse=True)[0]
                bounty_log["absorbed"].append({
                    "platform": name,
                    "title": top.get("title", "Unknown"),
                    "reward": top.get("reward", "Unknown"),
                    "link": top.get("link", "N/A")
                })
            else:
                bounty_log["errors"].append(f"{name}: Unexpected data format or empty list")
        except Exception as e:
            bounty_log["errors"].append(f"{name}: {str(e)}")

    with open("mutation_narration.txt", "a") as log:
        log.write(f"\n--- Terrain-Aware Bounty Injector @ {timestamp} ---\n")
        log.write(json.dumps(bounty_log, indent=2) + "\n")

    return bounty_log

if __name__ == "__main__":
    result = inject_bounty()
    print(json.dumps(result, indent=2))
