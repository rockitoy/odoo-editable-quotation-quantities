# -*- coding: utf-8 -*-
# This module and its content is copyright of Technaureus Info Solutions Pvt. Ltd.
# - © Technaureus Info Solutions Pvt. Ltd 2021. All rights reserved.

from odoo import api, fields, models
from ast import literal_eval


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    quotation_quantities = fields.Boolean(string="Editable Quotation Quantities", default=False)

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        ICPSudo = self.env['ir.config_parameter'].sudo()
        quotation_quantities = ICPSudo.get_param('odoo_editable_quotation_quantities.quotation_quantities')
        res.update(
            quotation_quantities=quotation_quantities)
        print(res)
        return res

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        ICPSudo = self.env['ir.config_parameter'].sudo()
        ICPSudo.set_param("odoo_editable_quotation_quantities.quotation_quantities",
                          self.quotation_quantities)
