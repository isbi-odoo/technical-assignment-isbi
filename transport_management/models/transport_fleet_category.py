# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class TrasnportFleetCategory(models.Model):
    
    _inherit = 'fleet.vehicle.model.category'
    
    max_weight = fields.Float(string ="Max Weight")
    max_volume = fields.Float(string="Max Volume")
    
    @api.depends('max_weight','max_volume')
    def _compute_display_name(self):
        for record in self:
            name = record.name
            if(record.max_weight or record.max_volume):
                name = f"{record.name} ({record.max_weight}kg, {record.max_volume}m\u00b3)"    
            record.display_name = name   

    # _sql_constraints = [
    # ]
    _sql_constraints = [ ('max_weight', 'CHECK( max_weight > 0)', 'The weight can not be zero.'),
        ('max_volume', 'CHECK( max_volume > 0)', 'The volume can not be zero.'),
        
    ]