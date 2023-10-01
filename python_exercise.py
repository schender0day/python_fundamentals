import re

import re

s = "The Terrible Tiger Tore The Towel"
pattern = '[Tt]'

matches = re.finditer(pattern, s)
for match in matches:
    print(match.start())
print(-1)
