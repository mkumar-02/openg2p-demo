# Part of OpenG2P Registry. See LICENSE file for full copyright and licensing details.
import logging

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class G2PResPartnerInherited(models.Model):
    _inherit = "res.partner"

    kind_name = fields.Boolean(default=True)

    # Individual personal info
    employment_status_id = fields.Many2one("g2p.individual.employment.status")
    marital_status_id = fields.Many2one("g2p.individual.marital.status")
    education_level_id = fields.Many2one("g2p.individual.education.level")


    # Economic Status Infomation
    source_of_income_id = fields.Many2one("g2p.source.of.income")
    annual_income = fields.Integer()
    owns_two_wheeler = fields.Selection([('yes', 'Yes'), ('no', 'No')])
    owns_three_wheeler = fields.Selection([('yes', 'Yes'), ('no', 'No')])
    owns_four_wheeler = fields.Selection([('yes', 'Yes'), ('no', 'No')])
    owns_cart = fields.Selection([('yes', 'Yes'), ('no', 'No')])
    land_ownership = fields.Selection([('yes', 'Yes'), ('no', 'No')])
    type_of_land_owned_id = fields.Many2one("g2p.type.of.land")
    land_size = fields.Float()
    owns_house = fields.Selection([('yes', 'Yes'), ('no', 'No')])
    owns_livestock = fields.Selection([('yes', 'Yes'), ('no', 'No')])

    # Social Status Information
    pregnent_and_lactating_women = fields.Integer()
    malnourished_children_under_five = fields.Integer()
    disablity = fields.Integer()
    type_of_disablity = fields.Many2one("g2p.type.of.disability")
    caste_ethnic_group = fields.Many2one("g2p.type.of.caste")
    protected_group = fields.Selection([('yes', 'Yes'), ('no', 'No')])
    vulnerable_status = fields.Selection([('yes', 'Yes'), ('no', 'No')])
    
    @api.onchange('kind')
    def _onchange_kind(self):
        if self.kind.name=="Household":
            self.write({'kind_name': False})
        else:
            self.write({'kind_name': True})