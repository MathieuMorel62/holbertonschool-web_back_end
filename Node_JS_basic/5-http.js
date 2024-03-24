const http = require("http");
const countStudents = require("./3-read_file_async");

const hostname = "127.0.0.1";
const port = 1245;

const app = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader("Content-Type", "text/plain");

  if (req.url === "/") {
    res.end("Hello Holberton School!");
  } else if (req.url === "/students") {
    let info_message = 'This is the list of our students\n';
    countStudents(process.argv[2])
      .then((msg) => {
        info_message += msg;
        res.end(info_message);
      })
      .catch((error) => {
        info_message += error.message;
        res.end(info_message);
      });
    }
});

app.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});

module.exports = app;
