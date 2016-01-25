# This file is part esale_product module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import Pool, PoolMeta
from trytond.transaction import Transaction

from sql import Literal


__all__ = ['Configuration']
__metaclass__ = PoolMeta


class Configuration:
    __name__ = 'product.configuration'
    esale_attribute_group = fields.Property(fields.Many2One('esale.attribute.group',
            'eSale Attribute Group'))

    @classmethod
    def __register__(cls, module_name):
        pool = Pool()
        Module = pool.get('ir.module')

        cursor = Transaction().cursor
        module = Module.__table__()

        cursor.execute(*module.update(
                columns=[module.state],
                values=[Literal('to remove')],
                where=module.name == Literal('product_configuration')
                ))

        super(Configuration, cls).__register__(module_name)
