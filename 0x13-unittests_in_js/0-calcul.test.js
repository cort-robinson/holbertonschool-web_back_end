const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', function() {
  it('Returns 4 when adding 1 and 3', function() {
    assert.equal(calculateNumber(1, 3), 4);
  });
});
