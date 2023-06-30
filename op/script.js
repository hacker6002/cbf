function changeLabelStyle() {
  var emailInput = document.getElementById("emailInput");
  var emailLabel = document.getElementById("emailLabel");
  var passwordInput = document.getElementById("passwordInput");
  var passwordLabel = document.getElementById("passwordLabel");

  if (emailInput.value !== "") {
    emailLabel.classList.add("highlight");
    emailLabel.classList.remove("default1");
  } else {
    emailLabel.classList.remove("highlight");
    emailLabel.classList.add("default1");
  }

  if (passwordInput.value !== "") {
    passwordLabel.classList.add("highlight");
    passwordLabel.classList.remove("default1");
  } else {
    passwordLabel.classList.remove("highlight");
    passwordLabel.classList.add("default1");
  }
}
