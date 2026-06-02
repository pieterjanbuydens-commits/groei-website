// Scholengemeenschap Groei — kleine interacties

// Navbar krijgt achtergrond + schaduw zodra je scrollt
(function () {
  const nav = document.querySelector('nav.site-nav');
  if (!nav) return;
  const onScroll = () => {
    if (window.scrollY > 20) {
      nav.classList.add('bg-white/90', 'shadow-md');
      nav.classList.remove('bg-transparent');
    } else {
      nav.classList.add('bg-transparent');
      nav.classList.remove('bg-white/90', 'shadow-md');
    }
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
})();

// Mobiel menu open/dicht
(function () {
  const btn = document.getElementById('menu-toggle');
  const menu = document.getElementById('mobile-menu');
  if (!btn || !menu) return;
  btn.addEventListener('click', () => {
    const open = menu.classList.toggle('hidden');
    btn.setAttribute('aria-expanded', String(!open));
  });
  // Sluit bij klik op een link
  menu.querySelectorAll('a').forEach((a) =>
    a.addEventListener('click', () => menu.classList.add('hidden'))
  );
})();
