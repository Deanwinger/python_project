import wrapt
import json
from flask import g, request, Response


def decorate_body_params(params_except=None, params_option=None):
    """
    1.应用通用参数验证装饰器，若验证成功则将数据写入g.params
    2.增加检查必传参数的检查，不予许空字符串传入
    3.增字段类型检查
    :param
        params_except [dict]    Json内的必选参数
        params_option [dict]    Json内的可选参数
    """

    @wrapt.decorator
    def decorated_function(wrapped, instance, args, kwargs):
        data = request.json
        g.params = {}
        if params_except is not None:
            if data is None:
                raise ExceptionResponse(401, "参数非法")
            try:
                for key, value in params_except.itmes():
                    if value == 'str':
                        if not isinstance(data[key], str):
                            raise ExceptionResponse(401, "错误的参数类型")
                        g.params[key] = data[key].strip()
                    elif value == 'int':
                        if not isinstance(data[key], int):
                            raise ExceptionResponse(401, "错误的参数类型")
                        g.params[key] = data[key]
                    else:
                        raise ExceptionResponse(401, "参数非法")
            except KeyError:
                raise ExceptionResponse(401, "参数非法")
        if params_option is not None:
            for key, value in params_option.itmes():
                try:
                    if value == 'str':
                        if not isinstance(data[key], str):
                            raise ExceptionResponse(401, "错误的参数类型")
                        g.params[key] = data[key].strip()
                    elif value == 'int':
                        if not isinstance(data[key], int):
                            raise ExceptionResponse(401, "错误的参数类型")
                        g.params[key] = data[key]
                    else:
                        raise ExceptionResponse(401, "参数非法")
                except KeyError:
                    g.params[key] = None
        return wrapped(*args, **kwargs)

    return decorated_function


class ExceptionResponse(Exception):
    """标准返回异常，此异常能被 public.decorate_resource 装饰器拦截病返回相应的 HTTP 错误"""

    def __init__(self, status: int, msg: str):
        self.http_status = status
        self.err_msg = msg

    def __str__(self):
        return repr(self.err_msg)

def decorate_resource():
    """RESTFul Json标准返回值装饰器，拦截标准异常转化为 HTTP 错误码"""

    @wrapt.decorator
    def decorated_function(wrapped, instance, args, kwargs):
        try:
            data = wrapped(*args, **kwargs)
            resp = Response(json.dumps(data, ensure_ascii=False))
            resp.headers["Content-Type"] = "application/json; charset=UTF-8"
            resp.status_code = 200
            return resp
        except Exception as e:
            if hasattr(e, "http_status") and hasattr(e, "err_msg"):
                resp = Response(json.dumps({"msg": e.err_msg}, ensure_ascii=False))
                resp.headers["Content-Type"] = "text/plain; charset=UTF-8"
                resp.status_code = e.http_status
                return resp
            raise e

    return decorated_function