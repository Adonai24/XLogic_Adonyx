// ============================================
// 1.js — XLogic Adonay
// Toggle de categorías de videos
// ============================================

function toggleCategoria(id) {
    const contenido = document.getElementById(id);
    const flecha = document.getElementById('flecha-' + id);

    // Cerrar todas las demás
    const todas = document.querySelectorAll('.categoria-videos');
    const flechas = document.querySelectorAll('.flecha');

    todas.forEach(function(cat) {
        if (cat.id !== id) {
            cat.classList.remove('visible');
        }
    });

    flechas.forEach(function(f) {
        if (f.id !== 'flecha-' + id) {
            f.classList.remove('abierta');
        }
    });

    // Toggle la seleccionada
    contenido.classList.toggle('visible');
    flecha.classList.toggle('abierta');
}

// Animación suave al hacer scroll
document.addEventListener('DOMContentLoaded', function() {
    // Efecto fade-in al entrar elementos en viewport
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(function(entry) {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, { threshold: 0.1 });

    // Observar elementos con animación
    document.querySelectorAll('.habilidad-item, .video-categoria, .dato-item').forEach(function(el) {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
        observer.observe(el);
    });
});

function reproducirVideo(url, titulo){

let videoID = "";

if(url.includes("watch?v=")){
    videoID = url.split("v=")[1];
}
else if(url.includes("youtu.be/")){
    videoID = url.split("youtu.be/")[1];
}

let embed = "https://www.youtube.com/embed/" + videoID;

document.getElementById("youtubePlayer").src = embed;

document.getElementById("tituloPrincipal").innerHTML = titulo;

window.scrollTo({
top:200,
behavior:'smooth'
});

}