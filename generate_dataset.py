import pandas as pd
import numpy as np
import random
from faker import Faker
from datetime import timedelta
import os


# Setup
fake = Faker()
Faker.seed(42)
random.seed(42)

# Constants
features = [
    "Build Mode", "Create-a-Sim", "Live Mode", "Expansion Pack", "Mods & Custom Content", 
    "Multiplayer", "Graphics", "UI", "Audio", "World Map", "Careers", "Skills", 
    "Aspirations", "Social Interactions", "Aging System", "Pets", "Seasons", "Occults", 
    "Bug Fixes", "Tutorial"
]

platforms = ["PC", "Mac", "PlayStation", "Xbox"]
regions = ["North America", "Europe", "Asia", "South America", "Africa", "Oceania"]
status_options = ["New", "Investigating", "In Progress", "Resolved", "Won't Fix"]
severity_levels = ["Low", "Medium", "High", "Critical"]
teams = ["LiveOps", "UI/UX", "Audio", "Build Mode", "CAS", "Expansion Pack", "Platform", "Graphics"]
milestones = ['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7']
priority_levels = ['Low', 'Medium', 'High']
bug_types = ['Graphics', 'Gameplay', 'Performance', 'UI', 'Audio', 'Network', 'Expansion Pack', 'Mods & Custom Content']

def generate_sims_bug_reports(n=10000):
    data = []
    for i in range(1, n + 1):
        date_reported = fake.date_between(start_date='-1y', end_date='today')
        resolved_flag = random.random() < 0.8
        resolution_days = random.randint(1, 30) if resolved_flag else None
        date_resolved = date_reported + timedelta(days=resolution_days) if resolution_days else None
        
        if date_resolved:
            status = random.choices(
                ["Resolved", "Won't Fix"],
                weights=[0.9, 0.1]
            )[0]
        else:
            status = random.choices(
                ["New", "Investigating", "In Progress"],
                weights=[0.4, 0.3, 0.3]
            )[0]
        
        data.append({
            "bug_id": i,
            "feature": random.choice(features),
            "severity": random.choices(severity_levels, weights=[0.4, 0.3, 0.2, 0.1])[0],
            "status": status,
            "date_reported": date_reported,
            "date_resolved": date_resolved,
            "platform": random.choice(platforms),
            "region": random.choice(regions),
            "assigned_team": random.choice(teams),
            "bug_type": random.choice(bug_types),
            "milestone": random.choice(milestones),
            "priority_level": random.choices(priority_levels, weights=[0.3, 0.5, 0.2])[0]
        })
    return pd.DataFrame(data)

sims_bug_df = generate_sims_bug_reports()
os.makedirs("data", exist_ok=True)
sims_bug_df.to_csv("data/Sims4_Bug_Report_Dataset.csv", index=False)