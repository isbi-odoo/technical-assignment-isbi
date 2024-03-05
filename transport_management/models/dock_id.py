from odoo import fields, models

class DockId(models.Model):
    
    _name = 'dock.id.config'
    _description = 'Dock Id'
    
    name = fields.Char(String = 'Dock Id')