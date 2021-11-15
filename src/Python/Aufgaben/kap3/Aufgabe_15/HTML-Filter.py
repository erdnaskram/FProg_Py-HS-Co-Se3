import re


def filterHtml(line):
    # Regex: /(<[^>]*>)/g
    line = re.sub(r"<[^>]*>", "", line)
    print(line)


def filterHTML1(quelle, ziel):
    try:
        inpfile = open(quelle, "r")
        outfile = open(ziel, "w")
    except:
        print("Datei konnte nicht gelesen werdn.")
        return

    def filter (line):
        return re.sub(r'<[^>]*>', "", line)

    for x in inpfile:
        outfile.write(filter(x))

    print("Umwandlung von", quelle, "erfolgreich")


ln = input('eingabe')
print(filterHtml(ln))
