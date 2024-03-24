const http = require("http");
const countStudents = require("./3-read_file_async");

const hostname = "127.0.0.1";
const port = 1245;

const app = http.createServer(async (req, res) => {
  if (req.url === "/") {
    res.statusCode = 200;
    res.setHeader("Content-Type", "text/plain");
    res.end("Hello Holberton School!");
  } else if (req.url === "/students") {
    try {
      const data = await countStudents(process.argv[2]);
      res.statusCode = 200;
      res.setHeader("Content-Type", "text/plain");
      res.end(`This is the list of our students\n${data}`);
    } catch (error) {
      res.statusCode = 500;
      res.end(`This is the list of our students\n${error.message}`);
    }
  }
});

app.listen(port, hostname);

module.exports = app;
