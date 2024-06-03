function buggyFunction(inputArray) {
  /**
   * Bug: This function is intended to return the sum of the elements in the input array,
   * but there's a bug preventing it from working correctly.
   * 
   * @param {number[]} inputArray - An array of numbers.
   * @returns {number} - The sum of the numbers in the array.
   */

  // Bug: The bug is in the loop condition, which prevents the correct summation.
  let sum = 0;
  for (let i = 0; i < inputArray.length; i++) {
    sum += inputArray[i];
  }

  return sum;
}

console.log(buggyFunction([1, 2, 3, 4, 5])); // 15