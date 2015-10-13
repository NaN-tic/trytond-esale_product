# This file is part esale_product module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from .configuration import *
from .product import *
from .shop import *

def register():
    Pool.register(
        Configuration,
        EsaleAttributeGroup,
        Template,
        EsaleExportStart,
        EsaleExportResult,
        SaleShop,
        module='esale_product', type_='model')
    Pool.register(
        EsaleExportProduct,
        EsaleExportPrice,
        EsaleExportImage,
        module='esale_product', type_='wizard')
