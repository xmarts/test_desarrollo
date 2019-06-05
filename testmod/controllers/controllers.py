# -*- coding: utf-8 -*-
from odoo import http

# class Testmod(http.Controller):
#     @http.route('/testmod/testmod/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/testmod/testmod/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('testmod.listing', {
#             'root': '/testmod/testmod',
#             'objects': http.request.env['testmod.testmod'].search([]),
#         })

#     @http.route('/testmod/testmod/objects/<model("testmod.testmod"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('testmod.object', {
#             'object': obj
#         })