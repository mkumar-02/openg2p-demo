# Part of OpenG2P Registry. See LICENSE file for full copyright and licensing details.
import logging

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)

class G2PSourceOfIncome(models.Model):
    _name = "g2p.source.of.income"
    _description = "Source Of Income"
    _order = "id desc"

    name = fields.Char("Source Of Income")

    @api.constrains("name")
    def _check_name(self):
        emp_lvl = self.search([])
        for record in self:
            if not record.name:
                error_message = _("Source Of Income should not empty.")
                raise ValidationError(error_message)
        for record in emp_lvl:
            if self.name.lower() == record.name.lower() and self.id != record.id:
                raise ValidationError(_("Source Of Income already exists"))

