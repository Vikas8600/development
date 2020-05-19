#-*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.http import request


class product_restric(models.Model):
    _inherit = "product.template"
    _description = "partner for product"
    
    partner_ids = fields.Many2many('res.partner', string="partner_ids")

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"
    _description = "Sales Order Line"

    @api.onchange('product_id')
    def product_id_change(self):
        # domain = super(SaleOrderLine, self).product_id_change()
        # p_id = self.env['product.product'].search([('partner_ids', 'in', self.order_id.partner_id.ids)])
        return {'domain': {'product_id': [('partner_ids', 'in', [self.order_id.partner_id.id])]}}

class count_product(models.Model):
    _inherit = 'res.partner'


    count_product = fields.Integer(compute='_compute_marksheet',readonly=True)

    def _compute_marksheet(self):
        self.count_product = self.env['product.template'].search_count(
            [('partner_ids', 'in',self.id )])
    def action_view_product(self):
        return {
            'name': ('Subscriptions'),
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'product.template',
            'view_id': False,
            'type': 'ir.actions.act_window',
            'domain': [('partner_ids', '=', self.id)]
        }




















        
