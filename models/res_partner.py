import os
from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    audio_file_ids = fields.One2many('customer.audio.file', 'partner_id', string="Audio Files")

    @api.model
    def import_audio_files(self):
        audio_dir = '/path/to/your/audio/files/'
        for filename in os.listdir(audio_dir):
            if filename.endswith('.mp3') or filename.endswith('.wav'):
                phone_number = filename.split('_')[0]  # Assuming the filename format is phone_number_something.mp3
                partner = self.search([('phone', '=', phone_number)], limit=1)
                if partner:
                    file_path = os.path.join(audio_dir, filename)
                    file_content = open(file_path, 'rb').read()
                    self.env['customer.audio.file'].create({
                        'partner_id': partner.id,
                        'name': filename,
                        'audio_file': file_content,
                        'file_type': 'audio/mpeg' if filename.endswith('.mp3') else 'audio/wav'
                    })

class CustomerAudioFile(models.Model):
    _name = 'customer.audio.file'
    _description = 'Customer Audio File'

    name = fields.Char(string="Filename")
    partner_id = fields.Many2one('res.partner', string="Customer", ondelete='cascade')
    audio_file = fields.Binary(string="Audio File", attachment=True)
    file_type = fields.Char(string="MIME Type")