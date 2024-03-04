# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api
from datetime import datetime, timedelta


class TrasnportStockPicking(models.Model):
    
    _inherit = 'stock.picking'
    
    weight = fields.Float(String ="Product Weight" , related="product_id.weight")
    volume = fields.Float(String ="Product Volume" , related="product_id.volume")
    
    @api.depends('weight', 'volume')
    def _compute_weight(self):
        for record in self:
            total_weight = sum(move.quantity * move.product_id.weight for move in record.move_ids)
            total_volume = sum(move.quantity * move.product_id.volume for move in record.move_ids)
            record.weight = total_weight
            record.volume = total_volume
