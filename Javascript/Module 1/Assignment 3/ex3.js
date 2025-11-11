//Write a program that prompts for three integers.
//The program prints the sum,product and average of the numbers to the HTML document. (3p)
// remember to convert strings to numbers when adding them together.
const int1str =prompt('Type first number.');
const int2str =prompt('Type second number.');
const int3str =prompt('Type third number.');
const int1 =parseInt(int1str);
const int2 =parseInt(int2str);
const int3 =parseInt(int3str);
const sum =int1 + int2 + int3;
const p = int1 * int2 * int3;
const avg = sum / 3;
document.querySelector('#target').innerHTML = 'Sum is:  ' + sum + '\nProduct is:' + p + '\nAvarage is:' + avg;
