# 创建一个列表来存储路由分组
from flask import Blueprint

route_groups = []

# 自定义函数来创建路由分组
def create_route_group(prefix, name):
    group_bp = Blueprint(name, __name__, url_prefix=prefix)
    route_groups.append(group_bp)
    return group_bp

# 示例：创建一个名为"api"的路由分组
api_bp = create_route_group('/api', 'api')