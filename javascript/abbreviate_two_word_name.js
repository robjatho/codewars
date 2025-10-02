// #Task
// Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
//
// The output should be two capital letters with a dot separating them.
//
// It should look like this:
//
// Sam Harris => S.H
//
// patrick feeney => P.F
//
// #Test
// const chai = require("chai");
// const assert = chai.assert;
// chai.config.truncateThreshold=0;
//
// describe("Basic tests", () => {
//   it("Testing for fixed tests", () => {
//     assert.strictEqual(abbrevName("Sam Harris"), "S.H");
//     assert.strictEqual(abbrevName("Patrick Feenan"), "P.F");
//     assert.strictEqual(abbrevName("Evan Cole"), "E.C");
//     assert.strictEqual(abbrevName("P Favuzzi"), "P.F");
//     assert.strictEqual(abbrevName("David Mendieta"), "D.M");
//   });
// });
//
//
// #Solution
// function abbrevName(name){
//
//     return name.split(' ').map(i => i[0].toUpperCase()).join('.')
//
// }

function abbrevName(name){
  const arr = name.split(" ");
  let initials = '';

  for (let i = 0; i<arr.length;i++){
    initials += arr[i][0].toUpperCase();
    if (i < arr.length-1) {
      initials += "."
    }
  }
  return initials
}