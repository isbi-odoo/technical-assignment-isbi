# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api
from datetime import datetime, timedelta
from odoo.exceptions import UserError ,ValidationError

class TransportBatchTransfer(models.Model):
    
    _inherit = 'stock.picking.batch'
    
    dock_id = fields.Many2one("dock.id.config" ,string ="Dock Id") 
    vehicle_category_id = fields.Many2one('fleet.vehicle.model.category',string="Vehicle Category")
    vehicle_id = fields.Many2one('fleet.vehicle',string="Vehicle",placeholder='semi-truck')
    product_id = fields.Many2one('stock.picking',string="Product Id")
    weight = fields.Float("Weight" , compute='_compute_weight_volume' ,store=True)
    volume = fields.Float("Volume" , compute='_compute_weight_volume' ,store =True)
    transfer = fields.Float(string='Transfer', compute='_compute_transfer' , store=True)
    
    
    @api.depends('weight', 'volume')
    def _compute_weight_volume(self):
        for record in self:
            total_weight = sum(move.product_qty * move.product_id.weight for move in record.move_ids)
            total_volume = sum(move.product_qty * move.product_id.volume for move in record.move_ids)
            if record.vehicle_category_id.max_weight != 0 :
                record.weight = total_weight/record.vehicle_category_id.max_weight
                
            if record.vehicle_category_id.max_volume != 0 :
                record.volume = total_volume/record.vehicle_category_id.max_volume

    
    def _compute_transfer(self):
        for record in self:
            record.transfer = len(record.picking_ids)
            
