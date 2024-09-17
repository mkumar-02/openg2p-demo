# -*- coding: utf-8 -*-
{
    'name': "registry",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ["base", "mail","g2p_registry_base", "g2p_registry_group", "g2p_registry_individual"],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/marital_status_views.xml',
        'views/employment_status_views.xml',
        'views/education_level_views.xml',
        'views/source_of_income_views.xml',
        'views/type_of_land_views.xml',
        'views/type_of_caste_views.xml',
        'views/type_of_disability_views.xml',
        'views/household_economic_status_views.xml',
        'views/household_social_status_views.xml',

        'views/individual_views.xml',
    ],
}

