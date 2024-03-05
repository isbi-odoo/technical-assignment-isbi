from odoo import fields, models, api

class TransportBatchTransfer(models.TransientModel):
    
    _inherit = 'res.config.settings'
    
    module_transport_management = fields.Boolean(String="Dispatch Management System")