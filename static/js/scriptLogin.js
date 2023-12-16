// const form = document.getElementById("form");
const form = document.querySelector(".form .sign-btn");
// console.log(form);
const username = document.getElementById("username");
const email = document.getElementById("email");
const password = document.getElementById("password");
const confirmation = document.getElementById("confirmation");

// Show input error message
function showError(input, message) {
  const formControl = input.parentElement;
  formControl.className = "form-control error";
  const small = formControl.querySelector("small");
  small.innerText = message;
}

// Show success outline
function showSuccess(input) {
  const formControl = input.parentElement;
  formControl.className = "form-control success";
}

// Check email is valid
var checkEmailVar;
function checkEmail(input) {
  const re =
    /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  if (re.test(input.value.trim())) {
    showSuccess(input);
    checkEmailVar = 1;
  } else {
    showError(input, "Email is not valid");
    checkEmailVar = 0;
  }
  return checkEmailVar;
}
var checkRequiredVar;
// Check required fields
function checkRequired(inputArr) {
  inputArr.forEach(function (input) {
    if (input.value.trim() === "") {
      showError(input, `${getFieldName(input)} is required`);
      checkRequiredVar = 0;
    } else {
      showSuccess(input);
      checkRequiredVar = 1;
    }
  });
  return checkRequiredVar;
}

// Check input length
var checkLengthVar;
function checkLength(input, min, max) {
  if (input.value.length < min) {
    showError(input, ` must be at least ${min} characters`);
    checkLengthVar = 0;
  } else if (input.value.length > max) {
    showError(
      input,
      `${getFieldName(input)} must be less than ${max} characters`
    );
    checkLengthVar = 0;
  } else {
    showSuccess(input);
    checkLengthVar = 1;
  }
  return checkLengthVar;
}

// Check passwords match
var checkPasswordsMatchVar;
function checkPasswordsMatch(input1, input2) {
  if (input1.value !== input2.value) {
    showError(input2, "Passwords do not match");
    checkPasswordsMatchVar = 0;
  } else {
    checkPasswordsMatchVar = 1;
  }
  return checkPasswordsMatchVar;
}

// Get fieldname
function getFieldName(input) {
  return input.id.charAt(0).toUpperCase() + input.id.slice(1);
}

// Event listeners
form.addEventListener("click", function (e) {
  checkRequiredVar = checkRequired([username, email, password, confirmation]);
  checkLengthVar = checkLength(username, 3, 15);
  checkLengthVar = checkLength(password, 6, 25);
  checkEmailVar = checkEmail(email);
  checkPasswordsMatchVar = checkPasswordsMatch(password, confirmation);

  if (
    checkRequiredVar == 0 ||
    checkLengthVar == 0 ||
    checkLengthVar == 0 ||
    checkEmailVar == 0 ||
    checkPasswordsMatchVar == 0
  ) {
    console.log("default prevented");
    e.preventDefault();
  }
});
