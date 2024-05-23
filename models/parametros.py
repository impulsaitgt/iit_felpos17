from odoo import models, fields, api

class Parametros(models.Model):
    _name = 'parametros'
    _description = 'Modelo para enviar parametros de envl'

    @api.model
    def get_env_info(self):
        # Supongamos que quieres obtener información del usuario actual
        company = self.env.user
        return {
            'fel_url_nit': self.env.company.fel_url_nit,
            'fel_emisor_codigo': self.env.company.fel_emisor_codigo,
            'fel_emisor_clave': self.env.company.fel_emisor_clave
        }
