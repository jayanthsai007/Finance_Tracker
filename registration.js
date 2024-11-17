function validateRegistrationForm() {
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("retype-password").value;

    if (password !== confirmPassword) {
        alert("Passwords do not match!");
        return false;
    }
    return true;
}

// Attach the validation function to the form submission event
document.querySelector('form').addEventListener('submit', function(event) {
    if (!validateRegistrationForm()) {
        event.preventDefault(); // Prevent form submission if validation fails
    }
});
