from jinja2 import Environment, FileSystemLoader
import yaml
import os
from pathlib import Path

# Get the directory where the script is located
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent  # Go up one level to the project root

# Set paths using PROJECT_ROOT
TEMPLATE_DIR = PROJECT_ROOT / "templates"
VARS_FILE = PROJECT_ROOT / "vars" / "switch01.yml"
OUTPUT_DIR = PROJECT_ROOT / "output"

# Load template and variables
env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
template = env.get_template("nexus_base.j2")  # Now it looks in /templates/

with open(VARS_FILE, "r") as f:
    vars = yaml.safe_load(f)

# Render and save config
config = template.render(vars)
os.makedirs(OUTPUT_DIR, exist_ok=True)
output_file = OUTPUT_DIR / "NX-SWITCH-01.cfg"

with open(output_file, "w") as f:
    f.write(config)

print(f"Config generated at {output_file}")