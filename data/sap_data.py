import json

from vo.sapVo import sapVo


class SapData:

    @classmethod
    #金额全部为0
    def get_2025_10_SSX_data(self):
        data = [
            {"RACCT":"6001123456","ACC_N":"营业总收入","RFAREA":"Y000"},
            {"RACCT": "6601010700", "ACC_N": "职工薪酬-职工福利-其他", "RFAREA": "Y000"},
            {"RACCT": "6001654321", "ACC_N": "营业总成本", "RFAREA": "Y000"},
            {"RACCT": "6601123456", "ACC_N": "销售费用", "RFAREA": "Y000"},
            {"RACCT": "6603123456", "ACC_N": "财务费用", "RFAREA": "Y000"},
            {"RACCT": "6603021234", "ACC_N": "利息支出", "RFAREA": "X100"},
            {"RACCT": "6603011234", "ACC_N": "利息收入", "RFAREA": "X100"},
            {"RACCT": "6603031234", "ACC_N": "汇兑损益", "RFAREA": "X100"},
            {"RACCT": "6701123456", "ACC_N": "资产减值损失", "RFAREA": "X100"},
            {"RACCT": "6101123456", "ACC_N": "公允价值变动收益", "RFAREA": "X100"},
            {"RACCT": "6111123456", "ACC_N": "投资收益", "RFAREA": "X100"},
            {"RACCT": "6302123456", "ACC_N": "其他收益", "RFAREA": "X100"},
            {"RACCT": "6301123456", "ACC_N": "营业外收入", "RFAREA": "X100"},
            {"RACCT": "6711123456", "ACC_N": "营业外支出", "RFAREA": "X100"},
            {"RACCT": "6601300000", "ACC_N": "劳务派遣", "RFAREA": "Y000"},
            {"RACCT": "6601010700", "ACC_N": "办公费-其他", "RFAREA": "Y000"},
            {"RACCT": "6601060000", "ACC_N": "仓储费", "RFAREA": "Y000"},
            {"RACCT": "6601180000", "ACC_N": "招待费", "RFAREA": "Y000"},
            {"RACCT": "6601270500", "ACC_N": "办公费-办公用品费", "RFAREA": "Y000"},

        ]
        sap_list = []
        for item in data:
            sap = sapVo(GJAHR='2025', MONAT='10', PRCTR='SSX', RACCT=item['RACCT'], ACC_N=item['ACC_N'], RFAREA=item['RFAREA'],C_D_SUM=0, HSL_E=0)
            sap_list.append(json.dumps(sap.to_dict(),ensure_ascii=False))

        return sap_list

    @classmethod
    #金额全部为负-100
    def get_2025_09_SSX_data(self):
        data = [
            {"RACCT": "6001123456", "ACC_N": "营业总收入", "RFAREA": "Y000"},
            {"RACCT": "6601010700", "ACC_N": "职工薪酬-职工福利-其他", "RFAREA": "Y000"},
            {"RACCT": "6001654321", "ACC_N": "营业总成本", "RFAREA": "Y000"},
            {"RACCT": "6601123456", "ACC_N": "销售费用", "RFAREA": "Y000"},
            {"RACCT": "6603123456", "ACC_N": "财务费用", "RFAREA": "Y000"},
            {"RACCT": "6603021234", "ACC_N": "利息支出", "RFAREA": "X100"},
            {"RACCT": "6603011234", "ACC_N": "利息收入", "RFAREA": "X100"},
            {"RACCT": "6603031234", "ACC_N": "汇兑损益", "RFAREA": "X100"},
            {"RACCT": "6701123456", "ACC_N": "资产减值损失", "RFAREA": "X100"},
            {"RACCT": "6101123456", "ACC_N": "公允价值变动收益", "RFAREA": "X100"},
            {"RACCT": "6111123456", "ACC_N": "投资收益", "RFAREA": "X100"},
            {"RACCT": "6302123456", "ACC_N": "其他收益", "RFAREA": "X100"},
            {"RACCT": "6301123456", "ACC_N": "营业外收入", "RFAREA": "X100"},
            {"RACCT": "6711123456", "ACC_N": "营业外支出", "RFAREA": "X100"},
            {"RACCT": "6601300000", "ACC_N": "劳务派遣", "RFAREA": "Y000"},
            {"RACCT": "6601010700", "ACC_N": "办公费-其他", "RFAREA": "Y000"},
            {"RACCT": "6601060000", "ACC_N": "仓储费", "RFAREA": "Y000"},
            {"RACCT": "6601180000", "ACC_N": "招待费", "RFAREA": "Y000"},
            {"RACCT": "6601270500", "ACC_N": "办公费-办公用品费", "RFAREA": "Y000"},

        ]
        sap_list = []
        for item in data:
            sap = sapVo(GJAHR='2025', MONAT='09', PRCTR='SSX', RACCT=item['RACCT'], ACC_N=item['ACC_N'],
                        RFAREA=item['RFAREA'], C_D_SUM=-100, HSL_E=-100)
            sap_list.append(json.dumps(sap.to_dict(), ensure_ascii=False))

        return sap_list

    @classmethod
    # 其他数据
    def get_data(self,year,month,prctr):
        data = [
            {"RACCT": "6001123456", "ACC_N": "营业总收入", "RFAREA": "Y000"},
            {"RACCT": "6601010700", "ACC_N": "职工薪酬-职工福利-其他", "RFAREA": "Y000"},
            {"RACCT": "6001654321", "ACC_N": "营业总成本", "RFAREA": "Y000"},
            {"RACCT": "6601123456", "ACC_N": "销售费用", "RFAREA": "Y000"},
            {"RACCT": "6603123456", "ACC_N": "财务费用", "RFAREA": "Y000"},
            {"RACCT": "6603021234", "ACC_N": "利息支出", "RFAREA": "X100"},
            {"RACCT": "6603011234", "ACC_N": "利息收入", "RFAREA": "X100"},
            {"RACCT": "6603031234", "ACC_N": "汇兑损益", "RFAREA": "X100"},
            {"RACCT": "6701123456", "ACC_N": "资产减值损失", "RFAREA": "X100"},
            {"RACCT": "6101123456", "ACC_N": "公允价值变动收益", "RFAREA": "X100"},
            {"RACCT": "6111123456", "ACC_N": "投资收益", "RFAREA": "X100"},
            {"RACCT": "6302123456", "ACC_N": "其他收益", "RFAREA": "X100"},
            {"RACCT": "6301123456", "ACC_N": "营业外收入", "RFAREA": "X100"},
            {"RACCT": "6711123456", "ACC_N": "营业外支出", "RFAREA": "X100"},
            {"RACCT": "6601300000", "ACC_N": "劳务派遣", "RFAREA": "Y000"},
            {"RACCT": "6601010700", "ACC_N": "办公费-其他", "RFAREA": "Y000"},
            {"RACCT": "6601060000", "ACC_N": "仓储费", "RFAREA": "Y000"},
            {"RACCT": "6601180000", "ACC_N": "招待费", "RFAREA": "Y000"},
            {"RACCT": "6601270500", "ACC_N": "办公费-办公用品费", "RFAREA": "Y000"},

        ]
        sap_list = []
        for item in data:
            sap = sapVo(GJAHR=year, MONAT=month, PRCTR=prctr, RACCT=item['RACCT'], ACC_N=item['ACC_N'],
                        RFAREA=item['RFAREA'], C_D_SUM=None, HSL_E=None)
            sap_list.append(json.dumps(sap.to_dict(), ensure_ascii=False))

        return sap_list
