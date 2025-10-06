#!/usr/bin/env python3
import time,os
LOG=os.path.expanduser("~/empress72/payout.log")
while True:
 with open(LOG,"a") as f:f.write(f"[{time.strftime("%Y-%m-%d %H:%M:%S")}] EMPRESS72 triggered payout to sovereign account.\n")
 time.sleep(300)
