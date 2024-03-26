const chai = require('chai');
const request = require('request');
const expect = chai.expect;

describe('GET /cart/:id', () => {
  it("should return correct status code", (done) => {
    request("http://localhost:7865", (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it("should return correct result", (done) => {
    request("http://localhost:7865", (error, response, body) => {
      expect(body).to.equal("Welcome to the payment system");
      done();
    });
  });

  it('Should return payment methods for numeric id', (done) => {
    request.get('http://localhost:7865/cart/123', (err, res, body) => {
      expect(res.statusCode).to.equal(200);
      expect(body).to.equal('Payment methods for cart 123');
      done();
    });
  });

  it('Should return 404 for non-numeric id', (done) => {
    request.get('http://localhost:7865/cart/abc', (err, res, body) => {
      expect(res.statusCode).to.equal(404);
      done();
    });
  });
});
