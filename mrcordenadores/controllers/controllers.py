# -*- coding: utf-8 -*-
from odoo import http

# class Mrcordenadores(http.Controller):
#     @http.route('/mrcordenadores/mrcordenadores/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mrcordenadores/mrcordenadores/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mrcordenadores.listing', {
#             'root': '/mrcordenadores/mrcordenadores',
#             'objects': http.request.env['mrcordenadores.mrcordenadores'].search([]),
#         })

#     @http.route('/mrcordenadores/mrcordenadores/objects/<model("mrcordenadores.mrcordenadores"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mrcordenadores.object', {
#             'object': obj
#         })