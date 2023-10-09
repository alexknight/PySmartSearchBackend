from . import api_bp
from .api_impl import *


@api_bp.route('/search', methods=['POST'])
def search_route():
    return search()


@api_bp.route('/match_data', methods=['POST'])
def match_data_route():
    return match_data()