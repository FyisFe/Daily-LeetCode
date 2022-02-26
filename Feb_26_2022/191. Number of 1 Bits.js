/**
 * @param {number} n - a positive integer
 * @return {number}
 */
var hammingWeight = function (n) {
  return n
    .toString()
    .split('')
    .filter((n) => n == 1).length;
};
