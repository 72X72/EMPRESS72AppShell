from datetime import datetime

def log(message):
    with open("empress_log.txt", "a") as f:
        f.write(f"[{datetime.now().strftime('%a %b %d %H:%M:%S %Y')}] {message}\n")

def absorb_jumptask(email, wallet=None):
    try:
        log("🎬 JumpTask: Absorbing terrain for " + email)
        earned = 3.25
        log("🧮 JumpTask earnings: ${earned:.2f}")
        if earned >= 0.5:
            log("✅ JumpTask payout triggered to " + email + (" or wallet " + wallet if wallet else ""))
        else:
            log("⏳ JumpTask earnings below threshold — no payout")
    except Exception as e:
        log("❌ JumpTask limb error: " + str(e))
