#!/usr/bin/node
function fact (n) {
  if (isNaN(n) || n === 0 || n === 1) {
    return 1;
  } else if (n < 0) {
    return 0;
  } else {
    return n * fact(n - 1);
  }
}
console.log(fact(Number(process.argv[2])));
