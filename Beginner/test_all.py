import os
import subprocess

def run_scripts(directory):
    print(f"\n🔹 Running scripts in {directory}...\n")
    for file in sorted(os.listdir(directory), key=lambda x: int(x[1:-3]) if x.startswith("Q") and x.endswith(".py") else float('inf')):
        if file.endswith(".py"):
            print(f"▶ Running {file}...")
            subprocess.run(["python", os.path.join(directory, file)])

base_dir = os.path.dirname(os.path.abspath(__file__))

run_scripts(os.path.join(base_dir, "Level_I"))
run_scripts(os.path.join(base_dir, "Level_II"))
run_scripts(os.path.join(base_dir, "Level_III"))
