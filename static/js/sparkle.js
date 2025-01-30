document.addEventListener("DOMContentLoaded", function() {
    // Select all text elements automatically
    const textElements = document.querySelectorAll("h1, h2, h3, h4, h5, h6, p, span, a");

    textElements.forEach(element => {
        element.classList.add("sparkle-container"); // Add the class dynamically

        element.addEventListener("mouseenter", function(event) {
            for (let i = 0; i < 10; i++) { // Generate multiple sparkles
                createSparkle(event, element);
            }
        });
    });

    function createSparkle(event, element) {
        const sparkle = document.createElement("div");
        sparkle.classList.add("sparkle");

        const rect = element.getBoundingClientRect();
        const x = Math.random() * rect.width;
        const y = Math.random() * rect.height;

        sparkle.style.left = `${x}px`;
        sparkle.style.top = `${y}px`;

        element.appendChild(sparkle);

        setTimeout(() => {
            sparkle.remove();
        }, 500);
    }
});
