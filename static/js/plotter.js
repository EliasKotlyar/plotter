function submitCommand(command)
{
  $.ajax(
      {
        url : command,
        success : function(data)
        {

        }
      }
  );

}

$(document).ready(
    function()
    {
      $(['up', 'down', 'left', 'right', 'draw','go']).each(
        function(index, item)
        {
          $('#' + item).on('click',
            function(event)
            {
                var x =  parseInt($('#xvalue').val());
                var y = parseInt($('#yvalue').val());
                var step = parseInt($('#step').val());

              //submitCommand(item);
              switch (item){
                  case 'up':
                      y = y + step;
                      break;
                  case 'down':
                      y = y - step;
                      break;
                  case 'left':
                      x = x - step;
                      break;
                  case 'right':
                    x = x + step;
                    break;
              }
              $('#xvalue').val(x);
              $('#yvalue').val(y);

              switch (item){
                  case "draw":
                      command = "/drawPixel";
                      break;
                  default:
                      command = "/goToPixel"
              }
                command = command + "?x="+x+"&y="+y;
                submitCommand(command)

            }
          );


        }
      );
    }
);
