# This file is part esale_product module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from . import configuration
from . import product
from . import shop

def register():
    Pool.register(
        configuration.Configuration,
        product.EsaleAttributeGroup,
        product.Template,
        product.Product,
        product.EsaleExportStart,
        product.EsaleExportResult,
        product.EsaleExportCSVStart,
        product.EsaleExportCSVResult,
        shop.SaleShop,
        module='esale_product', type_='model')
    Pool.register(
        product.EsaleExportProduct,
        product.EsaleExportPrice,
        product.EsaleExportImage,
        product.EsaleExportCSV,
        module='esale_product', type_='wizard')
