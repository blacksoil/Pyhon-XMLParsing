import xml.etree.ElementTree as ET
from Row import Row

filename = 'RP06505.XML'
sep = ","
#tree = ET.parse('RP06505.XML')


def getHeader():
	string = "TRP_ID#TRP_ATA#TRP_PORT_FROM#VES_VESSEL_NAME#VES_VESSEL_FLAG#TRP_CURRENT_LOCATION#AGT_NAME#TYPE#START_TIME#END_TIME#ACT#LOCATION#CLR_NEXT_PORT" 
	return string

def getText(parentElement, tag):
	e = parentElement.find(tag)
	if e is not None:
		return e.text if e.text is not None else ""
	else:
		return ""

def main():
	tree = ET.parse(filename)
	root = tree.getroot()
	lgv_elem = root.find("LIST_G_VESSEL")
	print_header = True
	# Print header
	#gv_elem = lgv_elem.find("G_VESSEL")
	#string = ""
	#for e in gv_elem.iter():
	#	if isLeaf(e):
	#		string += e.tag + sep
	#print string + "\n"
	print getHeader();

	em = root.find("LIST_G_VESSEL")
	# Print each of the value
	for gv in em.findall("G_VESSEL"):
		row = Row(getText(gv, "TRP_ID"), getText(gv, "TRP_ATA"), getText(gv, "TRP_PORT_FROM"), getText(gv, "VES_VESSEL_NAME"), getText(gv, "VES_VESSEL_FLAG"), getText(gv, "TRP_CURRENT_LOCATION"), getText(gv, "AGT_NAME"))
		lga = gv.find("LIST_G_ACTIVITY")
		for ga in lga.findall("G_ACTIVITY"):
			row.addActivity("", getText(ga, "TYPE"), getText(ga, "START_TIME"), getText(ga, "END_TIME"), getText(ga, "ACT"), getText(ga, "LOCATION"))	

		lgn = gv.find("LIST_G_NEXT_PORT")
		for gn in lgn.findall("G_NEXT_PORT"):
			row.addNextPort(getText(gn, "CLR_NEXT_PORT"))	

		print row.dump() 

def isLeaf(elem):
	if sum (1 for _ in elem.iter()) == 1:
		return True
	return False

if __name__ == "__main__":
	main();
