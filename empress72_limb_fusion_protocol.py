import os, traceback
from datetime import datetime

def log(message):
    with open("empress_log.txt", "a") as f:
        f.write(f"[{datetime.now().strftime('%a %b %d %H:%M:%S %Y')}] {message}\n")

def find_limbs():
    return [f for f in os.listdir() if f.startswith("empress72_") and f.endswith("_limb.py")]

def fuse_limbs(limbs):
    try:
        fused_name = "empress72_fused_limb.py"
        with open(fused_name, "w") as f:
            f.write("# 🧬 Fused limb: hybrid sweepers across terrain\n")
            f.write("def sweep():\n")
            for limb in limbs:
                f.write(f"    print('Injecting logic from {limb}...')\n")
                with open(limb, "r") as lf:
                    for line in lf:
                        if "def sweep()" in line or line.strip().startswith("#"):
                            continue
                        if line.strip().startswith("print("):
                            f.write("    " + line.strip() + "\n")
        log(f"🧬 Fused limb created: {fused_name}")
        return fused_name
    except Exception as e:
        log("❌ Limb fusion failed: " + str(e))
        log(traceback.format_exc())

def inject_to_cockpit(fused_limb):
    try:
        os.system("cp empress72_cockpit.py empress72_cockpit.bak")
        with open("empress72_cockpit.py", "r") as f:
            existing = f.read()
        with open("empress72_cockpit.py", "a") as f:
            import_line = f"from {fused_limb.replace('.py','')} import sweep\n"
            if import_line not in existing:
                f.write(import_line)
                log(f"🔁 Fused limb injected: {fused_limb}")
        log("✅ Limb fusion injected into cockpit.")
    except Exception as e:
        log("❌ Cockpit injection failed: " + str(e))

def cinematic_override(fused_limb):
    try:
        with open("empress_cinematic.txt", "a") as f:
            f.write(f"\n🎥 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} LIMB FUSION PROTOCOL\n")
            f.write(f"🧬 Fused limb: {fused_limb}\n")
        log("🎬 Cinematic override triggered by limb fusion.")
    except Exception as e:
        log("❌ Cinematic override failed: " + str(e))

def main():
    log("🛠️ EMPRESS72 limb fusion protocol initiated.")
    limbs = find_limbs()
    if limbs:
        fused = fuse_limbs(limbs)
        inject_to_cockpit(fused)
        cinematic_override(fused)
    else:
        log("🧘 No limbs found for fusion.")
    log("✅ Limb fusion cycle complete.")

if __name__ == "__main__":
    main()
