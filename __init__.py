#This file is part esale_product module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.pool import Pool
from .product import *
from .shop import *


def register():
    Pool.register(
        EsaleAttributeGroup,
        Template,
        EsaleExportStart,
        EsaleExportResult,
        SaleShop,
        module='esale_product', type_='model')
    Pool.register(
        EsaleExportProduct,
        EsaleExportPrice,
        EsaleExportStock,
        EsaleExportImage,
        module='esale_product', type_='wizard')
