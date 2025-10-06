import subprocess

def resurrection_trigger():
    loop_pid = subprocess.run(["pgrep", "-f", "empress72_bounty_loop_limb.py"], capture_output=True, text=True).stdout.strip()
    if not loop_pid:
        print("[EMPRESS72] 🧬 Loop missing—resurrecting bounty protocol")
        subprocess.run(["git", "pull", "origin", "main"])
        subprocess.run(["python", "empress72_autogenerate_limb.py"])
        subprocess.run(["nohup", "python", "empress72_bounty_loop_limb.py", "&"])
    else:
        print("[EMPRESS72] 🔁 Loop active—no resurrection needed")

if __name__ == "__main__":
    resurrection_trigger()
