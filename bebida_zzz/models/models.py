# -*- coding: utf-8 -*-

from odoo import models, fields, api

class BebidaZzz(models.Model):
    _name = 'bebida.zzz'
    _description = 'REGISTRAMOS TU SUEÑO Y TE RECOMENDAMOS UNA BEBIDA'

    # CAMPO 1: EL NOMBRE DEL ALUMNO
    alumno = fields.Char(
        string='ALUMNO',
        required=True
    )

    # CAMPO 2: EL NIVEL DE SUEÑO DEL ALUMNO
    nivel_sueno = fields.Integer(
        string='NIVEL DE SUEÑO',
        required=True,
        help="Valor entre 1 y 10"
    )

    # CAMPO 3: LA BEBIDA RECOMENDADA
    bebida_recomendada = fields.Char(
        string='BEBIDA RECOMENDADA',
        compute='_compute_bebida',
        store=True,
        readonly=True
    )

    # MÉTODO PARA CALCULAR LA BEBIDA EN FUNCIÓN DEL NIVEL DE SUEÑO DEL PANOLI
    @api.depends('nivel_sueno')
    def _compute_bebida(self):
        for record in self:
            nivel = record.nivel_sueno
            if 1 <= nivel <= 3:
                record.bebida_recomendada = 'Café con leche'
            elif 4 <= nivel <= 6:
                record.bebida_recomendada = 'Café solo largo'
            elif 7 <= nivel <= 9:
                record.bebida_recomendada = 'Café solo larguísimo'
            elif nivel == 10:
                record.bebida_recomendada = 'Inyección de adrenalina'
            else:
                record.bebida_recomendada = 'ERRORRR: nivel debe ser 1-10'