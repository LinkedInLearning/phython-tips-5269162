// script.js
const args = process.argv.slice(2);
const result = eval(args[0]); // ⚠ eval nur mit vertrauenswürdigen Inputs
console.log(result);
