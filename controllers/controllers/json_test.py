from odoo import http
from odoo.http import request

class MyWebController(http.Controller):
    @http.route('/test/', type='json', auth='user')
    def my_controller_method(self, **kwargs):
        # Your controller logic goes here
        # You can access the request parameters using the **kwargs dictionary
        return {'result': 'success'}
        # product_data = self.env['product.product'].search([])
        # print(product_data)
        # values = {
        #     'product_data': product_data
        # }
        #
        # return request.render("controller_task.test_controller", values)