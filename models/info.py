from odoo import fields, models, api


class Info(models.Model):
    _name = 'reports.info'
    _description = 'Reporte de informacion'

    name = fields.Char("📝 Tittle Report")
    partner_id = fields.Many2one('res.partner', "🏭 Factory / Company")
    well_view = fields.Selection([
        ('1', '🔴 Cancel'),
        ('2', '🟡 Back to review'),
        ('3', '🟢 Succesful'),
    ], "🔍 VoBo")

    invoice_ids = fields.One2many('account.move', 'partner_id', string='Facturas')

    def imprimir_reporte(self):
        for res in self:
            data={
                "docs": res,
            }
            return self.env.ref('reports.report_reports_info').report_action(self, data=data)
