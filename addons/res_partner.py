from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    audio_file_ids = fields.Many2many(
        'ir.attachment', 
        string="Audio Files", 
        domain=[('mimetype', 'ilike', 'audio/')]
    )
