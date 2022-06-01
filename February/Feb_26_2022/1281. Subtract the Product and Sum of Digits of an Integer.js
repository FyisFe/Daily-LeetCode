/**
 * @param {number} n
 * @return {number}
 */
var subtractProductAndSum = function (n) {
  const arr = n.toString().split('');
  const product = arr.reduce((acc, curr) => acc * curr);
  const sum = arr.reduce((acc, curr) => Number(acc) + Number(curr));
  return product - sum;
};
