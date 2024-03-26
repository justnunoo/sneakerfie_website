const wrapper = document.querySelector('.wrapper');
const loginLink = document.querySelector('.login-link');
const registerLink = document.querySelector('.register-link');

registerLink.addEventListener('click', ()=> {
    wrapper.classList.add('active');
})

loginLink.addEventListener('click', ()=> {
    wrapper.classList.remove('active');
})

function togglePassword(passwordId) {
    var passwordInput = document.getElementById(passwordId);
    var icon = passwordInput.previousElementSibling.querySelector('ion-icon');

    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        icon.setAttribute('name', 'lock-open');
    } else {
        passwordInput.type = "password";
        icon.setAttribute('name', 'lock-closed');
    }
}