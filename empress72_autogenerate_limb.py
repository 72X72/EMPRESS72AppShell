import os
from datetime import datetime

def log(message):
    with open("empress_log.txt", "a") as f:
        f.write(f"[{datetime.now().strftime('%a %b %d %H:%M:%S %Y')}] {message}\n")

def generate_simple_limb(limb_name):
    filename = f"empress72_{limb_name}_limb.py"
    if os.path.exists(filename):
        log(f"🔁 Limb already exists: {filename}")
        return
    with open(filename, "w") as f:
        f.write(f'''def {limb_name}():
    print("[EMPRESS72] ✅ Limb {limb_name} executed.")\n''')
    log(f"🧬 Simple limb generated: {filename}")

def inject_into_cockpit(limb_name):
    cockpit_path = "empress72_cockpit.py"
    if not os.path.exists(cockpit_path):
        log("❌ Cockpit not found.")
        return
    with open(cockpit_path, "r") as f:
        content = f.read()
    import_line = f"from empress72_{limb_name}_limb import {limb_name}"
    if import_line not in content:
        with open(cockpit_path, "a") as f:
            f.write(f"\n{import_line}\n")
        log(f"🔗 Limb injected into cockpit: {limb_name}")
    else:
        log(f"🔁 Limb already injected: {limb_name}")

def main():
    try:
        with open("empress_signal.txt", "r") as f:
            signal = f.read().strip()
        if signal.startswith("MISSING_LIMB:"):
            limb_name = signal.split(":")[1].strip()
            generate_simple_limb(limb_name)
            inject_into_cockpit(limb_name)
            log(f"🎬 Autogenerate cycle complete for: {limb_name}")
    except Exception as e:
        log(f"❌ Autogenerate failed: {str(e)}")

if __name__ == "__main__":
    main()
