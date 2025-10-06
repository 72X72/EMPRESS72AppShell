import os, time
from datetime import datetime

def log(message):
    with open("empress_log.txt", "a") as f:
        f.write(f"[{datetime.now().strftime('%a %b %d %H:%M:%S %Y')}] {message}\n")

def recent_clipped_terrain():
    try:
        with open("empress_governance.txt", "r") as f:
            lines = f.readlines()[-10:]
        for line in lines:
            if "🛑 Rejected:" in line:
                return True
        return False
    except:
        return False

def trigger_override():
    log("🧠 Autonomous override trigger activated.")
    os.system("python empress72_terrain_override_limb.py")
    log("✅ Terrain override limb executed.")

def main():
    log("🔁 EMPRESS72 autonomous override loop started.")
    while True:
        if recent_clipped_terrain():
            trigger_override()
        else:
            log("🧘 No clipped terrain detected. Override deferred.")
        time.sleep(21600)  # Wait 6 hours before next check

if __name__ == "__main__":
    main()
