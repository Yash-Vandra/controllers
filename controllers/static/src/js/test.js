var ajax = require('web.ajax');//To define ajaxvar
 test_variable = document.getElementById("name_id").value;//To get value from the required field.
ajax.jsonRpc('/test/', 'call', {
'test_variable' : test_variable,
});//json Rpc Call
.then(function (data) {});
//To receive data from python(non-mandatory)