# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api
from datetime import datetime, timedelta


class TransportBatchTransfer(models.Model):
    
    _inherit = 'stock.picking.batch'
    
    vehicle_category_id = fields.Many2one('fleet.vehicle.model.category',string="Vehicle Category")
    vehicle_id = fields.Many2one('fleet.vehicle',string="Vehicle",placeholder='semi-truck')
    product_id = fields.Many2one('stock.picking',string="Product Id")
    weight = fields.Float("Weight" , compute='_compute_weight')
    volume = fields.Float("Volume" , compute='_compute_volume')
    
    @api.depends('weight' , 'volume')
    def _compute_weight(self):
        for record in self:
            record.weight = record.product_id.weight
            record.volume = record.product_id.volume
        
    
    # @api.depends('weight')
    # def _compute_weight(self):
    #     max_weight = 0
    #     for record in self:
    #         max_weight = max(max_weight ,fl.max_weight (for fl in record.vehicle_category_id)