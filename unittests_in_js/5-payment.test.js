const sinon = require('sinon');
const sendPaymentRequestToApi = require('./5-payment');

describe("sendPaymentRequestToApi with hooks", function() {
  let spyConsole;

  beforeEach(() => {
    spyConsole = sinon.spy(console, 'log');
  });

  afterEach(() => {
    spyConsole.restore();
  });

  it('Should log the correct output', function() {
    sendPaymentRequestToApi(100, 20);
    sinon.assert.calledWith(spyConsole, 'The total is: 120');
  });
});
