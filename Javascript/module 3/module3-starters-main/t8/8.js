function calculate(){
      var str_num1 = document.getElementById("num1").value;
      var num1 = parseInt(str_num1);
      var str_num2 = document.getElementById("num2").value;
      var num2 = parseInt(str_num2);
      var operation = document.getElementById("operation").value;

      let res = 0.0
      switch(operation) {
          case "add":
            res = num1 + num2;
            break;
          case "sub":
              res = num1 - num2;
            break;
          case "multi":
            res = num1 * num2;
            break;
          case "div":
            res = num1 / num2;
            break;
      }

      document.getElementById("result").innerHTML = res;

}