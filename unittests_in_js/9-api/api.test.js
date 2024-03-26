const chai = require("chai");
const request = require("request");
const expect = chai.expect;

describe("GET /cart/:id", () => {
  it("Should return payment methods for numeric id", (done) => {
    chai.request(app)
    .get('/cart/123')
    .end((err, res) => {
      res.should.have.status(200);
      res.text.should.equal('Payment methods for cart 123');
      done();
    });
  });

  it("Should return 404 for non-numeric id", (done) => {
    chai.request(app)
    .get('/cart/abc')
    .end((err, res) => {
      res.should.have.status(404);
      done();
    });
  });
});
