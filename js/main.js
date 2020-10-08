(function () {
    "use strict";

    var regalo = document.getElementById('regalo');



    document.addEventListener('DOMContentLoaded', function () {

        // Campos Datos Usuarios

        var nombre = document.getElementById('nombre');
        var apellido = document.getElementById('apellido');
        var email = document.getElementById('email');

        //Campos pases

        var pase_dia = document.getElementById('pase_dia');
        var pase_dosdias = document.getElementById('pase_dosdias');
        var pase_completo = document.getElementById('pase_completo');

        //Botones y Divs

        var calcular = document.getElementById('calcular');
        var errorDiv = document.getElementById('error');
        var botonRegistro = document.getElementById('btnRegistro');
        var lista_productos = document.getElementById('lista-productos');
        var suma = document.getElementById('suma-total');

        //Extras

        var cantidadEtiquetas = document.getElementById('etiquetas');
        var camisas = document.getElementById('camisa_evento');

        if (document.getElementById('calcular')) {

            calcular.addEventListener('click', calcularMontos);

            pase_dia.addEventListener('blur', mostrarDias);
            pase_dosdias.addEventListener('blur', mostrarDias);
            pase_completo.addEventListener('blur', mostrarDias);

            nombre.addEventListener('blur', validarCampos);
            apellido.addEventListener('blur', validarCampos);
            email.addEventListener('blur', validarCampos);
            email.addEventListener('blur', validarMail);


            function validarCampos() {

                if (this.value == '') {
                    errorDiv.style.display = 'block';
                    errorDiv.innerHTML = "Este campo es obligatorio";
                    this.style.border = '1px solid red';
                    errorDiv.style.border = '1px solid red';
                } else {
                    errorDiv.style.display = 'none';
                    this.style.border = '3px solid green';
                }
            }

            function validarMail() {

                if (this.value.indexOf("@") > -1) {

                    errorDiv.display = 'none';
                    this.style.border = '3px solid green';
                } else {
                    errorDiv.style.display = 'block';
                    errorDiv.innerHTML = "Debe contener un '@'";
                    this.style.border = '1px solid red';
                    errorDiv.style.border = '1px solid red';
                }

            }

            function calcularMontos(event) {

                event.preventDefault();

                if (regalo.value === '') {

                    alert("Debes elegir un regalo");
                    regalo.focus();

                } else {

                    var boletoDia = parseInt(pase_dia.value, 10) || 0,
                        boleto2Dias = parseInt(pase_dosdias.value, 10) || 0,
                        boletoCompleto = parseInt(pase_completo.value, 10) || 0,
                        cantCamisas = parseInt(camisas.value, 10) || 0,
                        cantEtiquetas = parseInt(etiquetas.value, 10) || 0;

                    var totalPagar = (boletoDia * 30) + (boleto2Dias * 45) + (boletoCompleto * 50) + ((cantCamisas * 10) * .93) + (cantEtiquetas * 2);


                    var listadoProductos = [];

                    if (boletoDia >= 1) {

                        listadoProductos.push(boletoDia + ' Pases por día');

                    }
                    if (boleto2Dias >= 1) {

                        listadoProductos.push(boleto2Dias + ' Pases por dos días');

                    }
                    if (boletoCompleto >= 1) {

                        listadoProductos.push(boletoCompleto + ' Pases completos');

                    }
                    if (cantCamisas >= 1) {

                        listadoProductos.push(cantCamisas + ' Camisas');

                    }
                    if (cantEtiquetas >= 1) {

                        listadoProductos.push(cantEtiquetas + ' Etiquetas');

                    }

                    lista_productos.style.display = "block";

                    lista_productos.innerHTML = '';

                    for (var i = 0; i < listadoProductos.length; i++) {

                        lista_productos.innerHTML += listadoProductos[i] + '<br/>';

                    }

                    suma.innerHTML = "$ " + totalPagar.toFixed(2);

                }
            }

            function mostrarDias() {

                var boletoDia = parseInt(pase_dia.value, 10) || 0,
                    boleto2Dias = parseInt(pase_dosdias.value, 10) || 0,
                    boletoCompleto = parseInt(pase_completo.value, 10) || 0;

                var diasElegidos = [];

                if (boletoDia > 0) {
                    diasElegidos.push('viernes');
                    // console.log(diasElegidos);
                }
                if (boleto2Dias > 0) {
                    diasElegidos.push('viernes', 'sabado');
                    // console.log(diasElegidos);
                }
                if (boletoCompleto > 0) {
                    diasElegidos.push('viernes', 'sabado', 'domingo');
                    // console.log(diasElegidos);
                }

                for (var i = 0; i < diasElegidos.length; i++) {

                    document.getElementById(diasElegidos[i]).style.display = 'block';

                }

            }

        }

    }); //DOM CONTENT LOADED

})();



$(function () {

    //Lettering

    $('.nombre-sitio').lettering();

    //Menu Fijo

    var windowHeight = $(window).height();
    var barraAltura = $('.barra').innerHeight();

    $(window).scroll(function () {

        var scroll = $(window).scrollTop();

        if (scroll > windowHeight) {
            $('.barra').addClass('fixed');
            $('body').css({
                'margin-top': barraAltura + 'px'
            });
        } else {
            $('.barra').removeClass('fixed');
            $('body').css({
                'margin-top': '0px'
            });
        }

    });

    //Menú Sandwich Responsive

    $('.menu-movil').on('click', function () {
        $('.navegacion-principal').slideToggle();
    });

    //Programa de conferencias

    $('div.ocultar').hide();

    $('.programa-evento .info-curso:first').show();

    $('.menu-programa a:first').addClass('activo');

    $('.menu-programa a').on('click', function () {

        $('.menu-programa a').removeClass('activo');
        $(this).addClass('activo');

        $('.ocultar').hide();

        var enlace = $(this).attr('href');
        $(enlace).fadeIn(1200);

        return false;
    });

    //Animaciones para el contador 

    $('.resumen-evento li:nth-child(1) p').animateNumber({
        number: 6
    }, 1200);
    $('.resumen-evento li:nth-child(2) p').animateNumber({
        number: 15
    }, 1200);
    $('.resumen-evento li:nth-child(3) p').animateNumber({
        number: 3
    }, 1500);
    $('.resumen-evento li:nth-child(4) p').animateNumber({
        number: 9
    }, 1500);

    //Mapa

    var map = L.map('mapa').setView([-33.500089, -70.616641], 15);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    L.marker([-33.500089, -70.616641]).addTo(map)
        .bindPopup('<strong>Frontistirio</strong>  <br/> <small>Centro Operacional</small>')
        .openPopup();

    //Cuenta Regresiva

    $('.cuenta-regresiva').countdown('2020/11/10 09:00:00', function (event) {

        $('#dias').html(event.strftime('%D'));
        $('#horas').html(event.strftime('%H'));
        $('#minutos').html(event.strftime('%M'));
        $('#segundos').html(event.strftime('%S'));

    });

});