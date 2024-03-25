const sinon = require('sinon');
const expect = require('chai').expect;
const sendPaymentRequestToApi = require('./4-payment');
const Utils = require('./utils');

describe('sendPaymentRequestToApi', () => {
  it('Uses a stub for Utils.calculateNumber', () => {
    const stubCalculateNumber = sinon.stub(Utils, 'calculateNumber').returns(10);
    const spyConsole = sinon.spy(console, 'log');

    sendPaymentRequestToApi(100, 20);

    expect(stubCalculateNumber.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
    expect(spyConsole.calledWithExactly('The total is: 10')).to.be.true;

    stubCalculateNumber.restore();
    spyConsole.restore();
  });
});
