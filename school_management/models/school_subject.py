from odoo import fields, models

class SchoolSubject(models.Model):
    _name = 'school.subject'
    _description = 'School Subject Record'
    
    name = fields.Char(string='Name subject')
    credits = fields.Integer(string='Credits')
    max_students = fields.Integer(string='Max students')
    active = fields.Boolean(string='Active')
    student_ids = fields.Many2many('school.student',string='Student')
    teacher_id = fields.Many2one('school.teacher', string='Teacher')
    
    
