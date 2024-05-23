odoo.define('iit_felpos.custom_client_details_edit', function (require) {
    "use strict";

    var rpc = require('web.rpc');

    // Observar el evento de cambio en el documento para campos con el nombre "vat"
    $(document).ready(function() {
        // Define la función para capturar el cambio de valor del input
        window.captureInputValue = function(input) {
            var inputValue = input.value;
            // Realiza acciones adicionales aquí según sea necesario
            rpc.query({
                model: 'parametros',
                method: 'get_env_info',
                args: [],
            }).then(function (result) {
                var fel_url_nit = result.fel_url_nit;
                var fel_emisor_codigo = result.fel_emisor_codigo;
                var fel_emisor_clave = result.fel_emisor_clave;
                const url = fel_url_nit;

                const data = {
                    emisor_codigo: fel_emisor_codigo,
                    emisor_clave: fel_emisor_clave,
                    nit_consulta: inputValue // Suponiendo que 'vals' es un objeto en JavaScript
                };

                const headers = {
                    'Content-Type': "application/json"
                };

                // Usando fetch para hacer la petición POST
                fetch(url, {
                    method: 'POST',
                    headers: headers,
                    body: JSON.stringify(data)
                })
                .then(response => response.json())
                .then(data => {
                    // Intentar copiar el texto al portapapeles
                    navigator.clipboard.writeText(data.nombre)
                        .then(function() {
                            window.alert('El cliente esta registrado en la SAT como '+data.nombre+', hemos guardado su nombre en el portapapeles por si te sirve el dato')
                            var fel_nombre_sat = document.querySelector('input[name="fel_nombre_sat"]');
                               if (fel_nombre_sat) {
                                    fel_nombre_sat.value = data.nombre;
                               }
                        })
                        .catch(function(err) {
                            console.error('Error al copiar texto al portapapeles: ', err);
                        });
                }).catch(function (err) {
                   console.error('Error: ', err);
                });
            // Aquí puedes manejar los datos de la respuesta
        })
        .catch(error => {
            fel_nombre_sat.value = ""; // Aquí puedes poner el valor que desees asignar""
                        console.error('Error:', error);
        });

        }


        // Agregar el evento onchange al campo "vat"
        var vatInput = document.querySelector('input[name="vat"]');
        if (vatInput) {
            vatInput.setAttribute('onchange', 'captureInputValue(this)');
        }

    });


});
