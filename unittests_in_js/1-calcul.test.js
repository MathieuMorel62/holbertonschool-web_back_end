const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber with type', function() {
  describe("Test for SUM", function() {
    it('Correctly returns the addition of 2 positive numbers', () => {
      assert.equal(calculateNumber('SUM', 1, 3), 4);
      assert.equal(calculateNumber('SUM', 5, 3), 8);
    })
    it('Correctly returns the addition of 1 positive number and 1 negative number', () => {
      assert.equal(calculateNumber('SUM', -5, 3), -2);
      assert.equal(calculateNumber('SUM', -1, 3), 2);
    })
    it('Correctly returns the addition of 2 negative numbers', () => {
      assert.equal(calculateNumber('SUM', -1, -3), -4);
      assert.equal(calculateNumber('SUM', -5, -3), -8);
    })
    it('Correctly returns an error for invalid input types', () => {
      assert.throws(() => calculateNumber("a", 2), Error);
      assert.throws(() => calculateNumber(2, "b"), Error);
    })
  });

  describe("Test for SUBTRACT", function() {
    it('Correctly returns subtract 2 numbers', () => {
      assert.equal(calculateNumber('SUBTRACT', 1, 3), -2);
      assert.equal(calculateNumber('SUBTRACT', 5, 3), 2);
    })
    it('Correctly returns an error for invalid input types', () => {
      assert.throws(() => calculateNumber("a", 2), Error);
      assert.throws(() => calculateNumber(2, "b"), Error);
    })
  });

  describe("Test for DIVIDE", function() {
    it('Correctly returns divide 2 numbers', () => {
      assert.equal(calculateNumber('DIVIDE', 4, 2), 2);
      assert.equal(calculateNumber('DIVIDE', 10, 5), 2);
    })
    it('Correctly return Error when dividing by 0', () => {
      assert.equal(calculateNumber('DIVIDE', 3, 0), 'Error');
    })
    it('Correctly returns an error for invalid input types', () => {
      assert.throws(() => calculateNumber("a", 2), Error);
      assert.throws(() => calculateNumber(2, "b"), Error);
    })
  });
});
