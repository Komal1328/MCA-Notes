class Time:
	def __init__(self,h,m,s):
		self.hr = h
		self.mi = m
		self.se = s
	def add_time(self, obj):
		total_s = self.se + obj.se 
		carry_over_m, new_s = divmod(total_s,60)
		total_m = self.mi + carry_over_m + obj.mi
		carry_over_h, new_m = divmod(total_m,60)
		new_h = carry_over_h + self.hr + obj.hr
		return Time(new_h, new_m, new_s)
	def display(self):
		h_str = str(self.hr).rjust(2, '0')
		m_str = str(self.mi).rjust(2, '0')		
		s_str = str(self.se).rjust(2, '0')
		print(h_str + ":" + m_str + ":" + s_str)
time = Time(7,40,10)
time2 = Time(7,30,50)
time3 = time.add_time(time2)
time3.display()