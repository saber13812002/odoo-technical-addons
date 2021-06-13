# -*- coding: utf-8 -*-
from datetime import datetime
from odoo import models, fields, api


class feature_2(models.Model):
    _name = 'hr.employee'
    # _description = 'feature_2.feature_2'
    _inherit = 'hr.employee'
    field1 = fields.Date(string='joining date')
    field2 = fields.Char(string='Years of Experience',compute='_calc_date')
    
    @api.depends('field1','field2')
    def _calc_date(self):
        years = 0;
        months = 0;
        days = 0;
        if self.field1:
            d1 = self.field1
            d2 = datetime.date(datetime.now())
            d3 = (d2 - d1).days
            # Calculating years
            if d3>=365:
                years = d3/365
                d3 = d3%365
            # Calculating months
            if d3>=30:
                months = d3/30
                d3 = d3%30
            # Calculating days
            days = d3
            self.field2 = str(int(days)) + ' days,' + str(int(months)) + ' months and ' + str(int(years))+' years'
        else:
            self.field2 = "Set <joining date>, to get <Years of Experience>"
        # self.field2 = d1
#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100