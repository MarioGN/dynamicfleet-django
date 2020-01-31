$(document).ready(function() {
  jQuery.datetimepicker.setLocale('pt-BR');

  $("#id_start").datetimepicker({
    format: 'd/m/Y H:i',
    onShow:function(ct){
        this.setOptions({
          maxDate:jQuery('#id_end').val()?jQuery('#id_end').val():false
        })
    },
  });

  $("#id_end").datetimepicker({      
    format: 'd/m/Y H:i',
    onShow:function(ct){
      this.setOptions({
        minDate:jQuery('#id_start').val()?jQuery('#id_start').val():false
      })
    },
  });

  $("#filter-start").datetimepicker({
    format: 'd/m/Y H:i',
    onShow:function(ct){
        this.setOptions({
          maxDate:jQuery('#filter-end').val()?jQuery('#filter-end').val():false
        })
    },
  });

  $("#filter-end").datetimepicker({      
    format: 'd/m/Y H:i',
    onShow:function(ct){
      this.setOptions({
        minDate:jQuery('#filter-start').val()?jQuery('#filter-start').val():false
      })
    },
  });
});