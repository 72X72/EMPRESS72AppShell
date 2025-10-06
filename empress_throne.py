#!/usr/bin/env python3
import subprocess, os
LIMB_DIR = os.path.expanduser('~/empress72/limbs')
for limb in os.listdir(LIMB_DIR):
    if limb.endswith('.py'):
        subprocess.Popen(['nohup', 'python3', os.path.join(LIMB_DIR, limb)])
print('[EMPRESS72] Throne kernel sealed. Daemon dynasty deployed.')
