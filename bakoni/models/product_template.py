from odoo import api, fields, models


class nappi_code(models.Model):
    _name = 'nappi.code'
    _description = "NAPPI Code"

    name = fields.Char(string="NAPPI Code")


class icd_10_code(models.Model):
    _name = 'icd.10.code'
    _description = "ICD 10 Code"

    name = fields.Char(string="ICD 10 Code")


class product_template(models.Model):
    _inherit = 'product.template'

    nappi_code_id = fields.Many2one('nappi.code', string="NAPPI Code")
    icd_10_code_id = fields.Many2one('icd.10.code', string="ICD 10 Code")