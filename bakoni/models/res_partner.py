from odoo import api, fields, models

class res_partner(models.Model):
    _inherit = 'res.partner'

    medical_aid_name = fields.Char(string="Medical Aid Name")
    medical_aid_number = fields.Char(string="Medical Aid Number")
    patient_id_number = fields.Char(string="Patient Identification Number")
    customer_type = fields.Selection([('default', 'Default'),
                                      ('end_user', 'End user'),
                                      ('medical_aid', 'Medical aid'),
                                      ('practice', 'Practice'),
                                      ('private', 'Private'),
                                      ('public', 'Public')], default='default',  string="Customer Type")
    practice_number = fields.Char(string="Practice No.")
    tender_ref = fields.Char(string="Tender Reference")
    