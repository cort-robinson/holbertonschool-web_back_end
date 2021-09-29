const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', function () {
  it('Returns 4 when adding 1 and 3', function () {
    assert.equal(calculateNumber(1, 3), 4);
  });
  it('Returns 5 when adding 1 and 3.7', function () {
    assert.equal(calculateNumber(1, 3.7), 5);
  });
  it('Returns 5 when adding 1.2 and 3.7', function () {
    assert.equal(calculateNumber(1.2, 3.7), 5);
  });
  it('Returns 6 when adding 1.5 and 3.7', function () {
    assert.equal(calculateNumber(1.5, 3.7), 6);
  });
});
