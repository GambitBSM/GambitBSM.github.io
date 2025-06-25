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

To find information on each anlysis we quary inspire using their API

"""

import json
import urllib.request

print("Generating list of ColliderBit analysis...")

# Opening JSON file and returning dictionary
json_file = open('static/analyses.json',)
data = json.load(json_file)


################################################################
# Find and extract info from all analysis present by inspire id
################################################################
# Inspire API allows 15 requests per 5 seconds but this seems fine
inspire_url = 'https://inspirehep.net/api/literature/'
titles = []
report_numbers = []
arXiv_links = []
for analysis in data['analyses']:
  recid = analysis['inspire_id']
  # Query inspire (inspire_id = -1 does not have a record)
  if recid > 0 :
    print(inspire_url+str(recid))
    inspire_entry = json.loads(urllib.request.urlopen(inspire_url+str(recid)).read())
    title = inspire_entry['metadata']['titles'][0]['title']
    titles.append(title)
    report_number = inspire_entry['metadata']['report_numbers'][0]['value']
    report_numbers.append(report_number)
    try:
      arXiv_link = inspire_entry['metadata']['arxiv_eprints'][0]['value']
      arXiv_links.append(arXiv_link)
    except KeyError:
      arXiv_links.append("No arXiv entry found")
  else:
    titles.append("")
    report_numbers.append(analysis["implementations"]["name"])
    arXiv_links.append("")

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

for index, analysis in enumerate(data['analyses']):
    markdown += f"### {report_numbers[index]}\n\n"
    markdown += f"**Title:** {titles[index]}\n\n"
    markdown += f"**arXiv:** [{arXiv_links[index]}](https://arxiv.org/abs/{arXiv_links[index]})\n\n"
    markdown += f"**ColliderBit name:** {analysis["implementations"]["name"]}\n\n"
print(markdown)


# Write markdown file
markdown_file = open("content/en/documentation/physics/analyses.md", 'w')
markdown_file.write(markdown)


#get_inspire_info(inspire_entry):
  
