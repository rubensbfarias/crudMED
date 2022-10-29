var SPMaskBehavior = function (val) {
    return val.replace(/\D/g, '').length === 11 ? '(00) 00000-0000' : '(00) 0000-00009';
  },
  spOptions = {
    onKeyPress: function(val, e, field, options) {
        field.mask(SPMaskBehavior.apply({}, arguments), options);
      }
  };
  
django.jQuery(function(){
    django.jQuery('.mask-phone').mask(SPMaskBehavior, spOptions);
    django.jQuery('.mask-cep').mask('00000-000');

    function limpa_formulário_cep() {
        django.jQuery("#id_city").val("");
        django.jQuery("#id_uf").val("");
        django.jQuery("#id_address").val("")
    } 
    django.jQuery("#id_cep").blur(function() {
        var cep = $(this).val().replace(/\D/g, '');
        if (cep != "") {
            var validacep = /^[0-9]{8}$/;
            if(validacep.test(cep)) {
                django.jQuery("#id_city").val("...");
                django.jQuery("#id_uf").val("...");
                django.jQuery("#id_address").val("...")
                django.jQuery("#id_country").val("Brazil")
                django.jQuery.getJSON("https://viacep.com.br/ws/"+ cep +"/json/?callback=?", function(dados) {

                    if (!("erro" in dados)) {
                        django.jQuery("#id_city").val(dados.localidade);
                        django.jQuery("#id_uf").val(dados.uf);
                        django.jQuery("#id_address").val(dados.logradouro);
                    }
                    else {
                        limpa_formulário_cep();
                        alert("CEP não encontrado.");
                    }
                });
            } 
            else {
                limpa_formulário_cep();
                alert("Formato de CEP inválido.");
            }
        }
        else {
            limpa_formulário_cep();
        }
    });
});

