# Part of OpenG2P Registry. See LICENSE file for full copyright and licensing details.
import logging

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)

class G2PIndividualMaritalStatus(models.Model):
    _name = "g2p.individual.marital.status"
    _description = "Marital Status"
    _order = "id desc"

    name = fields.Char("Marital Status")

    @api.constrains("name")
    def _check_name(self):
        marital_state = self.search([])
        for record in self:
            if not record.name:
                error_message = _("Marital status should not empty.")
                raise ValidationError(error_message)
        for record in marital_state:
            if self.name.lower() == record.name.lower() and self.id != record.id:
                raise ValidationError(_("Marital Status already exists"))
