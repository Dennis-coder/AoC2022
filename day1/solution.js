const fs = require('fs');

let data;

try {
    data = fs.readFileSync('indata.txt', 'utf8');
  } catch (err) {
    console.error(err);
}

let elfs = data.split("\n\n").map((elf) => elf.split("\n").map((cal) =>  parseInt(cal)).reduce((a,b) => a+b, 0)).sort((a,b) => a-b).reverse()

// Part 1
console.log(elfs[0])

// Part 2
console.log(elfs[0] + elfs[1] + elfs[2])