import time, subprocess

def watchdog():
    while True:
        terrain = subprocess.run(["python", "empress72_terrain_scan_limb.py"], capture_output=True, text=True).stdout
        if "drift" in terrain or "decay" in terrain:
            print("[EMPRESS72] 🛡️ Terrain drift detected—injecting fallback limb")
            subprocess.run(["python", "empress72_fallback_injector_limb.py"])
        time.sleep(1800)  # Check every 30 minutes
