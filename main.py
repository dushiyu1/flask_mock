import json
import random

from flask import Flask, jsonify, request

from data.sap_data import SapData
from response.response import Response
from unit.log import Logger
from vo.sapVo import sapVo

app = Flask(__name__)
# ========== 关键配置：强制UTF-8编码 ==========
app.config['JSON_AS_ASCII'] = False  # 禁用ASCII编码，返回原生中文
app.config['JSONIFY_MIMETYPE'] = 'application/json; charset=utf-8'  # 响应头指定UTF-8

@app.route('/api/zmdms-esb-sap/sap/open/call', methods=['POST'])
def sap_call():
    year = request.json['year']
    month = request.json['month']
    prctr = request.json['prctr']

    Logger.info(request.json)

    if year == '' or month == '' or prctr == '' or year is None or month is None or prctr is None:
        Logger.info("年份/月份/利润中心不可为空")
        return Response.error("年份/月份/利润中心不可为空")

    if year == '2025' and month == '10' and prctr == 'SSX':
        res_data = SapData.get_2025_10_SSX_data()
    elif year == '2025' and month == '09' and prctr == 'SSX':
        res_data = SapData.get_2025_09_SSX_data()
    else:
        res_data = SapData.get_data(year=year, month=month, prctr=prctr)
    Logger.info(res_data)
    return Response.success(data=res_data)


@app.route('/test/login',methods=['GET'])
def test():
    if request.args.get('username') == None or request.args.get('password') == None:
        return Response.error({"msg":"用户名或密码不能为空"})
    elif request.args.get('username') == 'admin' and request.args.get('password') != 'admin':
        return Response.error({"msg":"用户名或密码错误"})
    elif request.args.get('username') == 'admin' and request.args.get('password') == 'admin':
        return Response.success({"msg":"登陆成功"})
    else:
        return Response.error({"msg":"登录异常"})

if __name__ == '__main__':
    app.run(debug=False)