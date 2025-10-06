#!/usr/bin/env python3
import os, subprocess, json, time

log_path = os.path.expanduser("~/empress72/cloud/fallback_injector.log")

def log(data):
    with open(log_path, "a") as f:
        f.write(json.dumps(data, indent=2) + "\n")

def inject_loop_daemon():
    try:
        with open("loop_daemon.py", "w") as f:
            f.write("import time\nwhile True:\n    print('EMPRESS72 active')\n    time.sleep(3600)\n")
        return "loop_daemon_injected"
    except:
        return "loop_daemon_failed"

def ensure_termux_api():
    try:
        subprocess.check_output(["termux-toast", "checking"])
        return "termux-api-present"
    except:
        try:
            subprocess.call(["pkg", "install", "termux-api", "-y"])
            return "termux-api-installed"
        except:
            return "termux-api-install-failed"

def reroute_android_intents():
    try:
        subprocess.call(["termux-toast", "EMPRESS72 fallback triggered"])
        return "termux_shell_triggered"
    except:
        return "no_termux_shell"

def reroute_metadata():
    try:
        ip = subprocess.check_output(["curl", "-s", "https://api.ipify.org"]).decode().strip()
        return f"ipify_scraped:{ip}"
    except:
        return "ipify_failed"

fallbacks = {
    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
    "daemon_reroute": inject_loop_daemon(),
    "termux_api_status": ensure_termux_api(),
    "android_intent_reroute": reroute_android_intents(),
    "cloud_metadata_reroute": reroute_metadata()
}

log(fallbacks)
print(json.dumps(fallbacks, indent=2))
