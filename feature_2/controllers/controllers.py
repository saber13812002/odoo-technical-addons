# -*- coding: utf-8 -*-
# from odoo import http


# class Feature2(http.Controller):
#     @http.route('/feature_2/feature_2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/feature_2/feature_2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('feature_2.listing', {
#             'root': '/feature_2/feature_2',
#             'objects': http.request.env['feature_2.feature_2'].search([]),
#         })

#     @http.route('/feature_2/feature_2/objects/<model("feature_2.feature_2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('feature_2.object', {
#             'object': obj
#         })
