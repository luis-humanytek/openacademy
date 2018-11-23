# -*- coding: utf-8 -*-
from odoo import fields, models


class Partner(models.Model):
    _inherit = 'res.partner'

    instructor = fields.Boolean(
        default=False,
        string='Instructor',
    )
    session_ids = fields.Many2many(
        comodel_name='openacademy.session',
        readonly=True,
        string='Attended Sessions',
    )
