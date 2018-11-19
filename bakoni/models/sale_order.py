from odoo import api, fields, models

class sale_order(models.Model):
    _inherit = 'sale.order'

    tender_ref = fields.Char(string="Tender Reference", related="partner_id.tender_ref")