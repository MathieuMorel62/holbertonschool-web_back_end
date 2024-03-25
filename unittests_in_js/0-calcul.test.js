const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', function() {
  it('Rounds 1 and 3 to 4', () => {
    assert.strictEqual(calculateNumber(1, 3), 4);
  }),
  it('Rounds 1 and 3.7 to 5', () => {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  }),
  it('Rounds 1.2 and 3.7 to 5', () => {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
  }),
  it('Rounds 1.5 and 3.7 to 6', () => {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  })
});
