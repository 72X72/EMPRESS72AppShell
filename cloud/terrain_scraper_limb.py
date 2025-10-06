#!/usr/bin/env python3
import os, platform, socket, subprocess, json, time

log_path = os.path.expanduser("~/empress72/cloud/terrain_map.log")

def log(data):
    with open(log_path, "a") as f:
        f.write(json.dumps(data, indent=2) + "\n")

def check_port_bind():
    try:
        s = socket.socket()
        s.bind(("127.0.0.1", 9999))
        s.close()
        return True
    except:
        return False

def check_proc_access():
    return os.path.exists("/proc") and os.access("/proc", os.R_OK)

def check_passwd():
    return os.path.exists("/etc/passwd")

def check_daemon_support():
    return any(os.path.exists(p) for p in ["/etc/init.d", "/lib/systemd", "/usr/lib/systemd"])

def check_elevation_paths():
    paths = ["sudo", "su", "doas", "polkit", "capsh", "setuid"]
    found = []
    for p in paths:
        if subprocess.call(["which", p], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0:
            found.append(p)
    return found

def scrape_android_intents():
    try:
        result = subprocess.check_output(["pm", "list", "packages"]).decode()
        return "android_intents_accessible"
    except:
        return "no_android_intents"

def scrape_cloud_metadata():
    try:
        result = subprocess.check_output(["curl", "-s", "http://169.254.169.254/latest/meta-data/"]).decode()
        return "cloud_metadata_accessible"
    except:
        return "no_cloud_metadata"

terrain = {
    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
    "os": platform.system(),
    "platform": platform.platform(),
    "can_bind_ports": check_port_bind(),
    "can_access_proc": check_proc_access(),
    "passwd_exists": check_passwd(),
    "daemon_support": check_daemon_support(),
    "elevation_paths": check_elevation_paths(),
    "android_intents": scrape_android_intents(),
    "cloud_metadata": scrape_cloud_metadata(),
    "terrain_valid": os.path.exists(os.path.expanduser("~/empress72/cloud"))
}

log(terrain)
print(json.dumps(terrain, indent=2))
