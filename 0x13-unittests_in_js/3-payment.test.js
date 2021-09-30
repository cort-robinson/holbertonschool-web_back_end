const expect = require('chai').expect;
const sinon = require('sinon');

const sendPaymentRequestToApi = require('./3-payment');
const Utils = require('./utils');


describe('sendPaymentRequestToApi', () => {
  it('Tests usage of Utils.calculateNumber()', () => {
    const calcSpy = sinon.spy(Utils, 'calculateNumber');
    sendPaymentRequestToApi(100, 7.85);

    expect(calcSpy.calledWith('SUM', 100, 7.85)).to.be.true;
    calcSpy.restore();
  });
});
