from odoo import api, models, fields
import json, requests

class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def create(self, vals):
        res = super(ResPartner, self).create(vals)

        if "vat" in vals and not "fel_nombre_sat" in vals:
            if vals["vat"] == 'CF':
                vals["fel_nombre_sat"] = 'Consumidor Final'
            else:
                # url = "https://consultareceptores.feel.com.gt/rest/action"
                url = self.env.company.fel_url_nit

                data = {
                    # 'emisor_codigo': "2459413K",
                    # 'emisor_clave': "46155CE198281D56C1F479082C6946C7",
                    'emisor_codigo': self.env.company.fel_emisor_codigo,
                    'emisor_clave': self.env.company.fel_emisor_clave,
                    'nit_consulta': vals["vat"]
                }

                headers = {
                    'Content-Type': "application/json"
                }

                response = requests.post(url, json=data, headers=headers)

                data = json.loads(response.text)

                vals["fel_nombre_sat"] = data['nombre']
                res.fel_nombre_sat = data['nombre']

        return res

    def write(self, vals):
        res = super(ResPartner, self).write(vals)

        if "vat" in vals:
            # url = "https://consultareceptores.feel.com.gt/rest/action"
            url = self.env.company.fel_url_nit

            data = {
                # 'emisor_codigo': "2459413K",
                # 'emisor_clave': "46155CE198281D56C1F479082C6946C7",
                'emisor_codigo': self.env.company.fel_emisor_codigo,
                'emisor_clave': self.env.company.fel_emisor_clave,
                'nit_consulta': vals["vat"]
            }

            headers = {
                'Content-Type': "application/json"
            }

            response = requests.post(url, json=data, headers=headers)

            data = json.loads(response.text)

            vals["fel_nombre_sat"] = data['nombre']
            self.fel_nombre_sat = data['nombre']

        return res