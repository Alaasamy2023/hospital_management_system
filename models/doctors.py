# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
class hms_doctors(models.Model):
     _name = "hms.doctors"

     name = fields.Char()
     l_Name = fields.Char()
     image = fields.Binary()
