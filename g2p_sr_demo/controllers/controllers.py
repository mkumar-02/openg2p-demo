# -*- coding: utf-8 -*-
# from odoo import http


# class Registry(http.Controller):
#     @http.route('/registry/registry', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/registry/registry/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('registry.listing', {
#             'root': '/registry/registry',
#             'objects': http.request.env['registry.registry'].search([]),
#         })

#     @http.route('/registry/registry/objects/<model("registry.registry"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('registry.object', {
#             'object': obj
#         })

