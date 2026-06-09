import os
from collections import Counter

folder = r"C:\Program Files\Epic Games\rocketleague\TAGame\CookedPCConsole"
output_file = "prefix_summary.txt"

prefixes = Counter()
examples = {}

for name in os.listdir(folder):
    # take everything before the first underscore as the prefix
    prefix = name.split("_")[0]
    prefixes[prefix] += 1
    # save up to 3 example filenames per prefix
    if prefix not in examples:
        examples[prefix] = []
    if len(examples[prefix]) < 3:
        examples[prefix].append(name)

with open(output_file, "w") as f:
    for prefix, count in prefixes.most_common():
        f.write(f"{prefix} ({count} files)\n")
        for ex in examples[prefix]:
            f.write(f"    {ex}\n")
        f.write("\n")

print(f"Done — see {output_file}")