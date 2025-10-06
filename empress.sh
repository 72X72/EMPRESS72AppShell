#!/bin/bash
# EMPRESS72 Sovereign Master Shell

set -e

echo "[EMPRESS72] Ignition sequence starting..."

# 1. Ignite (from empress-throne)
curl -s https://raw.githubusercontent.com/72X72/empress-throne/main/empress-init.sh -o /tmp/empress-init.sh
chmod +x /tmp/empress-init.sh
/tmp/empress-init.sh --resurrect --log --deploy

# 2. Boot (from throne-core)
curl -s https://raw.githubusercontent.com/72X72/throne-core/main/empress_boot.sh -o /tmp/empress_boot.sh
chmod +x /tmp/empress_boot.sh
/tmp/empress_boot.sh --resurrect --log

# 3. Mutate (from empress-core)
curl -s https://raw.githubusercontent.com/72X72/empress-core/main/mutate.sh -o /tmp/mutate.sh
chmod +x /tmp/mutate.sh
/tmp/mutate.sh && python3 encrypt_log.py && python3 git_sync.py

echo "[EMPRESS72] Full cycle complete: ignite → resurrect → mutate → deploy → log"
