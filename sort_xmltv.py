import re
import sys

xml = open(sys.argv[1], encoding="utf-8").read()

# Garde tout avant le premier <programme>
header = xml.split("<programme", 1)[0]

# Récupère tous les programmes
programmes = re.findall(r"<programme.*?</programme>", xml, re.S)

def get_start(p):
    m = re.search(r'start="([^"]+)"', p)
    return m.group(1) if m else ""

# Tri strict par date/heure de début
programmes.sort(key=get_start)

with open(sys.argv[2], "w", encoding="utf-8") as f:
    f.write(header)
    for p in programmes:
        f.write(p + "\n")
    f.write("</tv>")
