from decimal import Decimal
from enum import Enum

import logging

logging.basicConfig(level=logging.INFO)

class Package(Enum):
    STANDARD = 'STANDARD'
    SPECIAL = 'SPECIAL'
    REJECTED = 'REJECTED'

# Dimensions are in centimeters, mass is in kilograms
MAX_DIMENSION = Decimal('150.0')
MAX_VOLUME = Decimal('1000000.0')
MAX_MASS = Decimal('20.0')

def sort(width: Decimal, height: Decimal, length: Decimal, mass: Decimal) -> str:
    if width <= 0 or height <= 0 or length <= 0 or mass <= 0:
        logging.info("Package rejected due to invalid dimensions or mass.")
        return Package.REJECTED.value

    volume = width * height * length
    has_max_volume = volume >= MAX_VOLUME
    has_max_dimension = any(d >= MAX_DIMENSION for d in (width, height, length))
    is_bulky = has_max_dimension or has_max_volume
    is_heavy = mass >= MAX_MASS

    if is_bulky and is_heavy:
        return Package.REJECTED.value
    elif is_bulky or is_heavy:
        return Package.SPECIAL.value
    else:
        return Package.STANDARD.value
