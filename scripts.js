const productos = [
    {
        codigo: 900001, 
        bodega: "Combo",
        cepa: "Blend",
        imagen: "./imagenes/duoCaroGarzon.jpg",
        nombre: "Duo Caro Balasto",
        anio: 2024,
        precio: 345800,
        precioConDesc: 294780,  
        precioCuota: 98260,
        }, 
    {
        codigo: 900002,
        bodega: "Combo",
        cepa: "Blend",
        imagen: "./imagenes/GarzonCopas.jpg",
        nombre: "Dou Single Vineyard",
        anio: 2024,
        precio: 91600,
        precioConDesc: 77860,
        precioCuota: 25954,
        },
    {
        codigo: 900003,
        bodega: "Combo",
        cepa: "Blend",
        imagen: "./imagenes/GrazonBlanco.jpg",
        nombre: "Trio De Blancos",
        anio: 2024,
        precio: 52800,
        precioConDesc: 44880,
        precioCuota: 14960,
        }
    ]



let combosPromo = "";
for(let indice = 0; indice < productos.length; indice++){
    combosPromo +=`
                <div class="card-promo">
                    <a href="">
                        <img src=${productos[indice].imagen}
                    </a>
                    <h3>${productos[indice].nombre}</h3>
                    <p><del>$ ${productos[indice].precio.toLocaleString('de-DE')}</del>   ♦  <strong>$ ${productos[indice].precioConDesc.toLocaleString('de-DE')}</strong></p>
                    <p><b>3</b> <small>cuotas sin interes de </small><b>$ ${productos[indice].precioCuota.toLocaleString('de-DE')}</b></p>
                    <div class="card-promo-miniatura">
                        <a href="#">
                        <input class="boton-agregar-carrito" 
                            type="image" 
                            title="Agregar al carrito" 
                            src="imagenes/cart-plus-solid.svg" 
                            alt="Imagen predeterminada">
                        </a>
                    </div>
                </div>
                `;
    }

    

const contenedorCursos = document.getElementById("combosContenedor");
contenedorCursos.innerHTML = combosPromo

const modalCarrito = document.getElementById("modal-carrito-compras");
const cerrarModalCarrito = document.getElementById("cerrar-modal-carrito");
const abrirModalCarrito = document.getElementById("abrir-modal-carrito");
const listaCarrito = document.getElementById("lista-carrito");
const totalCarrito = document.getElementById("total-carrito");
const mensajeCarrito = document.getElementById("mensaje-carrito");
const botonBorrar = document.getElementById("boton-borrar");
const botonPagar = document.getElementById("boton-pagar");
const botonSeguirComprando = document.getElementById("boton-seguir-comprando");
const indicadorCarrito = document.getElementById("indicador-carrito");


let carrito = {};
let totalAPagar = 0;

/*MODAL*/
abrirModalCarrito.addEventListener("click", (e) => {
    e.preventDefault();
    modalCarrito.style.display = "block";
});

cerrarModalCarrito.addEventListener("click", () => {
    modalCarrito.style.display = "none";
});
/*CIERRE MODAL*/

/* CARRITO */
function agregarAlCarrito(indice) {
    const producto = productos[indice];

    // Si el producto ya está en el carrito, incrementa la cantidad
    if (carrito[producto.codigo]) {
        carrito[producto.codigo].cantidad++;
    } else {
        carrito[producto.codigo] = { ...producto, cantidad: 1 };
    }

    actualizarCarrito();
    modalCarrito.style.display = "block"; // Mostrar el modal automáticamente
}

// ACTUALIZAR
function actualizarCarrito() {
    listaCarrito.innerHTML = "";
    totalAPagar = 0;

    Object.values(carrito).forEach((item) => {
        const li = document.createElement("li");
        li.innerHTML = `
            ${item.nombre} x${item.cantidad} - $ ${(item.precioConDesc * item.cantidad).toLocaleString("de-DE")}
            <button class="eliminar-item" data-codigo="${item.codigo}">Eliminar</button>
        `;
        listaCarrito.appendChild(li);
        totalAPagar += item.precioConDesc * item.cantidad;
    });

    totalCarrito.innerText = `Total a Pagar: $ ${totalAPagar.toLocaleString("de-DE")}`;
    actualizarIndicadorCarrito();
}

// ELIMINIAR ARITCULO
listaCarrito.addEventListener("click", (e) => {
    if (e.target.classList.contains("eliminar-item")) {
        const codigo = e.target.dataset.codigo;
        if (carrito[codigo].cantidad > 1) {
            carrito[codigo].cantidad--;
        } else {
            delete carrito[codigo];
        }
        actualizarCarrito();
    }
});

//VACIAR
botonBorrar.addEventListener("click", () => {
    carrito = {};
    actualizarCarrito();
    mensajeCarrito.innerText = "";
});

// PAGAR
botonPagar.addEventListener("click", () => {
    if (Object.keys(carrito).length === 0) {
        mensajeCarrito.innerText = "No has seleccionado artículos.";
    } else {
        window.location.href = "paginas/pagos.html";
    }
});

// SEGUIR
botonSeguirComprando.addEventListener("click", () => {
    modalCarrito.style.display = "none";
});

// INDICADOR
function actualizarIndicadorCarrito() {
    const totalItems = Object.values(carrito).reduce((acc, item) => acc + item.cantidad, 0);
    if (totalItems > 0) {
        indicadorCarrito.style.display = "block";
        indicadorCarrito.innerText = totalItems;
    } else {
        indicadorCarrito.style.display = "none";
    }
}


// SCROLL
document.querySelectorAll(".boton-agregar-carrito").forEach((boton, indice) => {
    boton.addEventListener("click", (e) => {
        e.preventDefault();
        agregarAlCarrito(indice);
    });
});


/*
const botonesAgregarCarrito = document.querySelectorAll('.boton-agregar-carrito');
const listaCarrito = document.querySelector("#carrito ul");
const totalCarrito = document.querySelector("#carrito p");
const mensajePagarCarrito = document.getElementById("mensaje-carrito")


let totalAPagar= 0;

for(let indice = 0; indice < botonesAgregarCarrito.length; indice++){
    
    function agregarElementoCarrito(){
        const elementoLi = document.createElement("li")
        elementoLi.innerText = `Combo ${productos[indice].nombre} $ ${productos[indice].precioConDesc.toLocaleString('de-DE')}`

        listaCarrito.appendChild(elementoLi);
        totalAPagar += productos[indice].precioConDesc;
        totalCarrito.innerText = "Total a Pagar: $ " + totalAPagar.toLocaleString('de-DE'); 
        mensajePagarCarrito.innerText = ""
    }
    
    botonesAgregarCarrito[indice].addEventListener("click", agregarElementoCarrito)
}


const botonBorrar = document.querySelector("#boton-borrar");
document.querySelectorAll(".boton-agregar-carrito").forEach((boton, indice) => {
    boton.addEventListener("click", (e) => {
        e.preventDefault();
        agregarAlCarrito(indice);
    });
});


function borrarCarrito(){
    listaCarrito.innerHTML = "";
    totalCarrito.innerHTML = "Total a Pagar: $ 0";
    totalAPagar = 0;
    mensajePagarCarrito.innerText = ""
}
botonBorrar.addEventListener("click", borrarCarrito);



const botonPagar = document.querySelector("#boton-pagar");


function pagarCarrito(){
    
    if(listaCarrito.innerText === ""){
    mensajePagarCarrito.innerText = "No has seleccionado articulos"
    } else{
        window.location.href = "paginas/pagos.html"
    }
}

botonPagar.addEventListener("click", pagarCarrito);

const indicadorCarrito = document.getElementById("indicador-carrito");


botonesAgregarCarrito.forEach(boton => {
    boton.addEventListener('mouseover', () => {
        boton.src = 'imagenes/shopping-cart-add.png';
    });

    boton.addEventListener('mouseout', () => {
        boton.src = 'imagenes/cart-plus-solid.svg';
    });

});


*/


/*MODAL ZORZAL*/

function abrirModal(src) {
    document.getElementById("modalImagen").style.display = "block";
    document.getElementById("imagenAmpliada").src = src;
    }

function cerrarModal() {
    document.getElementById("modalImagen").style.display = "none";
    }

const destacadoContainer = document.querySelector(".destacados-lista");

destacadoContainer.addEventListener("click", (e) => {
    e.preventDefault();
    modalImagen.style.display = "block";
});

