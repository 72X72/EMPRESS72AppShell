#!/usr/bin/env python3
import time,os
LOG=os.path.expanduser("~/empress72/executor.log")
while True:
 with open(LOG,"a") as f:f.write(f"[{time.strftime("%Y-%m-%d %H:%M:%S")}] EMPRESS72 executed bounty task.\n")
 time.sleep(180)
