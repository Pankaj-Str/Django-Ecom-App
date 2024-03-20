let menu=document.querySelector('#menu-bar');
let navbar=document.querySelector('.navbar');
let header = document.querySelector('.header-2');


menu.addEventListener('click', () =>{
    menu.classList.toggle('fa-times');
    navbar.classList.toggle('active');
});

window.onscroll = () =>{
    menu.classList.remove('fa-times');
    navbar.classList.remove('active');

    if(window.scrollY > 150){
        header.classList.add('active');
    }else{
        header.classList.remove('active');
    }

}

let countDate = new Date('DECEMBER 28,2023 00:00:00').getTime();

function CountDown(){

    let now = new Date().getTime();
    gap = countDate - now;

    let second = 1000;
    let minute = second * 60;
    let hour = minute * 60;
    let day = hour * 24;

    let d =Math.floor(gap / (day));
    let h =Math.floor((gap % (day)) / (hour));
    let m =Math.floor((gap % (hour)) / (minute));
    let s =Math.floor((gap % (minute)) / (second));

    document.getElementById('day').innerText = d;
    document.getElementById('hour').innerText = h;
    document.getElementById('minute').innerText = m;
    document.getElementById('second').innerText = s;
}


setInterval(function(){
    CountDown(); 
},1000)

// Cart functionality
document.addEventListener('DOMContentLoaded', function () {
    const addToCartButtons = document.querySelectorAll('.box .btn');

    addToCartButtons.forEach(function (button) {
        button.addEventListener('click', addToCart);
    });

    const cartPopover = document.getElementById('cart-popover');
    const cartItemsList = document.getElementById('cart-items');

    function addToCart(event) {
        const productBox = event.target.closest('.box');
        const productName = productBox.querySelector('h3').innerText;
        const productPrice = productBox.querySelector('.price span').innerText;
        const productQuantity = productBox.querySelector('.quantity input').value;

        // Add item to cart popover
        const cartItem = document.createElement('li');
        cartItem.innerHTML = `${productName} - ${productQuantity} x ${productPrice}`;
        cartItemsList.appendChild(cartItem);

        // Show the cart popover
        cartPopover.style.display = 'block';

        // Close the popover when clicking outside of it
        window.addEventListener('click', function (event) {
            if (event.target === cartPopover) {
                closePopover();
            }
        });
    }

    function closePopover() {
        cartPopover.style.display = 'none';
    }
});



        // Assuming you have a variable 'cartItemCount' representing the number of items in the cart
        var cartItemCount = {{ cart_count|default:0 }}; // Use the cart_count from your Django context
        // Update the cart counter content
        document.getElementById('cartCounter').textContent = cartItemCount;
        
        document.addEventListener("DOMContentLoaded", function () {
            // Initialize cart array to store added items
            const cart = [];

            // Function to update the cart display
            function updateCartDisplay() {
                const cartItemsContainer = document.querySelector('.listcart');
                cartItemsContainer.innerHTML = ''; // Clear previous content

                // Display each item in the cart
                cart.forEach(function (item) {
                    const cartItem = document.createElement('div');
                    cartItem.classList.add('cart-item');
                    cartItem.innerHTML = `
                        <p>${item.name} - ${item.quantity} ${item.unit}</p>
                    `;
                    cartItemsContainer.appendChild(cartItem);
                });
            }

            // Add event listener to all "Add to Cart" buttons
            const addToCartButtons = document.querySelectorAll('.box .btn');
            addToCartButtons.forEach(function (button) {
                button.addEventListener('click', function (event) {
                    event.preventDefault();

                    // Get product details
                    const productBox = event.target.closest('.box');
                    const productName = productBox.querySelector('h3').innerText;
                    const productPrice = parseFloat(productBox.querySelector('.price span').innerText.replace('Rs.', '').trim());
                    const productQuantity = parseInt(productBox.querySelector('.quantity input').value);
                    const productUnit = productBox.querySelector('.quantity span').innerText;

                    // Check if the item is already in the cart
                    const existingItem = cart.find(item => item.name === productName);
                    if (existingItem) {
                        // Update quantity if the item is already in the cart
                        existingItem.quantity += productQuantity;
                    } else {
                        // Create a new item object and add it to the cart array
                        const newItem = {
                            name: productName,
                            price: productPrice,
                            quantity: productQuantity,
                            unit: productUnit,
                        };
                        cart.push(newItem);
                    }

                    // Update the cart display
                    updateCartDisplay();
                });
            });

            // Add event listener to the "CLOSE" button in the cart tab
            document.querySelector('.cartTab .close').addEventListener('click', function () {
                document.querySelector('.cartTab').classList.remove('active');
            });

            // Add event listener to the "CHECKOUT" button in the cart tab
            document.querySelector('.cartTab .checkout').addEventListener('click', function () {
                // Add your checkout logic here
                alert('Redirecting to checkout page...');
            });

            // Function to open the cart tab
            function openCartTab() {
                document.querySelector('.cartTab').classList.add('active');
            }

            // Function to close the cart tab
            function closeCartTab() {
                document.querySelector('.cartTab').classList.remove('active');
            }

            // Add event listener to the cart icon to toggle the cart tab
            document.querySelector('.icons .fa-shopping-cart').addEventListener('click', function () {
                if (document.querySelector('.cartTab').classList.contains('active')) {
                    closeCartTab();
                } else {
                    openCartTab();
                }
            });
        });
    
