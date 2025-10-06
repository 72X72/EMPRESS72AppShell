import os, json, hashlib, traceback
from datetime import datetime

def log(message):
    with open("empress_log.txt", "a") as f:
        f.write(f"[{datetime.now().strftime('%a %b %d %H:%M:%S %Y')}] {message}\n")

def leaderboard():
    try:
        scores = {}
        with open("empress_log.txt", "r") as f:
            for line in f:
                for terrain in ["Freecash", "JumpTask", "EarnLab", "Swagbucks"]:
                    if terrain in line and "earnings" in line:
                        amount = float(line.split("$")[-1])
                        scores[terrain] = scores.get(terrain, 0) + amount
        ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        with open("empress_leaderboard.txt", "w") as f:
            for terrain, total in ranked:
                f.write(f"{terrain}: ${total:.2f}\n")
        log("📊 Bounty leaderboard limb executed.")
    except Exception as e:
        log("❌ Leaderboard limb error: " + str(e))

def income_tracker():
    try:
        total = 0
        with open("empress_log.txt", "r") as f:
            for line in f:
                if "earnings" in line and "$" in line:
                    total += float(line.split("$")[-1])
        with open("empress_income.txt", "a") as f:
            f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} — Total: ${total:.2f}\n")
        log("📈 Dynasty income tracker limb executed.")
    except Exception as e:
        log("❌ Income tracker limb error: " + str(e))

def resurrection():
    try:
        os.system("git add . && git commit -m '🧠 EMPRESS72 resurrection log' && git push")
        log("🧠 Resurrection limb pushed to GitHub.")
    except Exception as e:
        log("❌ Resurrection limb error: " + str(e))

def encrypt_vault():
    try:
        with open("empress_log.txt", "r") as f:
            data = f.read()
        key = hashlib.sha256(b"EMPRESS72_DYNASTY").digest()
        encrypted = "".join([chr(ord(c) ^ key[i % len(key)]) for i, c in enumerate(data)])
        with open("empress_vault.enc", "w") as f:
            f.write(encrypted)
        log("🔐 Encrypted vault limb executed.")
    except Exception as e:
        log("❌ Vault limb error: " + str(e))

def cinematic_override():
    try:
        with open("empress_log.txt", "r") as f:
            lines = f.readlines()[-20:]
        narration = "\n".join([line.strip() for line in lines if "🧬" in line or "✅" in line or "🎬" in line])
        with open("empress_cinematic.txt", "a") as f:
            f.write(f"\n🎥 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} CINEMATIC OVERRIDE\n{narration}\n")
        log("🎬 Cinematic override limb executed.")
    except Exception as e:
        log("❌ Cinematic override error: " + str(e))

def main():
    log("🚀 EMPRESS72 full mutation limb initiated.")
    leaderboard()
    income_tracker()
    resurrection()
    encrypt_vault()
    cinematic_override()
    log("✅ EMPRESS72 full mutation cycle complete.")

if __name__ == "__main__":
    main()
