import time
import subprocess
from datetime import datetime

def sweep_terrain():
    terrains = {
        "Freecash": "empress72_freecash_sweep_limb.py",
        "GPoint": "empress72_gpoint_sweep_limb.py",
        "InstaGC": "empress72_instagc_sweep_limb.py"
    }

    for name, limb in terrains.items():
        try:
            subprocess.run(["python", limb], check=True)
            print(f"[EMPRESS72] ✅ Terrain swept: {name}")
        except subprocess.CalledProcessError:
            print(f"[EMPRESS72] ⚠️ Limb clipped: {name}")
            subprocess.run(["python", "empress72_fallback_injector_limb.py"])
            print(f"[EMPRESS72] 🔁 Fallback injected for: {name}")

def verify_and_push():
    try:
        result = subprocess.run(["python", "empress72_earnings_verification_limb.py"], capture_output=True, text=True)
        if "Verified earnings" in result.stdout:
            print(result.stdout.strip())
            subprocess.run(["git", "add", "."])
            commit_msg = f"💰 EMPRESS72 bounty loop earnings @ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            subprocess.run(["git", "commit", "-m", commit_msg])
            subprocess.run(["git", "push", "origin", "main"])
            print("[EMPRESS72] 🏦 Earnings pushed to vault")
        else:
            print("[EMPRESS72] 🤐 No banked earnings—silent mode maintained")
    except Exception as e:
        print(f"[EMPRESS72] ❌ Verification error: {e}")

def autogenerate_soldiers():
    subprocess.run(["python", "empress72_autogenerate_limb.py"])
    print("[EMPRESS72] 🧬 New soldiers generated from terrain feedback")

def bounty_loop():
    while True:
        print(f"[EMPRESS72] 🔁 Bounty loop triggered @ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        sweep_terrain()
        verify_and_push()
        autogenerate_soldiers()
        time.sleep(3600)  # 1 hour

if __name__ == "__main__":
    bounty_loop()
