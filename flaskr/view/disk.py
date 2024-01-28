from flask import Blueprint

from ..service.hardware import Hardware

bp = Blueprint('disk', __name__, url_prefix='/disk')


@bp.route('/usage', methods=['GET'])
def disk_usage():
    hw = Hardware()

    return str(hw.get_disk_usage())
