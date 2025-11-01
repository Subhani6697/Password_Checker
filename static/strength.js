const passwordInput = document.getElementById('password');
const strengthBar = document.getElementById('strength-bar');
const strengthText = document.getElementById('strength-text');

passwordInput.addEventListener('input', () => {
    const val = passwordInput.value;
    const score = calculateStrength(val);
    updateStrengthMeter(score);
});

function calculateStrength(password) {
    let score = 0;
    if (password.length >= 8) score++;
    if (/[A-Z]/.test(password)) score++;
    if (/[a-z]/.test(password)) score++;
    if (/[0-9]/.test(password)) score++;
    if (/[^A-Za-z0-9]/.test(password)) score++;
    return score;
}

function updateStrengthMeter(score) {
    const percent = (score / 5) * 100;
    strengthBar.style.width = percent + '%';

    let color = 'red';
    let text = 'Very Weak';

    switch (score) {
        case 1:
            color = 'orangered';
            text = 'Weak';
            break;
        case 2:
            color = 'orange';
            text = 'Moderate';
            break;
        case 3:
            color = 'gold';
            text = 'Fair';
            break;
        case 4:
            color = '#4caf50';
            text = 'Strong';
            break;
        case 5:
            color = '#2e7d32';
            text = 'Very Strong';
            break;
    }

    strengthBar.style.backgroundColor = color;
    strengthText.textContent = text;
}
