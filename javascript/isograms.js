// An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.
//
// Example: (Input --> Output)
//
// "Dermatoglyphics" --> true
// "aba" --> false
// "moOse" --> false (ignore letter case)
//
// Start;
// function isIsogram(str){
//   //...
// }
//
// Testing;
// const { assert, config } = require("chai");
// config.truncateThreshold = 0;
//
// describe("isIsogram", function() {
//   it("Sample tests", function() {
//     tester("Dermatoglyphics", true );
//     tester("isogram", true );
//     tester("aba", false);
//     tester("moOse", false);
//     tester("isIsogram", false );
//     tester("", true);
//   });
//   const tester = (input, expected) => {
//     assert.strictEqual(isIsogram(input), expected, `Failed for input: "${input}"\n`);
//   }
//
//
//   Solution
// function isIsogram(str){
// 	return new Set(str.toUpperCase()).size == str.length;
// }


function isIsogram(str){
    if(str.length === 0) {
        return true;
    }
    else {
        let arr = str.toLowerCase().split('');
        let result = {};
        for (let i = 0; i<arr.length;i++) {
            result[arr[i]] = (result[arr[i]] || 0) + 1;
            if (result[arr[i]] > 1) {
                return false;
            }
        }
        return true;
    }
}