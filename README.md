* Projeto de request e response com flask

* api de cotaçao
* login com autentificaçao jwt
* token com tempo de  expiraçao
* organizaçao com   blueprint
* 

usage in postman

* via GET
* 1) gerar um access-token para o usuario no endpoint:localhost/api/v1/authentication/token/ passando no body:  {"username": "", "password": ""}

* 2) usar o authorization Bearer token e colocar o access-token gerado com o usuario  cadastrado. exemplo de endpoint: localhost/api/v1/genres .Use o method POST para o request. OBS:authorizations para usuario normal=> GET,HEAD,OPTIONS

* 3) para gerar um novo access-token => acesse rota /api/authentication/token/refresh/ passando no body: {"refresh": "<your refresh token>"}

* via POST
* 4) para requests: POST,PUT,PATCH,DELETE fazer o mesmo processo , mas com um usuario admin.