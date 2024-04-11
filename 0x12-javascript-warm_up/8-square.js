#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  let i = 0;
  const num = Number(process.argv[2]);
  while (i < num)){
    console.log('X'.repeat(num));
    i++;
  }
}
