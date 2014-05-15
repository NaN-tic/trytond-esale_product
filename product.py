#This file is part esale_product module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
from trytond.model import ModelView, ModelSQL, fields
from trytond.wizard import Wizard, StateTransition, StateView, Button
from trytond.pool import Pool, PoolMeta
from trytond.transaction import Transaction

__all__ = ['EsaleAttributeGroup', 'Template', 'EsaleExportStart',
    'EsaleExportResult', 'EsaleExportProduct', 'EsaleExportPrice',
    'EsaleExportStock', 'EsaleExportImage']
__metaclass__ = PoolMeta


class EsaleAttributeGroup(ModelSQL, ModelView):
    'Esale Attribute Group'
    __name__ = 'esale.attribute.group'
    name = fields.Char('Name', required=True)
    code = fields.Char('Code', required=True)
    active = fields.Boolean('Active')

    @staticmethod
    def default_active():
        return True

class Template:
    __name__ = 'product.template'
    esale_attribute_group = fields.Many2One('esale.attribute.group', 'Attribute')


class EsaleExportStart(ModelView):
    'Export Tryton to External Shop: Start'
    __name__ = 'esale.export.start'
    shop = fields.Many2One('sale.shop', 'Shop', required=True,
            domain=[
                ('esale_available', '=', True)
            ],
            help='Select shop will be clone this product.')

    @staticmethod
    def default_shop():
        Shop = Pool().get('sale.shop')
        shops = Shop.search([('esale_available','=',True)])
        if len(shops) == 1:
            return shops[0].id
        else:
            return None

class EsaleExportResult(ModelView):
    'Export Tryton to External Shop: Result'
    __name__ = 'esale.export.result'
    info = fields.Text('Info', readonly=True)


class EsaleExportProduct(Wizard):
    'Export Products Tryton to External Shop'
    __name__ = "esale.export.product"

    start = StateView('esale.export.start',
        'esale_product.esale_export_start', [
            Button('Cancel', 'end', 'tryton-cancel'),
            Button('Clone', 'export', 'tryton-ok', default=True),
            ])
    export = StateTransition()
    result = StateView('esale.export.result',
        'esale_product.esale_export_result', [
            Button('Close', 'end', 'tryton-close'),
            ])

    @classmethod
    def __setup__(cls):
        super(EsaleExportProduct, cls).__setup__()
        cls._error_messages.update({
                'export_info': 'Export products %s IDs to %s shop',
                })

    def transition_export(self):
        shop = self.start.shop
        export_status = getattr(shop, 'export_products_%s' % shop.esale_shop_app)
        templates = Transaction().context['active_ids']
        export_status(shop, templates)
        self.result.info = self.raise_user_error('export_info', 
                (','.join(str(t) for t in templates), shop.rec_name),
                raise_exception=False)
        return 'result'

    def default_result(self, fields):
        info_ = self.result.info
        return {
            'info': info_,
            }

class EsaleExportPrice(Wizard):
    """Export Prices Tryton to External Shop"""
    __name__ = "esale.export.price"

    start = StateView('esale.export.start',
        'esale_product.esale_export_start', [
            Button('Cancel', 'end', 'tryton-cancel'),
            Button('Clone', 'export', 'tryton-ok', default=True),
            ])
    export = StateTransition()
    result = StateView('esale.export.result',
        'esale_product.esale_export_result', [
            Button('Close', 'end', 'tryton-close'),
            ])

    @classmethod
    def __setup__(cls):
        super(EsaleExportPrice, cls).__setup__()
        cls._error_messages.update({
                'export_info': 'Export product prices %s IDs to %s shop',
                })

    def transition_export(self):
        shop = self.start.shop
        export_status = getattr(shop, 'export_prices_%s' % shop.esale_shop_app)
        templates = Transaction().context['active_ids']
        export_status(shop, templates)
        self.result.info = self.raise_user_error('export_info', 
                (','.join(str(t) for t in templates), shop.rec_name),
                raise_exception=False)
        return 'result'

    def default_result(self, fields):
        info_ = self.result.info
        return {
            'info': info_,
            }

class EsaleExportStock(Wizard):
    """Export Stocks Tryton to External Shop"""
    __name__ = "esale.export.stock"

    start = StateView('esale.export.start',
        'esale_product.esale_export_start', [
            Button('Cancel', 'end', 'tryton-cancel'),
            Button('Clone', 'export', 'tryton-ok', default=True),
            ])
    export = StateTransition()
    result = StateView('esale.export.result',
        'esale_product.esale_export_result', [
            Button('Close', 'end', 'tryton-close'),
            ])

    @classmethod
    def __setup__(cls):
        super(EsaleExportStock, cls).__setup__()
        cls._error_messages.update({
                'export_info': 'Export product stocks %s IDs to %s shop',
                })

    def transition_export(self):
        shop = self.start.shop
        export_status = getattr(shop, 'export_stocks_%s' % shop.esale_shop_app)
        templates = Transaction().context['active_ids']
        export_status(shop, templates)
        self.result.info = self.raise_user_error('export_info', 
                (','.join(str(t) for t in templates), shop.rec_name),
                raise_exception=False)
        return 'result'

    def default_result(self, fields):
        info_ = self.result.info
        return {
            'info': info_,
            }

class EsaleExportImage(Wizard):
    """Export Images Tryton to External Shop"""
    __name__ = "esale.export.image"

    start = StateView('esale.export.start',
        'esale_product.esale_export_start', [
            Button('Cancel', 'end', 'tryton-cancel'),
            Button('Clone', 'export', 'tryton-ok', default=True),
            ])
    export = StateTransition()
    result = StateView('esale.export.result',
        'esale_product.esale_export_result', [
            Button('Close', 'end', 'tryton-close'),
            ])

    @classmethod
    def __setup__(cls):
        super(EsaleExportImage, cls).__setup__()
        cls._error_messages.update({
                'export_info': 'Export product images %s IDs to %s shop',
                })

    def transition_export(self):
        shop = self.start.shop
        export_status = getattr(shop, 'export_images_%s' % shop.esale_shop_app)
        templates = Transaction().context['active_ids']
        export_status(shop, templates)
        self.result.info = self.raise_user_error('export_info', 
                (','.join(str(t) for t in templates), shop.rec_name),
                raise_exception=False)
        return 'result'

    def default_result(self, fields):
        info_ = self.result.info
        return {
            'info': info_,
            }
