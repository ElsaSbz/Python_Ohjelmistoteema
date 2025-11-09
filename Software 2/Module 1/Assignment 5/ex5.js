//Write a program that asks the user to enter a year and notifies the user whether the input year is a leap year. A year is a leap year if it is divisible by four. However, years divisible by 100 are leap years only if they are also divisible by 400. Print the result on the HTML document.
const yearstr = prompt("Enter the year :")
const year=parseFloat(yearstr)
let result ;
if  (year%4 ==0) {
    if(year%100 == 0 ){
        result = "The year is a leap year";
    }
    else {
        result = "The year is not a leap year";
    }
}
else {
        result = "The year is not a leap year";
}
document.getElementById('result').innerText = result;