//Write a program that prompts the user for five numbers and prints them in the reverse order they were entered (not reverse sorted).
// Print the result to the console.(2p)
// Save the numbers to an array, then use for-loop to iterate in reverse order.
// Do not use array.reverse() function.

function reverseNumbers() {
            const numbers = [];

            for (let i = 0; i < 5; i++) {
                const num = prompt(`Enter number ${i + 1}:`);
                numbers.push(num);  // Add the number to the array
            }

            let result = "Numbers in reverse order are:\n";
            for (let i = numbers.length - 1; i >= 0; i--) {
                result += numbers[i] + "\n";
            }

            console.log(result);
        }