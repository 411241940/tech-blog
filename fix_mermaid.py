#!/usr/bin/env python3
import re

with open('contextual-retrieval.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 1: Replace ~800 tokens
content = content.replace('~800 tokens', '约800 tokens')

# Fix 2: Remove problematic mermaid link with % and |
content = re.sub(
    r'JustRight -->\|"重叠 10-20%"\| Overlap',
    'JustRight -.-> Overlap',
    content
)

# Fix 3: Fix Ex2 with % and remove the link
content = re.sub(
    r"Ex2\[\"检索到：'公司营收增长3%\.\.\.'\"\]",
    'Ex2["检索到：公司营收增长3"]',
    content
)

content = re.sub(
    r'Ex2 -.->\|"缺少上下文"\| Problem',
    'Ex2 -.-> Problem',
    content
)

with open('contextual-retrieval.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed!")
