#!usr/bin/node
if (isNaN(process.argv[3]) || process.argv[3] === undefined) {
  console.log(0);
} else {
  let arr = process.argv.slice(2);
  let second = arr.sort( function (a, b) { b - a; })[1];
  console.log(second);
}
