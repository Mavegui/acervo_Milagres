document.addEventListener('DOMContentLoaded', () => {
    const hamburgerBtn = document.getElementById('hamburger');
    const mobileMenu = document.getElementById('mobile-menu');
    const iconOpen = document.getElementById('icon-open');
    const iconClose = document.getElementById('icon-close');

    const toggleMenu = (forceClose = false) => {
        const isOpening = forceClose ? false : mobileMenu.classList.contains('hidden');
        
        if (isOpening) {
            mobileMenu.classList.remove('hidden');
            iconOpen.classList.add('opacity-0', 'scale-50');
            iconClose.classList.remove('opacity-0', 'scale-50');
            hamburgerBtn.setAttribute('aria-expanded', 'true');
            hamburgerBtn.setAttribute('aria-label', 'Fechar menu');
        } else {
            mobileMenu.classList.add('hidden');
            iconOpen.classList.remove('opacity-0', 'scale-50');
            iconClose.classList.add('opacity-0', 'scale-50');
            hamburgerBtn.setAttribute('aria-expanded', 'false');
            hamburgerBtn.setAttribute('aria-label', 'Abrir menu');
        }
    };

    if (hamburgerBtn && mobileMenu) {
        hamburgerBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            toggleMenu();
        });

        // Fechar ao clicar fora ou na tecla Esc
        document.addEventListener('click', (e) => {
            if (!mobileMenu.classList.contains('hidden') && !mobileMenu.contains(e.target)) {
                toggleMenu(true);
            }
        });

        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && !mobileMenu.classList.contains('hidden')) {
                toggleMenu(true);
            }
        });
    }

    // Reset ao redimensionar
    window.addEventListener('resize', () => {
        if (window.innerWidth >= 768 && !mobileMenu.classList.contains('hidden')) {
            toggleMenu(true);
        }
    });
});