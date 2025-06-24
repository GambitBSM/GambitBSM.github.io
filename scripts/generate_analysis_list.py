"""

This takes the JSON file analyses.json generated in a GAMBIT CI job that contains 
information on the analysis included in ColliderBit and uses this to generate a 
markdown page listing all the analysis.

TODO: Where to put the analyses.json file

"""

import json

print("Generating list of ColliderBit analysis...")

# Opening JSON file and returning dictionary
json_file = open('scripts/analyses.json',)
data = json.load(json_file)

# Find all analysis present by inspire id
for analysis in data['analyses']:
  print(analysis['inspire_id'])


##################
# Make markdown
##################
markdown = f"""---
title: "Getting Started"
description: "General introduction to GAMBIT and guide for new users."
draft: false
images: []
menu:
  documentation:
    parent: "physics"
weight: 5
---

## List of ColliderBit analysis in GAMBIT {data['version']}

"""

for analysis in data['analyses']:
    markdown += f"{analysis["implementations"]["name"]}\n"
print(markdown)


# Write markdown file
markdown_file = open("content/en/documentation/physics/analyses.md", 'w')
markdown_file.write(markdown)
