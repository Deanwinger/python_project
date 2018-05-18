from flask import g, request
from functools import singledispatch
from app.exception import ExceptionResponse
import wrapt


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
                for key, value in params_except.items():
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
            for key, value in params_option.items():
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


# big problem
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
        if params_except is not None and data is None:
            raise ExceptionResponse(401, "参数非法")
        try:
            for key, val in params_except.items():
                if not type_check(data[key], val):
                    raise ExceptionResponse(401, "错误的参数类型")
                g.params[key] = data[key] if not isinstance(data[key], str) else data[key].strip()
        except KeyError:
            raise ExceptionResponse(401, "参数非法")
        return wrapped(*args, **kwargs)

    return decorated_function

def type_check(obj, target_type):
    return isinstance(obj, target_type)
