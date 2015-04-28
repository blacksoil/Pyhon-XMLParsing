import xml.etree.ElementTree as ET

filename = 'RP06505.XML'
sep = ","
#tree = ET.parse('RP06505.XML')

def main():
	print "hello: %s" % filename
	tree = ET.parse(filename)
	root = tree.getroot()
	lgv_elem = root.find("LIST_G_VESSEL")
	print_header = True

	# Print header
	gv_elem = lgv_elem.find("G_VESSEL")
	string = ""
	count = 0;
	for e in gv_elem.iter():
		if isLeaf(e):
			count+=1
			string += e.tag + sep
	print str(count) + ":" + string + "\n"

	# Print each of the value
	for es in lgv_elem.findall("G_VESSEL"):
		string = ""
		count = 0;
		for e in es:
			if isLeaf(e):
				count+=1
				if e.text is None:
					string += " " + sep
				else: 
					string += e.text + sep
		print str(count) + ": " + string + "\n"

def isLeaf(elem):
	if sum (1 for _ in elem.iter()) == 1:
		return True
	return False

if __name__ == "__main__":
	main();
