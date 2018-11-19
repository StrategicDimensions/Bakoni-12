from odoo import api, fields, models

class account_invoice(models.Model):
    _inherit = 'account.invoice'

    tender_ref = fields.Char(string="Tender Reference", related="partner_id.tender_ref")
    customer_ref = fields.Char(string="Customer Reference", related="partner_id.ref")