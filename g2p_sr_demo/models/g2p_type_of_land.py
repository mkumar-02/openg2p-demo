# Part of OpenG2P Registry. See LICENSE file for full copyright and licensing details.
import logging

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)

class G2PTypeOfLand(models.Model):
    _name = "g2p.type.of.land"
    _description = "Type Of Land"
    _order = "id desc"

    name = fields.Char("Type Of Land")

    @api.constrains("name")
    def _check_name(self):
        emp_lvl = self.search([])
        for record in self:
            if not record.name:
                error_message = _("Type Of Land should not empty.")
                raise ValidationError(error_message)
        for record in emp_lvl:
            if self.name.lower() == record.name.lower() and self.id != record.id:
                raise ValidationError(_("Type Of Land already exists"))
