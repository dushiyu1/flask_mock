import random


class sapVo():

    def __init__(self,GJAHR,MONAT,PRCTR,RACCT,ACC_N,RFAREA,C_D_SUM,HSL_E):
        self.GJAHR = GJAHR
        self.MONAT = MONAT
        self.PRCTR = PRCTR
        self.RACCT = RACCT
        self.ACC_N = ACC_N
        self.RFAREA = RFAREA
        self.RFA_N = "管理费用"
        self.C_D_SUM = C_D_SUM if C_D_SUM is not None else round(random.uniform(1.0, 100.0), 2)
        self.HSL_E = HSL_E if HSL_E is not None else round(random.uniform(1.0, 100.0), 2)

    def to_dict(self):
        return {
            "GJAHR": self.GJAHR,
            "MONAT": self.MONAT,
            "PRCTR": self.PRCTR,
            "RACCT": self.RACCT,
            "ACC_N": self.ACC_N,
            "RFAREA": self.RFAREA,
            "RFA_N": self.RFA_N,
            "C_D_SUM": self.C_D_SUM,
            "HSL_E": self.HSL_E
        }