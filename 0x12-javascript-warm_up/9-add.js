#!/usr/bin/node
if (isNaN(process.argv[2]) || isNaN(process.argv[3])) {
  console.log(NaN);
} else {
  console.log(process.argv[2] + process.argv[3]);
}
