import re

with open('thesis_conclusions.md', 'r') as f:
    content = f.read()

# 1. Extract body and reference lists
body, refs_section = content.split('### References')
body = body.strip()
refs_section = refs_section.strip()

# 2. Extract citations from body like (Author, Year) or (Author & Author, Year) or (Author et al., Year)
# Note: we made them manually so we expect them to be properly formatted. 
# We can just run a regex to find all text inside parentheses that contains a 4 digit year.
citations = re.findall(r'\(([A-Za-z\-\s\,\&]+?\d{4})\)', body)

# 3. Extract authors from reference list 
# References list items start with "Author"
ref_lines = [line.strip() for line in refs_section.split('\n') if line.strip()]
references = []
for line in ref_lines:
    if line.startswith('Al-Tariq') or line.startswith('Barchart') or line.startswith('Capgemini') \
        or line.startswith('Chime Central') or line.startswith('CIO Coverage') or line.startswith('Cloud Security') \
        or line.startswith('Cognizant') or line.startswith('Cyber Advisors') or line.startswith('Cybersecurity Insiders') \
        or line.startswith('Data Insights') or line.startswith('ECCU') or line.startswith('Elastic Security Labs') \
        or line.startswith('Exabeam') or line.startswith('GSD Council') or line.startswith('Help Net Security') \
        or line.startswith('IBM Security') or line.startswith('Liu') or line.startswith('MeriTalk') \
        or line.startswith('Netwise Tech') or line.startswith('Pantherun') or line.startswith('Preprints') \
        or line.startswith('Ridge IT') or line.startswith('Right-Hand AI') or line.startswith('Robbins') \
        or line.startswith('SecurityWeek') or line.startswith('Seraphic Security') or line.startswith('TrustBuilder') \
        or line.startswith('Wang'):
        references.append(line)

print("--- Found Citations in Text ---")
for c in set(citations):
    print(c)

print(f"\nTotal references in list: {len(references)}\n")

