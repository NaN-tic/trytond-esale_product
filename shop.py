#This file is part esale_product module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
from trytond.model import ModelView, fields
from trytond.transaction import Transaction
from trytond.pool import PoolMeta

__all__ = ['SaleShop']
__metaclass__ = PoolMeta


class SaleShop:
    __name__ = 'sale.shop'
    esale_last_products = fields.DateTime('Last Products', 
        help='This date is last export (filter)')
    esale_last_prices = fields.DateTime('Last Prices', 
        help='This date is last export (filter)')
    esale_last_stocks = fields.DateTime('Last Stocks', 
        help='This date is last export (filter)')
    esale_last_images = fields.DateTime('Last Images', 
        help='This date is last export (filter)')
    esale_last_menus = fields.DateTime('Last Menus', 
        help='This date is last export (filter)')
    esale_top_menu = fields.Many2One('esale.catalog.menu', 'Top Menu')

    @classmethod
    def __setup__(cls):
        super(SaleShop, cls).__setup__()
        cls._error_messages.update({
            'stock_not_export': 'Threre are not stock to export',
            'menu_not_export': 'Select a top menu in sale shop',
        })
        cls._buttons.update({
                'export_products': {},
                'export_prices': {},
                'export_stocks': {},
                'export_images': {},
                'export_menus': {},
                })

    @classmethod
    @ModelView.button
    def export_products(self, shops):
        """
        Export Products to External APP
        """
        for shop in shops:
            export_products = getattr(shop, 'export_products_%s' % shop.esale_shop_app)
            export_products(shop)

    @classmethod
    @ModelView.button
    def export_prices(self, shops):
        """
        Export Prices to External APP
        """
        for shop in shops:
            export_prices = getattr(shop, 'export_prices_%s' % shop.esale_shop_app)
            export_prices(shop)

    @classmethod
    @ModelView.button
    def export_stocks(self, shops):
        """
        Export Stocks to External APP
        """
        for shop in shops:
            export_stocks = getattr(shop, 'export_stocks_%s' % shop.esale_shop_app)
            export_stocks(shop)

    @classmethod
    @ModelView.button
    def export_images(self, shops):
        """
        Export Images to External APP
        """
        for shop in shops:
            export_images = getattr(shop, 'export_images_%s' % shop.esale_shop_app)
            export_images(shop)

    @classmethod
    @ModelView.button
    def export_menus(self, shops):
        """
        Export Menus to External APP
        """
        for shop in shops:
            if not shop.esale_top_menu:
                self.raise_user_error('menu_not_export')
            export_menus = getattr(shop, 'export_menus_%s' % shop.esale_shop_app)
            export_menus(shop)

    def export_products_tryton(self, shop):
        """Export Products to Tryton e-Sale
        :param shop: Obj
        """
        #TODO: Export Tryton product
        active_ids = Transaction().context.get('active_ids')
        return True

    def export_prices_tryton(self, shop):
        """Export Prices to Tryton e-Sale
        :param shop: Obj
        """
        #TODO: Export Tryton prices
        active_ids = Transaction().context.get('active_ids')
        return True

    def export_stocks_tryton(self, shop):
        """Export Stocks to Tryton e-Sale
        :param shop: Obj
        """
        self.raise_user_error('stock_not_export')

    def export_images_tryton(self, shop):
        """Export Images to Tryton e-Sale
        :param shop: Obj
        """
        #TODO: Export Tryton images
        active_ids = Transaction().context.get('active_ids')
        return True

    def export_menus_tryton(self, shop):
        """Export Menus to Tryton e-Sale
        :param shop: Obj
        """
        #TODO: Export Tryton menus
        return True
