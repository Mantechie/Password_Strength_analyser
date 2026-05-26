// =========================
// DOM Elements
// =========================

const passwordInput =
    document.getElementById("passwordInput");

const togglePassword =
    document.getElementById("togglePassword");

const strengthBar =
    document.getElementById("strengthBar");

const strengthText =
    document.getElementById("strengthText");

const feedbackList =
    document.getElementById("feedbackList");

const entropyValue =
    document.getElementById("entropyValue");

const crackTime =
    document.getElementById("crackTime");

const statusIndicator =
    document.getElementById("statusIndicator");

const generateBtn =
    document.getElementById("generateBtn");

const generatedPassword =
    document.getElementById("generatedPassword");

const passwordLength =
    document.getElementById("passwordLength");

const copyBtn =
    document.getElementById("copyBtn");


// =========================
// Debounce Timer
// =========================

let debounceTimer;


// =========================
// Toggle Password Visibility
// =========================

togglePassword.addEventListener("click", () => {

    if (passwordInput.type === "password") {

        passwordInput.type = "text";

        togglePassword.textContent = "Hide";

    } else {

        passwordInput.type = "password";

        togglePassword.textContent = "Show";
    }
});


// =========================
// Real-Time Password Analysis
// =========================

passwordInput.addEventListener("input", () => {

    const password = passwordInput.value;

    // Reset if empty
    if (password.length === 0) {

        resetUI();

        return;
    }

    // Show typing status
    statusIndicator.textContent =
        "Analyzing password...";

    // Clear previous debounce
    clearTimeout(debounceTimer);

    // Debounce request
    debounceTimer = setTimeout(() => {

        analyzePassword(password);

    }, 500);
});


// =========================
// Analyze Password API
// =========================

async function analyzePassword(password) {

    try {

        const response = await fetch("/analyze", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                password: password
            })
        });

        const data = await response.json();

        updateStrengthUI(data);

    } catch (error) {

        console.error(error);

        statusIndicator.textContent =
            "Analysis failed";
    }
}


// =========================
// Update UI
// =========================

function updateStrengthUI(data) {

    let width = "10%";

    let color = "#7f1d1d";

    // Strength Mapping
    switch (data.strength) {

        case "Very Weak":
            width = "10%";
            color = "#7f1d1d";
            break;

        case "Weak":
            width = "25%";
            color = "#dc2626";
            break;

        case "Moderate":
            width = "50%";
            color = "#ea580c";
            break;

        case "Strong":
            width = "75%";
            color = "#16a34a";
            break;

        case "Very Strong":
            width = "100%";
            color = "#15803d";
            break;
    }

    // Strength Bar
    strengthBar.style.width = width;

    strengthBar.style.background = color;

    // Strength Text
    strengthText.textContent = data.strength;

    // Entropy
    entropyValue.textContent = data.entropy;

    // Crack Time
    crackTime.textContent = data.crack_time;

    // Status Indicator
    if (
        data.strength === "Strong" ||
        data.strength === "Very Strong"
    ) {

        statusIndicator.textContent =
            "Password looks secure";

    } else {

        statusIndicator.textContent =
            "Password needs improvement";
    }

    // Clear Feedback
    feedbackList.innerHTML = "";

    // Render Feedback
    data.feedback.forEach(item => {

        const li = document.createElement("li");

        li.textContent = item;

        // Critical warnings
        if (
            item.includes("previously used") ||
            item.includes("extremely common")
        ) {

            li.classList.add(
                "critical-warning"
            );
        }

        feedbackList.appendChild(li);
    });
}


// =========================
// Reset UI
// =========================

function resetUI() {

    strengthBar.style.width = "0%";

    strengthText.textContent =
        "Password Strength";

    entropyValue.textContent = "0";

    crackTime.textContent =
        "Instantly";

    feedbackList.innerHTML = "";

    statusIndicator.textContent =
        "Waiting for input...";
}


// =========================
// Password Generator
// =========================

generateBtn.addEventListener("click", async () => {

    const length = passwordLength.value;

    try {

        const response = await fetch(
            `/generate-password?length=${length}`
        );

        const data = await response.json();

        generatedPassword.value =
            data.generated_password;

    } catch (error) {

        console.error(error);
    }
});


// =========================
// Copy Password
// =========================

copyBtn.addEventListener("click", async () => {

    const password =
        generatedPassword.value;

    if (!password) return;

    try {

        await navigator.clipboard.writeText(
            password
        );

        copyBtn.textContent = "Copied!";

        setTimeout(() => {

            copyBtn.textContent = "Copy";

        }, 2000);

    } catch (error) {

        console.error(error);
    }
});