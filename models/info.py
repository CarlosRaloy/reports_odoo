from odoo import fields, models, api


class Info(models.Model):
    _name = 'reports.info'
    _description = 'Reporte de informacion'

    name = fields.Char("📝 Nombre Reporte")
    partner_id = fields.Many2one('res.partner', "🏭 Factory / Company")
    well_view = fields.Selection([
        ('1', '🔴 Cancel'),
        ('2', '🟡 Back to review'),
        ('3', '🟢 Succesful'),
    ], "🔍 VoBo")
