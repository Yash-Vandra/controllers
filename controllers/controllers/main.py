from odoo import http
from odoo.http import request

class TestController(http.Controller):
    @http.route(['/test/'], type="http", auth="public", website="True")
    def testcontroller(self, **post):
        testcontroller = request.env['res.partner'].sudo().search([])
        print(testcontroller, 'Testtttttttttttttttttt')
        values = {
            'test_controller': testcontroller
        }

        return request.render("controller_task.test_controller", values)