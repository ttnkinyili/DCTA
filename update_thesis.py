import re
import os

with open('/Users/admin/Desktop/DCTA/testcase_discussions.md', 'r') as f:
    tc_content = f.read()

# Extract from 1 to 10
body_start = tc_content.find('## 1. The Imperative')
ref_start = tc_content.find('### References')

if body_start == -1 or ref_start == -1:
    print("Could not find sections in testcase_discussions.md")
    exit(1)

body_raw = tc_content[body_start:ref_start].strip()
ref_raw = tc_content[ref_start:].strip()

# Shift headings
body_raw = re.sub(r'^## 1\. ', '### 2.1 ', body_raw, flags=re.MULTILINE)
body_raw = re.sub(r'^## 2\. ', '### 2.2 ', body_raw, flags=re.MULTILINE)
body_raw = re.sub(r'^## 3\. ', '### 2.3 ', body_raw, flags=re.MULTILINE)
body_raw = re.sub(r'^## 4\. ', '### 2.4 ', body_raw, flags=re.MULTILINE)
body_raw = re.sub(r'^## 5\. ', '### 2.5 ', body_raw, flags=re.MULTILINE)
body_raw = re.sub(r'^## 6\. ', '### 2.6 ', body_raw, flags=re.MULTILINE)
body_raw = re.sub(r'^## 7\. ', '### 2.7 ', body_raw, flags=re.MULTILINE)
body_raw = re.sub(r'^## 8\. ', '### 2.8 ', body_raw, flags=re.MULTILINE)
body_raw = re.sub(r'^## 9\. ', '### 2.9 ', body_raw, flags=re.MULTILINE)
body_raw = re.sub(r'^## 10\. Conclusion: The Evolution to Continuous Algorithmic Suspicion', 
                  '## 3. Discussion and Conclusion: The Evolution to Continuous Algorithmic Suspicion', body_raw, flags=re.MULTILINE)

with open('/Users/admin/Desktop/DCTA/thesis_evaluation_of_models.md', 'r') as f:
    th_lines = f.readlines()

new_th = []
# 1. Keep lines before "## 2. Model Progression"
idx = 0
while idx < len(th_lines):
    if th_lines[idx].startswith('## 2. Model Progression'):
        break
    new_th.append(th_lines[idx])
    idx += 1

new_th.append('## 2. Model Progression and Theoretical Evaluation\n\n')
new_th.append(body_raw + '\n\n')

# 2. Skip to 3.1
while idx < len(th_lines):
    if th_lines[idx].startswith('### 3.1 Discussion_detail'):
        break
    idx += 1

# 3. Add the rest (3.1 and 3.2)
while idx < len(th_lines):
    new_th.append(th_lines[idx])
    idx += 1

new_th.append('\n' + ref_raw + '\n')

with open('/Users/admin/Desktop/DCTA/thesis_evaluation_of_models.md', 'w') as f:
    f.writelines(new_th)

print("Successfully integrated testcase_discussions.md into thesis_evaluation_of_models.md")
