#!/usr/bin/env python3

with open('contextual-retrieval.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

in_mermaid = False
output_lines = []

for line in lines:
    if '<div class="mermaid">' in line:
        in_mermaid = True
        output_lines.append(line)
    elif '</div>' in line and in_mermaid:
        # This might be the end of mermaid, but check if it was the closing tag
        if '</div>' in line:
            in_mermaid = False
        output_lines.append(line)
    elif in_mermaid:
        # Replace % with safe text in mermaid content
        line = line.replace('%', ' 百分比 ')
        output_lines.append(line)
    else:
        output_lines.append(line)

with open('contextual-retrieval.html', 'w', encoding='utf-8') as f:
    f.writelines(output_lines)

print("Fixed!")
