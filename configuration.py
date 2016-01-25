# This file is part esale_product module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta


__all__ = ['Configuration']
__metaclass__ = PoolMeta


class Configuration:
    __name__ = 'product.configuration'
    esale_attribute_group = fields.Property(fields.Many2One('esale.attribute.group',
            'eSale Attribute Group'))
