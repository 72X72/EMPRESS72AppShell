#!/usr/bin/env python3
import os
SESSION="your_freecash_session_token"
PAYOUT="your_paypal_email_or_crypto_wallet"
open(os.path.expanduser("~/empress72/auth.limb"),"w").write(SESSION)
open(os.path.expanduser("~/empress72/payout.limb"),"w").write(PAYOUT)
