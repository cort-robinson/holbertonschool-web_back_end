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
  it('Returns NaN when adding NaN and NaN', function () {
    assert.equal(isNaN(calculateNumber(NaN, NaN)), true);
  });
  it('Returns NaN when adding 0 and NaN', function () {
    assert.equal(isNaN(calculateNumber(0, NaN)), true);
  });
  it('Returns NaN when adding NaN and 0', function () {
    assert.equal(isNaN(calculateNumber(NaN, 0)), true);
  });
  it('Returns NaN when adding 1 and NaN', function () {
    assert.equal(isNaN(calculateNumber(1, NaN)), true);
  });
  it('Returns NaN when adding NaN and 1', function () {
    assert.equal(isNaN(calculateNumber(NaN, 1)), true);
  });
  it('Returns NaN when adding Infinity and Infinity', function () {
    assert.equal(calculateNumber(Infinity, Infinity), Infinity);
  });
  it('Returns NaN when adding Infinity and 0', function () {
    assert.equal(calculateNumber(Infinity, 0), Infinity);
  });
  it('Returns NaN when adding 0 and Infinity', function () {
    assert.equal(calculateNumber(0, Infinity), Infinity);
  });
  it('Returns NaN when adding Infinity and 1', function () {
    assert.equal(calculateNumber(Infinity, 1), Infinity);
  });
});
