from flask import jsonify

class Response:

    @classmethod
    def success(self, data):
        return jsonify({
            'code': '200',
            'msg':'操作成功',
            'data':data
        })
    @classmethod
    def error(self, data):
        return jsonify({
            'code': '400',
            'msg': '操作失败',
            'data': data
        })
