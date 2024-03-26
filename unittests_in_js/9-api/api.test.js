const chai = require('chai');
const request = require('request');
const expect = chai.expect;

describe('GET /cart/:id', () => {
  it('Should return payment methods for numeric id', (done) => {
    request.get('http://localhost:7865/cart/123', (err, res, body) => {
      expect(body).to.equal('Payment methods for cart 123');
      done();
    });
  });

  it('Should return 404 for non-numeric id', (done) => {
    request.get('http://localhost:7865/cart/abc', (err, res, body) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });
});
