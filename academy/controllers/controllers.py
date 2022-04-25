# -*- coding: utf-8 -*-
from odoo import http


class Academy(http.Controller):
    # Simple controller
    @http.route('/academy/academy', auth='public')
    def index(self, **kw):
        return http.request.render('academy.index', {
            'teachers': ["John Doe", "Jane Smith", "Jack Black"],
        })

    # Controller that uses the website arg
    @http.route('/academy/academy/database', auth='public', website=True)
    def index_database(self, **kw):
        Teachers = http.request.env['academy.teachers']
        return http.request.render('academy.index_database', {
            'teachers': Teachers.search([])
        })
        
    # Controller with a variable 
    @http.route('academy/academy/<int:id>', auth='public', website=True)
    def teacher(self, id):
        return '<h1>{} ({})</h1>'.format(id, type(id).__name__)


    @http.route('/academy/<model("academy.teachers"):teacher>', auth='public', website=True)
    def teacher_model(self, teacher):
        return http.request.render('academy.biography', {
            'person': teacher
        })