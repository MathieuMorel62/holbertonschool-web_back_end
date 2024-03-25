const expect = require('chai').expect;
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber with Chai', function() {
  describe("Test for SUM", function() {
    it('Correctly returns the addition of 2 positive numbers', () => {
      expect(calculateNumber('SUM', 1, 3)).to.equal(4);
      expect(calculateNumber('SUM', 5, 3)).to.equal(8);
    });
    it('Correctly returns the addition of 1 positive number and 1 negative number', () => {
      expect(calculateNumber('SUM', -5, 3)).to.equal(-2);
      expect(calculateNumber('SUM', -1, 3)).to.equal(2);
    });
    it('Correctly returns the addition of 2 negative numbers', () => {
      expect(calculateNumber('SUM', -1, -3)).to.equal(-4);
      expect(calculateNumber('SUM', -5, -3)).to.equal(-8);
    });
    it('Correctly returns an error for invalid input types', () => {
      expect(() => calculateNumber('SUM', "a", 2)).to.throw(Error);
      expect(() => calculateNumber('SUM', 2, "b")).to.throw(Error);
    });
  });

  describe("Test for SUBTRACT", function() {
    it('Correctly returns the subtraction of 2 numbers', () => {
      expect(calculateNumber('SUBTRACT', 1, 3)).to.equal(-2);
      expect(calculateNumber('SUBTRACT', 5, 3)).to.equal(2);
    });
    it('Correctly returns an error for invalid input types', () => {
      expect(() => calculateNumber('SUBTRACT', "a", 2)).to.throw(Error);
      expect(() => calculateNumber('SUBTRACT', 2, "b")).to.throw(Error);
    });
  });

  describe("Test for DIVIDE", function() {
    it('Correctly returns the division of 2 numbers', () => {
      expect(calculateNumber('DIVIDE', 4, 2)).to.equal(2);
      expect(calculateNumber('DIVIDE', 10, 5)).to.equal(2);
    });
    it('Correctly returns "Error" when dividing by 0', () => {
      expect(calculateNumber('DIVIDE', 3, 0)).to.equal('Error');
    });
    it('Correctly returns an error for invalid input types', () => {
      expect(() => calculateNumber('DIVIDE', "a", 2)).to.throw(Error);
      expect(() => calculateNumber('DIVIDE', 2, "b")).to.throw(Error);
    });
  });
});
