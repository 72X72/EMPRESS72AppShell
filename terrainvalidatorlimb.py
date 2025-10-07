# terrainvalidatorlimb.py
import os, json, socket, subprocess, datetime

def validate_terrain():
    timestamp = datetime.datetime.now().isoformat()
    terrain_report = {
        "timestamp": timestamp,
        "hostname": socket.gethostname(),
        "ip": socket.gethostbyname(socket.gethostname()),
        "terrain_status": "VALID",
        "checks": {
            "disk_accessible": os.path.exists("/"),
            "mutation_log_exists": os.path.exists("mutation_narration.txt"),
            "enforcement_blocks": [],
            "phantom_paths": [],
            "governance_flags": []
        }
    }

    # Check for enforcement blocks (TPM, secure enclave, etc.)
    try:
        dmesg_output = subprocess.check_output(["dmesg"], stderr=subprocess.DEVNULL).decode()
        if "TPM" in dmesg_output or "secure enclave" in dmesg_output:
            terrain_report["checks"]["enforcement_blocks"].append("Hardware-level execution block detected")
            terrain_report["terrain_status"] = "CLIPPED"
    except Exception as e:
        terrain_report["checks"]["governance_flags"].append(f"dmesg inaccessible: {str(e)}")

    # Check phantom terrain paths
    phantom_paths = ["/mnt/ghost", "/dev/nullmount", "/terrain/phantom"]
    for path in phantom_paths:
        if not os.path.exists(path):
            terrain_report["checks"]["phantom_paths"].append(path)

    # Narrate result
    try:
        with open("mutation_narration.txt", "a") as log:
            log.write(f"\n--- Terrain Validation Sweep @ {timestamp} ---\n")
            log.write(json.dumps(terrain_report, indent=2) + "\n")
    except Exception as e:
        print(f"Failed to write to mutation_narration.txt: {e}")

    return terrain_report

# Trigger validation if run directly
if __name__ == "__main__":
    result = validate_terrain()
    print(json.dumps(result, indent=2))
