# -*- coding: utf-8 -*-

from odoo import models, fields, api
class Products(models.Model):
    _inherit = 'product.template'

    arabic_name = fields.Char(string="Arabic Name", required=False, )


