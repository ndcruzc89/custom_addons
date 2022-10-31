{
    'name': "School Management",

    'summary': """
        App para gestión escolar
    """,

    'description': """
        Gestión escolar para el registro de asignaturas, estudiantes y profesores.
    """,

    'author': "Nelson Daniel Cruz Camelo",
    'website': "https://www.linkedin.com/in/nelsoncruz89/",

    'category': 'School',
    'version': '1.0',

    'depends': [
        'base',
    ],

    'data': [
        'views/school_subject_views.xml',
        'views/school_student_views.xml',
        'views/school_teacher_views.xml',
        'views/menu_item_views.xml',
        'security/ir.model.access.csv',
    ],
    
    'application': True,
    'installable': True,
    'auto_install': False,
}