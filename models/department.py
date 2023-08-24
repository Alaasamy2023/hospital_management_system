# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
class hms_department(models.Model):
     _name = "hms.department"

     name = fields.Char()
     Capacity = fields.Integer()
     Is_opened = fields.Boolean()
     # Patients = fields.Char()

