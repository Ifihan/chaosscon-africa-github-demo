// Palindrome Check

function isPalindrome(str) {
    str = str.toLowerCase().replace(/[^a-zA-Z0-9]/g, "");
    const reverseStr = str.split("").reverse().join("");
    return str === reverseStr;
}

const input = prompt("Enter a string to check if it's a palindrome:");
const result = isPalindrome(input);
console.log(`Is "${input}" a palindrome? ${result}`);