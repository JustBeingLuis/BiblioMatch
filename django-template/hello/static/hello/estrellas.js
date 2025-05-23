document.addEventListener('DOMContentLoaded', function() {
    const stars = document.querySelectorAll('.star-rating .star');
    const input = document.getElementById('id_calificacion');
    let currentRating = parseInt(input.value) || 0;

    function setStars(rating) {
        stars.forEach((star, idx) => {
            if (idx < rating) {
                star.classList.add('filled');
            } else {
                star.classList.remove('filled');
            }
        });
    }

    stars.forEach((star, idx) => {
        star.addEventListener('mouseenter', () => setStars(idx + 1));
        star.addEventListener('mouseleave', () => setStars(currentRating));
        star.addEventListener('click', () => {
            currentRating = idx + 1;
            input.value = currentRating;
            setStars(currentRating);
        });
    });

    // Inicializa las estrellas si ya hay valor
    setStars(currentRating);
});