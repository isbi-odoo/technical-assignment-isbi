# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api
from datetime import datetime, timedelta


class TrasnportStockPicking(models.Model):
    
    _inherit = 'stock.picking'
    
    weight = fields.Float(string="Product Weight", compute='_compute_weight_and_volume')
    volume = fields.Float(string="Product Volume", compute='_compute_weight_and_volume')
    
    @api.depends('weight', 'volume')
    def _compute_weight_and_volume(self):
        for record in self:
            total_weight = sum(move.product_id.weight for move in record.picking_id)
            total_volume = sum(move.product_id.volume for move in record.picking_id)
            record.weight = total_weight
            record.volume = total_volume
