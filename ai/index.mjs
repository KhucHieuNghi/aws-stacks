import fs from "fs";
import fetch from "node-fetch";
import express from "express";
import { fileURLToPath } from "url";
import { dirname } from "path";
import bodyParser from "body-parser";
import cors from "cors";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const app = express();
const port = 3000;

app.use(cors());

app.use("/mp3", express.static(__dirname + "/mp3"));

// parse application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: false }));

// parse application/json
app.use(bodyParser.json());

app.post("/mp3", async (req, res) => {
  const body = req.body;

  const url = "https://api.play.ht/api/v2/tts/stream";
  const options = {
    method: "POST",
    headers: {
      accept: "audio/mpeg",
      "content-type": "application/json",
      AUTHORIZATION: "99a1094ae424490780e837ced9d23adf",
      "X-USER-ID": "RoXtfF4aeme6PbGv07ghs4CDgF72",
    },
    body: JSON.stringify({
      voice_engine: "PlayHT2.0-turbo",
      text:
        body.text ||
        "Hello I'm from Quokka team. This is a test product for the text to speech feature. Let's wait and see what our product brings to you",
      voice:
        "s3://voice-cloning-zero-shot/d9ff78ba-d016-47f6-b0ef-dd630f59414e/female-cs/manifest.json",
      output_format: "mp3",
      sample_rate: "44100",
      speed: 1,
    }),
  };

  const response = await fetch(url, options);
  const readableStream = response.body;

  const generateId = new Date().valueOf();

  // Pipe the readable stream to a writable stream, this can be a local file or any other writable stream
  readableStream.pipe(
    fs.createWriteStream(`./mp3/${body.file || ''}_${generateId}.mp3`)
  );
  readableStream.on("finish", () => {
    res.json({
      ok: 1,
      file: `${generateId}.mp3`,
      message: `File is saved as ${generateId}.mp3`,
    });
  });
});

app.get("/", (req, res) => {
  fs.readdir(__dirname + "/mp3", (err, files) => {
    if (err) res.json({ok: 0});
    else {
      res.json({ok: 1, files: files.filter(file => file.endsWith('.mp3'))})
    }
  });
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});
