def sanitize(name):
    return name.lower().replace("'", "").replace("[", "").replace("]", "").replace(" ", "").replace('"', '')

def resurrect_limb(name):
    try:
        clean = sanitize(name)
        filename = f"empress72_{clean}_limb.py"
        if not os.path.exists(filename):
            with open(filename, "w") as f:
                f.write(f"# 🧬 Resurrected limb for {name}\n")
                f.write("def sweep():\n")
                f.write(f"    print('Attempting fallback sweep on {name} terrain...')\n")
            log(f"🧬 Limb resurrected: {filename}")
            return filename
        else:
            log(f"🔁 Limb already exists: {filename}")
            return filename
    except Exception as e:
        log(f"❌ Limb resurrection failed for {name}: {str(e)}")
