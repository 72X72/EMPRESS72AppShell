from datetime import datetime

def log(message):
    with open("empress_log.txt", "a") as f:
        f.write(f"[{datetime.now().strftime('%a %b %d %H:%M:%S %Y')}] {message}\n")

def absorb_earnlab(email, wallet=None):
    try:
        log("🎬 EarnLab: Absorbing terrain for " + email)
        earned = 3.25
        log("🧮 EarnLab earnings: ${earned:.2f}")
        if earned >= 0.5:
            log("✅ EarnLab payout triggered to " + email + (" or wallet " + wallet if wallet else ""))
        else:
            log("⏳ EarnLab earnings below threshold — no payout")
    except Exception as e:
        log("❌ EarnLab limb error: " + str(e))
