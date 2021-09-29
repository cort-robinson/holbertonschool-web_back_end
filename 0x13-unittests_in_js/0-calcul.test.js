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
  it('Returns 0 when adding -0.4 and -0.4', function () {
    assert.equal(calculateNumber(-0.4, -0.4), 0);
  });
    it('Returns 0 when adding -0.4 and -0.2', function () {
    assert.equal(calculateNumber(-0.4, -0.2), 0);
  });
  it('Returns 0 when adding -0.2 and -0.4', function () {
    assert.equal(calculateNumber(-0.2, -0.4), 0);
  });
  it('Returns 0 when adding 0 and 0', function () {
    assert.equal(calculateNumber(0, 0), 0);
  });
  it('Returns -2 when adding -0.6 and -0.8', function () {
    assert.equal(calculateNumber(-0.6, -0.8), -2);
  })
  it('Returns -1 when adding -0.8 and -0.5', function () {
    assert.equal(calculateNumber(-0.8, -0.5), -1);
  })
});
