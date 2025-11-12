/* Saki-Doruma Landing Page - JavaScript Utilities */

/**
 * Authentication System (localStorage-based)
 */
const AUTH_KEY = 'saki_doruma_user';

/**
 * Initialize authentication on page load
 */
document.addEventListener('DOMContentLoaded', function() {
    checkAuthStatus();
    observeElements();
    setupFormHandlers();
});

/**
 * Check if user is logged in and update UI
 */
function checkAuthStatus() {
    const user = localStorage.getItem(AUTH_KEY);
    if (user) {
        const userData = JSON.parse(user);
        showUserProfile(userData);
    } else {
        showLoginButton();
    }
}

/**
 * Show login button and hide user profile
 */
function showLoginButton() {
    const authMenu = document.getElementById('auth-menu');
    const userMenu = document.getElementById('user-menu');
    if (authMenu) authMenu.style.display = 'block';
    if (userMenu) userMenu.style.display = 'none';
}

/**
 * Show user profile and hide login button
 */
function showUserProfile(userData) {
    const authMenu = document.getElementById('auth-menu');
    const userMenu = document.getElementById('user-menu');
    const userName = document.getElementById('user-name');
    
    if (authMenu) authMenu.style.display = 'none';
    if (userMenu) userMenu.style.display = 'block';
    if (userName) userName.textContent = userData.name || userData.email.split('@')[0];
}

/**
 * Open login modal
 */
function openLoginModal() {
    const modal = document.getElementById('login-modal');
    if (modal) {
        modal.classList.add('active');
    }
}

/**
 * Close login modal
 */
function closeLoginModal() {
    const modal = document.getElementById('login-modal');
    if (modal) {
        modal.classList.remove('active');
    }
}

/**
 * Handle login form submission
 */
function handleLogin(event) {
    event.preventDefault();
    
    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('password').value;
    const remember = document.getElementById('remember').checked;
    
    // Basic validation
    if (!email || !password) {
        showAlert('Please fill in all fields', 'error');
        return;
    }
    
    if (!validateEmail(email)) {
        showAlert('Please enter a valid email address', 'error');
        return;
    }
    
    if (password.length < 6) {
        showAlert('Password must be at least 6 characters', 'error');
        return;
    }
    
    // Simulate successful login
    const userData = {
        email: email,
        name: email.split('@')[0].charAt(0).toUpperCase() + email.split('@')[0].slice(1),
        loginTime: new Date().toISOString(),
        rememberMe: remember
    };
    
    // Store user in localStorage
    localStorage.setItem(AUTH_KEY, JSON.stringify(userData));
    
    // Update UI
    showUserProfile(userData);
    closeLoginModal();
    
    // Show success message
    showAlert(`Welcome, ${userData.name}!`, 'success');
    
    // Clear form
    document.getElementById('login-form').reset();
}

/**
 * Handle logout
 */
function logout() {
    if (confirm('Are you sure you want to log out?')) {
        localStorage.removeItem(AUTH_KEY);
        showLoginButton();
        showAlert('You have been logged out', 'info');
    }
}

/**
 * Scroll to section
 */
function scrollTo(elementId) {
    const element = document.getElementById(elementId);
    if (element) {
        element.scrollIntoView({ behavior: 'smooth' });
    }
}

/**
 * Observe elements for scroll animations
 */
function observeElements() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.animation = 'fadeInUp 0.6s ease-out forwards';
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1
    });

    document.querySelectorAll('.feature-card, .benefit-item, .pricing-card, .testimonial-card').forEach(el => {
        el.style.opacity = '0';
        observer.observe(el);
    });
}

/**
 * Setup form handlers and close modal on outside click
 */
function setupFormHandlers() {
    // Close modal when clicking outside
    const modal = document.getElementById('login-modal');
    if (modal) {
        window.addEventListener('click', (event) => {
            if (event.target === modal) {
                closeLoginModal();
            }
        });
    }
}

/**
 * Simple email validation
 */
function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

/**
 * Show alert message
 */
function showAlert(message, type = 'info') {
    let alertContainer = document.getElementById('alert-container');
    if (!alertContainer) {
        alertContainer = document.createElement('div');
        alertContainer.id = 'alert-container';
        alertContainer.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            z-index: 10000;
            max-width: 400px;
        `;
        document.body.appendChild(alertContainer);
    }
    
    const alert = document.createElement('div');
    alert.className = `alert alert-${type}`;
    alert.style.cssText = `
        padding: 1rem;
        margin-bottom: 0.5rem;
        border-radius: 8px;
        background: ${type === 'success' ? '#00cc66' : type === 'error' ? '#ff4444' : '#00ff99'};
        color: #000;
        font-weight: 500;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        animation: slideIn 0.3s ease-out;
    `;
    alert.textContent = message;
    
    alertContainer.appendChild(alert);
    
    setTimeout(() => {
        alert.style.animation = 'slideOut 0.3s ease-out';
        setTimeout(() => alert.remove(), 300);
    }, 4000);
}

/**
 * Add active state to nav links on scroll
 */
window.addEventListener('scroll', function() {
    const sections = document.querySelectorAll('section[id]');
    const scrollPosition = window.scrollY + 200;

    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;

        if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
            const navLinks = document.querySelectorAll('.nav-menu a');
            navLinks.forEach(link => link.classList.remove('active'));
            const activeLink = document.querySelector(`.nav-menu a[href="#${section.id}"]`);
            if (activeLink) {
                activeLink.classList.add('active');
            }
        }
    });
});

// Add active link styling and animations
const style = document.createElement('style');
style.textContent = `
    .nav-menu a.active {
        color: var(--primary-dark) !important;
        border-bottom: 2px solid var(--primary-dark);
        padding-bottom: 0.25rem;
    }
    
    #alert-container .alert {
        margin-bottom: 0.5rem;
    }
    
    @keyframes slideIn {
        from {
            transform: translateX(400px);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes slideOut {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(400px);
            opacity: 0;
        }
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
`;
document.head.appendChild(style);
