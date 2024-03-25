const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', function() {
  it('Test sum of integers', () => {
    assert.equal(calculateNumber(1, 3), 4);
  }),
  it('Test sum with floating point number', () => {
    assert.equal(calculateNumber(1, 3.7), 5);
  }),
  it('Test sum with two floating point numbers', () => {
    assert.equal(calculateNumber(1.2, 3.7), 5);
  }),
  it('Test sum of rounded numbers', () => {
    assert.equal(calculateNumber(1.5, 3.7), 6);
  }),
  it('Test sum of negative numbers', () => {
    assert.equal(calculateNumber(-1, -3), -4);
  }),
  it('Test with a non-numeric value', () => {
    assert.throws(() => calculateNumber("a", 2), Error);
    assert.throws(() => calculateNumber(2, "b"), Error);
  });
});
