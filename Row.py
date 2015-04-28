# 14:TRP_ID,TRP_ATA,TRP_PORT_FROM,VES_VESSEL_NAME,VES_VESSEL_FLAG,TRP_CURRENT_LOCATION,AGT_NAME,TRIP_ID,TYPE,START_TIME,END_TIME,ACT,LOCATION,LIST_G_NEXT_PORT,


class Row:
	def __init__(self, trp_id, trp_ata, trp_port_from, ves_vessel_name, ves_vessel_flag, trp_current_location, agt_name):
		self.trp_id = str(trp_id)
		self.trp_ata = trp_ata
		self.trp_port_from = trp_port_from
		self.ves_vessel_name = ves_vessel_name
		self.ves_vessel_flag = ves_vessel_flag
		self.trp_current_location = trp_current_location
		self.agt_name = agt_name
		self.activitylist = []
		self.nextportlist = []


	class Activity:
		def __init__(self, trip_id, t_type, start_time, end_time, act, location):
			self.trip_id = str(trip_id)
			self.t_type = t_type
			self.start_time = start_time
			self.end_time = end_time
			self.act = act
			self.location = location

	def addActivity(self, trip_id, t_type, start_time, end_time, act, location):
		activity = self.Activity(trip_id, t_type, start_time, end_time, act, location)
		self.activitylist.append(activity)	


	class NextPort:
		def __init__(self, clr_next_port):
			self.clr_next_port = clr_next_port
	
	def addNextPort(self, clr_next_port):
		nextport = self.NextPort(clr_next_port)
		self.nextportlist.append(nextport)

	def printParent(self, activity, port):
		al = ["", "", "", "", ""]
		if not activity is None:
			al = []
			al.append(activity.t_type)
			al.append(activity.start_time)
			al.append(activity.end_time)
			al.append(activity.act)
			al.append(activity.location)
		if not port is None:
			pl = port.clr_next_port
		else:
			pl = ""

		string = self.trp_id + "," + self.trp_ata + "," + self.trp_port_from + "," + self.ves_vessel_name + "," + self.ves_vessel_flag + "," + self.trp_current_location + "," + self.agt_name + "," + al[0] + "," + al[1]  + "," + al[2] + "," + al[3] + "," + al[4] + "," + pl
		return string

	def printNoParent(self, activity, port):
		al = ["", "", "", "", ""]
		if not activity is None:
			al = []
			al.append(activity.t_type)
			al.append(activity.start_time)
			al.append(activity.end_time)
			al.append(activity.act)
			al.append(activity.location)
		if not port is None:
			pl = port.clr_next_port
		else:
			pl = ""

		string = ""
		for i in range(0,7):
			string += ","
		string += al[0] + "," + al[1]  + "," + al[2] + "," + al[3] + "," + al[4] + "," + pl
		return string

	def dump(self):
		len_a = len(self.activitylist)
		len_p = len(self.nextportlist)
		len_max = max(len_a, len_p)	
		len_max = max(len_max, 1)
		string = ""
		for i in range(0, len_max):
			a = self.activitylist[i] if len(self.activitylist) > i else None
			p = self.nextportlist[i] if len(self.nextportlist) > i else None
			if i == 0:
				string += self.printParent(a, p) + "\n"
			else:
				string += self.printNoParent(a,p) + "\n"
		
		return string	
					
def main():
	print "Begin!"
	row = Row(15013213,"2015/03/14 16:13" ,"OPEN SEA" , "YMH LIVE FISH CARRIER" , "PHI", "LUKCHAU" , "ISM SHIPPING AGENT COMPANY"); 
	print row.dump()

	row.addActivity("","A","2015/04/27 12:50","" ,"COK","")
	row.addNextPort("");
	print row.dump()

	row.addActivity("", "A", "2015/04/27 12:22", "", "CAK", "")	
	print row.dump()

	row.addActivity("", "B", "2015/12/12 13:50", "", "JAK", "")
	row.addNextPort("TOKUYAMA")
	print row.dump()

	row.addNextPort("JAKARTA")
	print row.dump()

	row.addNextPort("CIREBON")
	print row.dump()

if __name__ == "__main__":
	main()

