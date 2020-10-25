import sys

month = sys.argv[1]
concept = sys.argv[2]

print("=IF('" + month + " Bruto'.F1=\"" + concept + "\",'" + month + " Bruto'.E1,0)")
