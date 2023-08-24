# -*- coding: utf-8 -*-
from odoo import api, fields, models, _




class hms_patient(models.Model):
     _name = "hms.patient"

     name = fields.Char()
     l_name = fields.Char(string="l_name")
     birth_date = fields.Date()
     history = fields.Html()
     cr_ratio = fields.Float()
     image = fields.Binary()
     address = fields.Text()
     blood_type = fields.Selection([('O', "O"), ('A', "A")], default="O")




     states = fields.Selection([('f', "Fair"), ('s', "Serious"), ('u', "Undetermined"), ('g', "Good")], default="g")





     age = fields.Float()
     pcr = fields.Boolean()



     department_id = fields.Many2one("hms.department",domain=[('Is_opened', '=', True)])
     # The  patient   can’t  choose   a  closed department

     doctors_id = fields.Many2one("hms.doctors")
     history_ids = fields.Many2many("hms.history")






     # @api.depends('birth_date')
     # def age_calc(self):
     #
     #      if self.birth_date is not False:
     #           self.age = (datetime.today().date() - datetime.strptime(self.date_of_birth, '%Y-%m-%d').date()) // timedelta(days=365)

     # ..............................


     email = fields.Char()

     @api.model
     def create(self, vals):
          new_patient = super().create(vals)

          name_split = new_patient.name.split()
          new_patient.email = f"{name_split[0][0]}{name_split[1]} @gmail.com"
          return new_patient
     # ..............................




# ------------------------------
     log_ids = fields.One2many('hms.log', 'model_id', string='سجلات الحالة')

     def write(self, vals):
          old_state = self.states
          result = super(hms_patient, self).write(vals)
          new_state = vals.get('states', old_state)

          if old_state != new_state:
               self.log_ids.create({
                    'model_id': self.id,
                    'description': f'تم تغيير الحالة إلى {new_state}'
               })

          return result

     # ------------------------------

     # If The  pcr  field is checked, the  CR  ratio field should    be  mandatory

     @api.onchange('cr_ratio')
     def _on_change_cr_ratio(self):
          if self.cr_ratio != 0:
               self.pcr = True
          else:
               self.pcr = False

# ------------------------------




# history

class hms_history(models.Model):
     _name = "hms.history"
     _rec_name = "description"

     name = fields.Char()
     date = fields.Date()
     description = fields.Html()


# ------------------------------
# With each change of the state a new log record is being created with a description of (State changed to NEW_STATE)
class MyModelLog(models.Model):
    _name = 'hms.log'
    _rec_name = "description"

    model_id = fields.Many2one('hms.patient', string='النموذج')
    description = fields.Char(string='الوصف')




# ------------------------------
