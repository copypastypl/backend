## Copypasty.pl
Strona z pastami ( ͡° ͜ʖ ͡°)

### dokumentacja
#### użytkownicy
Autoryzacja odbywa się poprzez bearer token.

| metoda | endpoint | opis |
| ------------ | ------------ |------------ |
| POST | /users/create/ | Tworzy nowego użytkownika, wymagane pola to username, email, password |
| POST  | /users/token/  | Wymagane pola to username lub email i password. Zwraca bearer token oraz token do odświeżenia. Token dostępu jest ważny przez 1h, po odświeżeniu przez 24h. |
| POST  | /users/token/refresh/ | Odświeża token, wymagany jest bearer token. |
| GET | /users/profile/ | Zwraca informacje o użytkowniku na podstawie zawartego tokenu.

#### posty

| metoda | endpoint | opis |
| ------------ | ------------ |------------ |
| POST | /posts/ | Tworzy nowy post (paste), wymagana autoryzacja, wymagane pola to title, content, tags (oddzielone przecinkiem tagi) |
| GET  | /posts/ | Zwraca wszystkie posty, po 15 na request (zwraca też url do następnej strony z postami). Istnieje możliwość filtrowania postów dla nazwy lub id autora. Wtedy endpoint wygląda następująco: **/posts/?author__username=ivall**. W ten sposób otrzymamy posty tylko użytkownika o nazwie ivall. Zamiast username możemy też dać tam **id**. |
| GET  | /posts/**{id}**/| Zwraca post o konkretnym id. |
| DELETE | /posts/**{id}**/ | Usuwa post o konkretnym id, wymagana autoryzacja, a użytkownik musi być autorem. |
| PUT | /posts/**{id}**/ | Aktualizuje post o konkretnym id, wymagana autoryzacja, a użytkownik musi być autorem. |
| GET | /posts/tags/ | Zwraca listę tagów wraz z ich id oraz nazwą. |
| GET | /posts/**{id}**/comments/ | Zwraca komentarze. |
| GET | /posts/**{id}**/comments/**{id}**}/ | Zwraca komentarz o konkretnym id. |
| POST | /posts/**{id}**/comments/ | Tworzy komentarz, wymagane pola to content i post (id pasty, dla której jest komentarz). |
| DELETE | /posts/**{id}**/comments/**{ID}**/ | Usuwa komentarz. |
| POST | /posts/**{id}**/votes/ | Oddaje plusa lub minusa na post. W body w requescie musi byc { "choice": "downvote" } lub { "choice": "upvote" } |
