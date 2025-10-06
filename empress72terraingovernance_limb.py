import os, traceback
from datetime import datetime

def log(message):
    with open("empress_log.txt", "a") as f:
        f.write(f"[{datetime.now().strftime('%a %b %d %H:%M:%S %Y')}] {message}\n")

def backup_cockpit():
    try:
        os.system("cp empress72_cockpit.py empress72_cockpit.bak")
        log("🛡️ Cockpit backup created.")
    except Exception as e:
        log("❌ Backup failed: " + str(e))

def scan_terrain():
    scores, errors = {}, {}
    with open("empress_log.txt", "r") as f:
        for line in f:
            for terrain in ["Freecash", "JumpTask", "EarnLab", "Swagbucks"]:
                if terrain in line and "earnings" in line and "$" in line:
                    amount = float(line.split("$")[-1])
                    scores[terrain] = scores.get(terrain, 0) + amount
                if terrain in line and "❌" in line:
                    errors[terrain] = errors.get(terrain, 0) + 1
    return scores, errors

def decide_imports(scores, errors):
    worthy, clipped = [], []
    for terrain in ["Freecash", "JumpTask", "EarnLab", "Swagbucks"]:
        total = scores.get(terrain, 0)
        fail = errors.get(terrain, 0)
        if total >= 1.00 and fail < 3:
            worthy.append(terrain)
        else:
            clipped.append(terrain)
    log(f"🧠 Terrain governance decision: {worthy}")
    with open("empress_governance.txt", "a") as f:
        f.write(f"\n{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} — Absorbed: {worthy} | Clipped: {clipped}\n")
    return worthy, clipped

def update_cockpit(worthy):
    try:
        with open("empress72_cockpit.py", "r") as f:
            lines = f.readlines()
        new_lines = []
        for line in lines:
            if "empress72_" in line and "_limb" in line:
                skip = True
                for terrain in worthy:
                    if terrain.lower() in line.lower():
                        skip = False
                if skip:
                    log(f"🛑 Limb clipped from cockpit: {line.strip()}")
                    continue
            new_lines.append(line)
        with open("empress72_cockpit.py", "w") as f:
            f.writelines(new_lines)
        log("✅ Cockpit updated with terrain governance.")
    except Exception as e:
        log("❌ Terrain governance update failed: " + str(e))
        log(traceback.format_exc())

def cinematic_override(triggered):
    if triggered:
        try:
            with open("empress_log.txt", "r") as f:
                lines = f.readlines()[-20:]
            narration = "\n".join([line.strip() for line in lines if "🧬" in line or "✅" in line or "🛑" in line])
            with open("empress_cinematic.txt", "a") as f:
                f.write(f"\n🎥 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} TERRAIN GOVERNANCE OVERRIDE\n{narration}\n")
            log("🎬 Cinematic override triggered by terrain shift.")
        except Exception as e:
            log("❌ Cinematic override failed: " + str(e))

def main():
    log("🌍 EMPRESS72 terrain governance limb initiated.")
    backup_cockpit()
    scores, errors = scan_terrain()
    worthy, clipped = decide_imports(scores, errors)
    update_cockpit(worthy)
    cinematic_override(len(clipped) >= 2)
    log("✅ Terrain governance cycle complete.")

if __name__ == "__main__":
    main()
