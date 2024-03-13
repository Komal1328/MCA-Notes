#pr12

class Time():
    def __init__(self,h,m,s):
        self.h=h
        self.m=m
        self.s=s

    def add(self,obj):
        tot_s=self.s + obj.s
        carry_m,new_s=divmod(tot_s,60)
        tot_m=self.m + obj.m + carry_m
        carry_h,new_m=divmod(tot_m,60)
        tot_h=self.h + obj.h + carry_h
        return Time(tot_h,new_m,new_s)

    def display(self):
        h_str=str(self.h).rjust(2,'0')
        m_str=str(self.m).rjust(2,'0')
        s_str=str(self.s).rjust(2,'0')
        print(h_str,":",m_str,":",s_str)

time1=Time(3,4,59)
time2=Time(7,2,1)
time3=time1.add(time2)
time3.display()
