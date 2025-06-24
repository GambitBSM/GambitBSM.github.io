"""

This takes the JSON file generated using the GAMBIT script
  gambit/ColliderBit/src/analyses/mkjson.py
that contains information on the analysis included in ColliderBit and uses this 
to generate a markdown page listing all the analyses.

The JSON file can be found in this repo as
  static/analyses.json
and should be updated as a part of a GAMBIT release.

The analyses.json file is exposed on the webpage as
https://gambitbsm.org/analyses.json

"""

import json

print("Generating list of ColliderBit analysis...")

# Opening JSON file and returning dictionary
json_file = open('static/analyses.json',)
data = json.load(json_file)

# Find all analysis present by inspire id
for analysis in data['analyses']:
  print(analysis['inspire_id'])


##################
# Make markdown
##################
markdown = f"""---
title: "ColliderBit analysis"
description: "List of ColliderBit analysis"
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
    markdown += f"### {analysis["implementations"]["name"]}\n"
print(markdown)


# Write markdown file
markdown_file = open("content/en/documentation/physics/analyses.md", 'w')
markdown_file.write(markdown)
