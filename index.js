const express = require('express')
const {spawn} = require('child_process');
const app = express()
const port = 3000
const bodyparser = require('body-parser')
const mysql = require('mysql')

// Configure MySQL connection
var mysql_connection = mysql.createConnection({
	host: 'localhost',
	user: 'luxpm',
	password: "luxpm",
	database: "sukhija"
});
mysql_connection.connect(function(err){
	if (err) throw err;
	else {
		console.log("Connection Established");
	}
});

// App
app.use(bodyparser.json())
app.get('/', (req, res) => {
	var result = [];

 // spawn new child process to call the python script
 const pyscript = spawn('python', ['pyscript.py']);
 // collect data from script
 pyscript.stdout.on('data', function (data) {
  console.log('Pipe data from python script 2...');
	result.push(data)
	result = JSON.parse(result.join(""))
	// Inserting into table one-by-one
	for( var idx = 0; idx < result.length; idx++){
		mysql_connection.query('INSERT INTO LettersAndNumbers (letter, number) VALUES (?,?)',
		 [result[idx].letter.toString(), result[idx].number],
		 function(err, data) {
			 if(err) throw err;
		 });
	}
 });

 // in close event we are sure that stream from child process is closed
 pyscript.on('close', (code) => {
	 console.log(`child process 2 close all stdio with code ${code}`);
	 res.send("Node Script Executed")

 });
});

app.listen(port, () => console.log(`Sever listening on port ${port}!`))
