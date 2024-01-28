from flask import Blueprint

from ..service.hardware import Hardware

bp = Blueprint('config', __name__, url_prefix='/config')


@bp.route('/int', methods=['GET'])
def config_int():
    hw = Hardware()

    return str(hw.get_config_int())
