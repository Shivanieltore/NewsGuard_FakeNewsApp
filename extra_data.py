import pandas as pd
import os

# Sample real news headlines
real_headlines = [
    "CBSE approves twice-a-year board exams for Class 10 from next year",
    "NASA launches water-seeking rover to the Moon",
    "Government launches scheme for AI education in schools",
    "Supreme Court rules in favor of environmental protection laws",
    "ISRO announces Chandrayaan-4 mission for lunar exploration",
    "WHO declares malaria vaccine rollout in 10 countries",
    "RBI raises interest rates to control inflation",
    "India's GDP grows at 7.8% in the last quarter",
    "Scientists develop new biodegradable plastic from seaweed",
    "IITs to introduce quantum computing as elective from next semester"
]

# Sample fake news headlines
fake_headlines = [
    "Aliens to replace teachers in Indian schools by 2030",
    "CBSE bans all science subjects from 2025 to reduce stress",
    "Chocolate found to be the cure for all diseases",
    "Time travel to be included in school curriculum next year",
    "NASA confirms Moon is made of cheese",
    "Government to replace currency with gold coins in 2026",
    "RBI to issue cryptocurrency powered by solar energy",
    "India to be renamed as BharatLand by 2025",
    "Supreme Court legalizes teleportation for court appearances",
    "WHO approves laughter therapy as universal vaccine"
]

# Combine and label
data = pd.DataFrame({
    "text": real_headlines + fake_headlines,
    "label": [1]*len(real_headlines) + [0]*len(fake_headlines)
})

# Ensure dataset/ directory exists
os.makedirs("dataset", exist_ok=True)

# Save to CSV
csv_path = "dataset/extra_data.csv"
data.to_csv(csv_path, index=False)

print(f"✅ Created {csv_path} with {len(data)} rows.")
