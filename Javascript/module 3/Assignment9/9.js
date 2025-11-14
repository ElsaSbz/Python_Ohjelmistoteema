function calculate() {
    var cal_str = document.getElementById("calculation").value;

    var res = 0;
    var nums = [];
    if (cal_str.includes("+")) {
        nums = cal_str.split("+").map(Number);
        res = nums[0] + nums[1];
    } else if (cal_str.includes("-")) {
        nums = cal_str.split("-").map(Number);
        res = nums[0] - nums[1];
    } else if (cal_str.includes("*")) {
        nums = cal_str.split("*").map(Number);
        res = nums[0] * nums[1];
    } else if (cal_str.includes("/")) {
        nums = cal_str.split("/").map(Number);
        res = nums[0] / nums[1];
    } else {
        res = "Invalid operation";
    }
  document.getElementById("result").innerHTML = res;

}