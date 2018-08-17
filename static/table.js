$(window).load(function(){
      var data = {{data|tojson}};
      var columns = {{columns|tojson}};
      $(function() {
        $('#table').bootstrapTable({ 
          data: data,
          columns: columns,
        });
      });
    });