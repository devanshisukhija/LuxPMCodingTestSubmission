# LuxPMCodingTestSubmission

Hello,

My name is Devanshi Sukhija. I am a Computer Vision and Deep Learning enthusiast. I am currently working as a Machine Learning Intern at an established start-up in India, where I engineer software devops for computer vision problem.

This repo contains my attempt at solving the Coding Test from Mr. Young, software director at LUX PM. Refer to following to understand repo/code structure:

* **pyfunction.py** : Consists of two python functions,
  * one generates list of odd numbers from zero, and
  * other inserts digits in between letters of a word.
* **Node APP**
  * **pyscript.py** : reads and prints the _letter_number.json_ file.  
  * **index.js** : is a basic _express.js_ server application that spawns child process to interact with the python script (_pyscript.py_) and _mysql_ server. Execute `<node index.js>` to start the server.

For node script _index.js_ to interact with mysql, a user 'luxpm' must be created:

`<CREATE USER 'luxpm'@'localhost' IDENTIFIED WITH mysql_native_password BY 'luxpm';>`

`<GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT on sukhija.LettersAndNumbers TO 'luxpm'@'localhost' WITH GRANT OPTION;>`

To call node script _index.js_ via Postman, send a **GET** request to http://localhost:3000 with dummy test, copy and paste example for _Pre-request script_ and _Tests_ from **postman_contract_test.txt**








