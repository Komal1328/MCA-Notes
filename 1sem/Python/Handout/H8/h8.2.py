#h8.2
class Time:
    def __init__(self,hr,mi,sec):
        self.h=hr
        self.m=mi
        self.s=sec
    def addt(self,obj):
        tot_s=self.s+obj.s
        carry_m,new_s= divmod(tot_s,60)
        tot_m=self.m+obj.m+carry_m
        carry_h,new_m= divmod(tot_m,60)
        new_h=carry_h+self.h+obj.h
        return Time(new_h,new_m,new_s)
    def display(self):
        h_str=str(self.h).rjust(2,'0')
        m_str=str(self.m).rjust(2,'0')
        s_str=str(self.s).rjust(2,'0')
        print("Addtion: ",h_str,":",m_str,":",s_str)

time1=Time(7,40,10)
time2=Time(7,30,50)
time=time1.addt(time2)
time.display()
        
        
