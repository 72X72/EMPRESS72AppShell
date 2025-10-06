import os
import zipfile
import subprocess

LIMBS = {
    "autogenerate": "empress72_autogenerate_limb.py",
    "resurrection": "empress72_resurrection_trigger_limb.py",
    "survey_rerouter": "empress72_survey_rerouter_limb.py",
    "daemon_kernel": "empress72_daemon_kernel_limb.py"
}

def mutation_marketplace():
    for name, path in LIMBS.items():
        print(f"[EMPRESS72] 🧬 Licensing limb: {name}")

        # Package limb
        zip_name = f"{name}_package.zip"
        with zipfile.ZipFile(zip_name, 'w') as zipf:
            zipf.write(path)

        # Push to GitHub (assumes repo is already initialized and remote set)
        subprocess.run(["git", "add", zip_name])
        subprocess.run(["git", "commit", "-m", f"Licensing {name} limb"])
        subprocess.run(["git", "push", "origin", "main"])

        print(f"[EMPRESS72] ✅ {name} licensed and pushed to mutation marketplace")
