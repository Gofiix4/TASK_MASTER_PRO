document.addEventListener("DOMContentLoaded", function() {
    const formulario = document.getElementById("signin_form");
    const botonEnviar = document.getElementById("iniciar");
  
    formulario.addEventListener("submit", function(event) {
      // Validar que los campos estén llenos
      const username = document.getElementById("username").value;
      const password = document.getElementById("password").value;
      // Puedes agregar más campos y validaciones según tus necesidades.
  
      if (username === "" || password === "") {
        alert("Por favor, llene todos los campos");
        event.preventDefault(); // Evita que el formulario se envíe
      }
    });
  });

  document.addEventListener("DOMContentLoaded", function() {
    const formulario = document.getElementById("signup_form");
    const botonEnviar = document.getElementById("registrar");
  
    formulario.addEventListener("submit", function(event) {
      // Validar que los campos estén llenos
      const first_name = document.getElementById("first_name").value;
      const last_name = document.getElementById("last_name").value;
      const email = document.getElementById("email").value;
      const username = document.getElementById("username").value;
      // Puedes agregar más campos y validaciones según tus necesidades.
  
      if (first_name === "" || last_name === "" || email === "" || username === "") {
        alert("Por favor, llene todos los campos");
        event.preventDefault(); // Evita que el formulario se envíe
      }
    });
  });
  