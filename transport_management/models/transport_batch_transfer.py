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
    weight = fields.Float("Weight" , compute='_compute_weight_volume',store = True)
    volume = fields.Float("Volume" , compute='_compute_weight_volume', store = True)
    transfer = fields.Float(string='Transfer', compute='_compute_transfer',store = True)
    line = fields.Float(string='Line', compute='_compute_line' ,store =True)
    
    
    @api.depends('weight', 'volume','vehicle_category_id')
    def _compute_weight_volume(self):
        for record in self:
            for record in self:
                if record.vehicle_category_id or record.vehicle_category_id.max_weight != 0:
                    record.weight = (sum(record.picking_ids.mapped('weight'))*100/record.vehicle_category_id.max_weight)
                    record.volume = (sum(record.picking_ids.mapped('volume'))*100/record.vehicle_category_id.max_volume)
                else:
                    record.weight=0
                    record.volume=0

    
    def _compute_transfer(self):
        for record in self:
            record.transfer = len(record.picking_ids)
    
    def _compute_line(self):
        for record in self:
            record.line = len(record.move_ids)
    
    @api.depends('weight', 'volume')
    def _compute_display_name(self):
        for batch in self:
            batch.display_name = f"{batch.vehicle_id.location}: {batch.weight}kg, {batch.volume}m\N{SUPERSCRIPT THREE} {batch.vehicle_id.driver_id.name}"
