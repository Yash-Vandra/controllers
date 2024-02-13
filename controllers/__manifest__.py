{
    'name': "Controller Task",
    'depends': ['base', 'sale_management', 'mail'],
    'data': [
        'views/main_template_views.xml',
    ],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_frontend': [
            'controller_task/static/src/js/test.js',
        ]
    }
}