* URL : `/signup`
* Méthodes : GET, POST
* Nom du template : signup.html
* Variables de templates : Aucune
* Redirection : en POST vers `/`


* URL : `/login`
* Méthodes : GET, POST
* Nom du template : login.html
* Variables de templates : Aucune
* Redirection : en POST vers `/`


* URL : `/logout`
* Méthodes : GET
* Nom du template : Aucun
* Variables de templates : Aucune
* Redirection : vers `/`


* URL : `/`
* Méthodes : GET
* Nom du template : homepage.html
* Variables de templates :
  * `users` : la liste des utilisateurs ayant un compte
  * `latest_posts` : les 3 derniers posts,
  * `scored_posts` : les 3 posts les mieux notés,
  * `commented_posts` : les 3 posts les plus commentés
* Redirection : Aucune

* URL : /posts
* Méthodes : GET
* Nom du template : post_listing.html
* Variables de templates :
  * `posts` : tous les posts
* Redirection : Aucune


* URL : `/post/<slug>`
* Méthodes : GET
* Nom du template : post_display.html
* Variables de templates :
  * `post` : le post correspondant au paramètre `<slug>`
* Redirection : Aucune

* URL : `/add/post`
* Méthodes : GET, POST
* Nom du template : add_post_form.html
* Variables de templates : Aucune
* Redirection : en POST vers `/posts`
