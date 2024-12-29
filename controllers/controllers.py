# -*- coding: utf-8 -*-
# from odoo import http


# class GestionTurnos(http.Controller):
#     @http.route('/gestion__turnos/gestion__turnos/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestion__turnos/gestion__turnos/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestion__turnos.listing', {
#             'root': '/gestion__turnos/gestion__turnos',
#             'objects': http.request.env['gestion__turnos.gestion__turnos'].search([]),
#         })

#     @http.route('/gestion__turnos/gestion__turnos/objects/<model("gestion__turnos.gestion__turnos"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestion__turnos.object', {
#             'object': obj
#         })
