# -*- coding: utf-8 -*-
{
    'name': "hms",
    'sequence': -100,
    'summary': """
        Hospitals Management System""",

    'description': """
       Hospitals Management System
    """,

    'author': "alaa samy",
    'website': "http://www.alaa_samy.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['crm'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/patient.xml',
        'views/department.xml',
        'views/doctors.xml',

    ],

    'application': True,
}