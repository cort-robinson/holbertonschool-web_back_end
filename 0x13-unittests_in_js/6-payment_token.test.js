const expect = require('chai').expect;
const sinon = require('sinon');

const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', () => {
  it('Tests result with true', (done) => {
    getPaymentTokenFromAPI(true)
      .then((result) => {
        expect(result).to.deep.equal({ data: 'Successful response from the API' });
      }).then(done, done);
  });
  it('Tests result with false', () => {
    expect(getPaymentTokenFromAPI(false)).to.be.undefined;
  });
});
