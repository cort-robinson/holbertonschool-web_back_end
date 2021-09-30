const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber() with type \'SUM\'', function () {
  it('Returns 4 when adding 1 and 3', function () {
    assert.equal(calculateNumber('SUM', 1, 3), 4);
  });
  it('Returns 5 when adding 1 and 3.7', function () {
    assert.equal(calculateNumber('SUM', 1, 3.7), 5);
  });
  it('Returns 5 when adding 1.2 and 3.7', function () {
    assert.equal(calculateNumber('SUM', 1.2, 3.7), 5);
  });
  it('Returns 6 when adding 1.5 and 3.7', function () {
    assert.equal(calculateNumber('SUM', 1.5, 3.7), 6);
  });
  it('Returns 0 when adding -0.4 and -0.4', function () {
    assert.equal(calculateNumber('SUM', -0.4, -0.4), 0);
  });
  it('Returns 0 when adding -0.4 and -0.2', function () {
    assert.equal(calculateNumber('SUM', -0.4, -0.2), 0);
  });
  it('Returns 0 when adding -0.2 and -0.4', function () {
    assert.equal(calculateNumber('SUM', -0.2, -0.4), 0);
  });
  it('Returns 0 when adding 0 and 0', function () {
    assert.equal(calculateNumber('SUM', 0, 0), 0);
  });
  it('Returns -2 when adding -0.6 and -0.8', function () {
    assert.equal(calculateNumber('SUM', -0.6, -0.8), -2);
  });
  it('Returns -1 when adding -0.8 and -0.5', function () {
    assert.equal(calculateNumber('SUM', -0.8, -0.5), -1);
  });
});

describe('calculateNumber() with type \'SUBTRACT\'', function () {
  it('Returns 5 when subtracting 5 from 10', function () {
    assert.equal(calculateNumber('SUBTRACT', 10, 5), 5);
  });
  it('Returns 5 when subtracting 4.5 from 10', function () {
    assert.equal(calculateNumber('SUBTRACT', 10, 4.5), 5);
  });
  it('Returns 5 when subtracting 4.5 from 10.3', function () {
    assert.equal(calculateNumber('SUBTRACT', 10.3, 4.5), 5);
  });
  it('Returns 4 when subtracting 3 from 1', function () {
    assert.equal(calculateNumber('SUBTRACT', 1, 3), -2);
  });
  it('Returns 5 when subtracting 3.7 from 1', function () {
    assert.equal(calculateNumber('SUBTRACT', 1, 3.7), -3);
  });
  it('Returns 5 when subtracting 3.7 from 1.2', function () {
    assert.equal(calculateNumber('SUBTRACT', 1.2, 3.7), -3);
  });
  it('Returns 6 when subtracting 3.7 from 1.5', function () {
    assert.equal(calculateNumber('SUBTRACT', 1.5, 3.7), -2);
  });
  it('Returns 0 when subtracting -0.4 from -0.4', function () {
    assert.equal(calculateNumber('SUBTRACT', -0.4, -0.4), 0);
  });
  it('Returns 0 when subtracting -0.2 from -0.4', function () {
    assert.equal(calculateNumber('SUBTRACT', -0.4, -0.2), 0);
  });
  it('Returns 0 when subtracting -0.4 from -0.2', function () {
    assert.equal(calculateNumber('SUBTRACT', -0.2, -0.4), 0);
  });
  it('Returns 0 when subtracting 0 from 0', function () {
    assert.equal(calculateNumber('SUBTRACT', 0, 0), 0);
  });
  it('Returns -2 when subtracting -0.8 from -0.6', function () {
    assert.equal(calculateNumber('SUBTRACT', -0.6, -0.8), 0);
  });
  it('Returns -1 when subtracting -0.5 from -0.8', function () {
    assert.equal(calculateNumber('SUBTRACT', -0.8, -0.5), -1);
  });
});

describe('calculateNumber() with type \'DIVIDE\'', function () {
  it('Returns 1 when dividing 1 and 1', function () {
    assert.equal(calculateNumber('DIVIDE', 1, 1), 1);
  });
  it('Returns 0.25 when dividing 1 and 3.7', function () {
    assert.equal(calculateNumber('DIVIDE', 1, 3.7), 0.25);
  });
  it('Returns 0.25 when dividing 1.2 and 3.7', function () {
    assert.equal(calculateNumber('DIVIDE', 1.2, 3.7), 0.25);
  });
  it('Returns 0.5 when dividing 1.5 and 3.7', function () {
    assert.equal(calculateNumber('DIVIDE', 1.5, 3.7), 0.5);
  });
  it('Returns "Error" when dividing -0.4 and -0.4', function () {
    assert.equal(calculateNumber('DIVIDE', -0.4, -0.4), 'Error');
  });
    it('Returns "Error" when dividing -0.4 and -0.2', function () {
    assert.equal(calculateNumber('DIVIDE', -0.4, -0.2), 'Error');
  });
  it('Returns "Error" when dividing -0.2 and -0.4', function () {
    assert.equal(calculateNumber('DIVIDE', -0.2, -0.4), 'Error');
  });
  it('Returns "Error" when dividing 0 and 0', function () {
    assert.equal(calculateNumber('DIVIDE', 0, 0), 'Error');
  });
  it('Returns 1 when dividing -0.6 and -0.8', function () {
    assert.equal(calculateNumber('DIVIDE', -0.6, -0.8), 1);
  })
  it('Returns "Error" when dividing -0.8 and -0.5', function () {
    assert.equal(calculateNumber('DIVIDE', -0.8, -0.5), 'Error');
  })
});
