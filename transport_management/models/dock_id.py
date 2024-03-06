# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models

class DockId(models.Model):
    
    _name = 'dock.id.config'
    _description = 'Dock Id'
    
    name = fields.Char(String = 'Dock Id')