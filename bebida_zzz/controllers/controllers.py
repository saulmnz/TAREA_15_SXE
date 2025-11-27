# -*- coding: utf-8 -*-
# from odoo import http


# class BebidaZzz(http.Controller):
#     @http.route('/bebida_zzz/bebida_zzz', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bebida_zzz/bebida_zzz/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bebida_zzz.listing', {
#             'root': '/bebida_zzz/bebida_zzz',
#             'objects': http.request.env['bebida_zzz.bebida_zzz'].search([]),
#         })

#     @http.route('/bebida_zzz/bebida_zzz/objects/<model("bebida_zzz.bebida_zzz"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bebida_zzz.object', {
#             'object': obj
#         })

