#!/bin/bash
content="$(cat - | jq -r .)"

echo -e "\`\`\`\`\`\`\n${content}\n\`\`\`\`\`\`" | pandoc -f markdown -t json
