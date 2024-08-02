// document.addEventListener("DOMContentLoaded", () => {
//     const favoriteIcons = document.querySelectorAll(".favorite-icon");

//     favoriteIcons.forEach(icon => {
//         icon.addEventListener("click", () => {
//             if (icon.classList.contains("favorite-icon-active")) {
//                 icon.classList.remove("favorite-icon-active");
//             } else {
//                 icon.classList.add("favorite-icon-active");
//             }
//         });
//     });
// });

document.addEventListener("DOMContentLoaded", () => {
    // this is useed to add the animation feature to the page
    const elements = document.querySelectorAll(".animate-up");
    function checkIfInView(){
        elements.forEach(element =>{
        const rect = element.getBoundingClientRect();

        if (rect.top <= (window.innerHeight || document.documentElement.clientHeight) && rect.bottom >= 0){
            setTimeout(() => {
                element.classList.add('in-view');
            }, 100)
        }
    })
    };

    window.addEventListener("scroll", checkIfInView);

    checkIfInView();

    // this will toggle the favorite icon and allow users to add and reeove an item from their favorites
    const favoriteIcons = document.querySelectorAll(".favorite-icon");
    favoriteIcons.forEach(icon => {
        icon.addEventListener("click", () => {
            const productId = icon.dataset.productId; // Get the product ID from data attribute
            const url = `/toggle_favorite/${productId}/`;

            fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken') // Include CSRF token for security
                },
                body: JSON.stringify({ product_id: productId })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    if (data.action === 'added') {
                        icon.classList.add("favorite-icon-active");
                        console.log("added");
                        icon.style.color = "red";
                    } else if (data.action === 'removed') {
                        icon.classList.remove("favorite-icon-active");
                        console.log("removed");
                        icon.style.color = "#bfbfbf";
                    }
                } else {
                    console.error(data.error);
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    });

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});