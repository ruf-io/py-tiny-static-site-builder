<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>{{name}} | {{domain}}</title>
  <meta name="description" content="{{description}}">
  <meta name="author" content="{{author}}">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" type="image/png" href="/img/favicon.png">
  <link rel="canonical" href="https://{{domain}}/{{slug}}">
</head>
<body>
  {{#posts}}
    <section>
      <h3><a href="{{slug}}">{{name}}</a></h3>
      <p>{{description}}</p>
    </section>
  {{/posts}}
</body>
</html>
