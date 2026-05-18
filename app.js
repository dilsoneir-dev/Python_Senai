<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta http-equiv="X-UA-Compatible" content="ie=edge" />
  <title>Meu primeiro formulário</title>

  <style>
    .btn {
      padding: 16px 32px;
      border: 0;
      background: #25a30e;
      color: #fff;
      cursor: pointer;
      border-radius: 8px;
    }

    input {
      padding: 16px;
      border-radius: 8px;
    }
  </style>
</head>
<body>
  <form>
    <input id="nome" type="text" placeholder="Seu Nome" />
    <input id="email" type="email" placeholder="Seu E-mail" required />
    <input id="senha" type="password" placeholder="Sua Senha" />

    <button class="btn">Salvar</button>
  </form>

  <script>
    const formElement = document.querySelector("form");

    // campos de entrada
    const inputNome = document.querySelector("#nome");
    const inputEmail = document.querySelector("#email");
    const inputSenha = document.querySelector("#senha");
  </script>
</body>
</html>