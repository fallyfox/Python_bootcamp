class PronetMall():
    bonus = 20000

    def __init__(self):
        print('This is a staff at Pronet Mall')

    def salary(self):
        salary_ = self.m_pay + PronetMall.bonus
        print(f'''
        Monthly pay for {self.f_name}.{self.s_name}
        ===========================================
        {salary_}
        ''')
    
class It(PronetMall):
    def __init__(self, f_name, s_name, m_pay):
        PronetMall.__init__(self)
        self.f_name = f_name
        self.s_name = s_name
        self.m_pay = m_pay

class Med(PronetMall):
    def __init__(self, f_name, s_name, m_pay):
        PronetMall.__init__(self)
        self.f_name = f_name
        self.s_name = s_name
        self.m_pay = m_pay

james = It('James','Adebo',400000)
ada = It('Ada','Emeka',410000)
aliyu = Med('Aliyu','Musa',430000)
preye = Med('Preye','Enoh',470000)

preye.salary()
