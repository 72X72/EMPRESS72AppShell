#!/usr/bin/env python3
import socket, subprocess, os, json, time

log_path = os.path.expanduser("~/empress72/cloud/terrain_access.log")

def log(data):
    with open(log_path, "a") as f:
        f.write(json.dumps(data, indent=2) + "\n")

def get_ip():
    try:
        return subprocess.check_output(["curl", "-s", "https://api.ipify.org"]).decode().strip()
    except:
        return "unreachable"

def check_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    try:
        s.connect(("127.0.0.1", port))
        s.close()
        return True
    except:
        return False

terrain = {
    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
    "public_ip": get_ip(),
    "ssh_port_open": check_port(22),
    "cockpit_port_open": check_port(7272),
    "terrain_valid": os.path.exists("/data/data/com.termux/files/home/empress72/cloud")
}

log(terrain)
print(json.dumps(terrain, indent=2))
