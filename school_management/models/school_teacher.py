from odoo import fields, models

class SchoolTeacher (models.Model):
    _name = 'school.teacher'
    _description = 'Teacher Record'
    
    name = fields.Char(string='Name teacher')
    profile = fields.Text(string='Profile')
    subject_ids= fields.One2many('school.subject', 'teacher_id', string='Subject')