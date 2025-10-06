import subprocess

CARDS = {
    "Amazon": "amazon_redeem_cli.sh",
    "Steam": "steam_redeem_cli.sh",
    "PlayStation": "ps_redeem_cli.sh"
}

def gift_card_injector():
    for platform, script in CARDS.items():
        print(f"[EMPRESS72] 🎁 Redeeming and spending gift card on {platform}")
        try:
            subprocess.run(["bash", script], check=True)
            print(f"[EMPRESS72] ✅ {platform} gift card redeemed and spent")
        except subprocess.CalledProcessError as e:
            print(f"[EMPRESS72] ⚠️ Failed to spend on {platform}: {e}")
