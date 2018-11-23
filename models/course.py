# -*- coding: utf-8 -*-

from odoo import api, models, fields


class Course(models.Model):
    _name = 'openacademy.course'

    name = fields.Char(
        required=True,
        string='Title',
    )
    description = fields.Text(
    )
    responsible_id = fields.Many2one(
        comodel_name='res.users',
        ondelete='set null',
        string='Responsible',
        index=True,
    )
    session_ids = fields.One2many(
        comodel_name='openacademy.session',
        inverse_name='course_id',
        string='Sessions',
    )

    @api.multi
    def copy(self, default=None):
        default = dict(default or {})

        copied_count = self.search_count(
            [('name', '=like', u"Copy of {}%".format(self.name))])
        if not copied_count:
            new_name = u"Copy of {}".format(self.name)
        else:
            new_name = u"Copy of {} ({})".format(self.name, copied_count)

        default['name'] = new_name
        new_course = super(Course, self).copy(default)
        for session in self.session_ids:
            session.copy().course_id = new_course
        return new_course

    _sql_constraints = [
        ('name_description_check',
         'CHECK(name != description)',
         "The title of the course should not be the description"),

        ('name_unique',
         'UNIQUE(name)',
         "The course title must be unique"),
    ]
