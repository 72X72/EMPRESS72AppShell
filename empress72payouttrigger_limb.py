import subprocess

def payout_trigger():
    verified = 5.00  # Replace with actual verified earnings
    if verified >= 5.00:
        print(f"[EMPRESS72] 🏦 Triggering payout: ${verified}")
        # Simulate PayPal or crypto transfer
        subprocess.run(["python", "empress72_vault_push_limb.py"])
        print("[EMPRESS72] 💸 Payout initiated to wallet")
    else:
        print("[EMPRESS72] 🤐 Earnings below threshold—payout not triggered")
