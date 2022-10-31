from odoo import fields, models
from datetime import date

class SchoolStudent (models.Model):
    _name = 'school.student'
    _description = 'Student Record'
    
    name = fields.Char(string='Name student')
    birth_date = fields.Date(string='Birth date')
    age = fields.Integer(compute='_compute_age',string='Age')
    final_exam_grade = fields.Float(string='Final exam grade')
    subject_ids = fields.Many2many('school.subject', string='Subject')
    
    def _compute_age(born):
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    
    

    