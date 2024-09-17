# Part of OpenG2P Registry. See LICENSE file for full copyright and licensing details.
import logging

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)

class G2PIndividualEducationLevel(models.Model):
    _name = "g2p.individual.education.level"
    _description = "Education Level"
    _order = "id desc"

    name = fields.Char("Education Level")

    @api.constrains("name")
    def _check_name(self):
        edu_lvl = self.search([])
        for record in self:
            if not record.name:
                error_message = _("Education Level should not empty.")
                raise ValidationError(error_message)
        for record in edu_lvl:
            if self.name.lower() == record.name.lower() and self.id != record.id:
                raise ValidationError(_("Education Level already exists"))
