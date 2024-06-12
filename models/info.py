from odoo import fields, models, api


class AccountMoveInfo(models.Model):
    _inherit = 'account.move'
    move_lines = fields.Many2one('reports.info', string='Lineas Factura')


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

    """
    Notes: Get invoives by customers
    - Use search in differents models
    """
    def get_all_invoices(self):
        customer = self.env['account.move'].search([('state', '=', 'posted'),
                                                    ('partner_id', '=', self.partner_id.id)])
        return customer

    #invoice_ids = fields.One2many('account.move', 'move_lines', string='Facturas')

    def imprimir_reporte(self):
        for res in self:
            data={
                "docs": res,
            }
            return self.env.ref('reports.report_reports_info').report_action(self, data=data)

